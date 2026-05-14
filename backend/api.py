from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from groq import Groq
from qdrant_client import QdrantClient, models
from fastembed import TextEmbedding, SparseTextEmbedding, LateInteractionTextEmbedding
from fastapi.middleware.cors import CORSMiddleware
import re
from pathlib import Path
from dotenv import load_dotenv
import os
app = FastAPI()
# CORS configuration to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
load_dotenv(Path(__file__).parent / ".env")
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
# Connect to Qdrant
if QDRANT_API_KEY:
    # cloud mode(with API key)
    client = QdrantClient(url=os.getenv("QDRANT_URL"), api_key=QDRANT_API_KEY)
else:
    # local mode(no API key)
    client = QdrantClient(url=os.getenv("QDRANT_URL"))
collection_name = "documentation"
# Load embedding models

DENSE_MODEL_ID = "BAAI/bge-base-en-v1.5"
SPARSE_MODEL_ID = "prithivida/Splade_PP_en_v1"
COLBERT_MODEL_ID = "colbert-ir/colbertv2.0"

dense_model = TextEmbedding(DENSE_MODEL_ID)
sparse_model = SparseTextEmbedding(SPARSE_MODEL_ID)
colbert_model = LateInteractionTextEmbedding(COLBERT_MODEL_ID)
# stream LLM responses from Groq
def stream_llm(prompt, system_prompt):
    stream = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        stream=True,
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

@app.get("/chat")
def chat(query: str):
    # Replace code placeholders
    def inject_code_blocks(text: str, payload: dict) -> str:

        codes = payload.get("codes", [])

        code_lookup = {}
        for item in codes:
            lang = item.get("language")
            code_id = item.get("id")
            code_content = item.get("code")

            if lang and code_id and code_content:
                code_lookup[(lang, code_id)] = code_content

        pattern = r"```(\w+)_code_(\d+)```"

        def replacer(match):
            language = match.group(1)
            code_id = int(match.group(2))

            code_content = code_lookup.get((language, code_id))

            if code_content:
                return f"\n```{language}\n{code_content}\n```\n"
            else:
                return match.group(0)

        return re.sub(pattern, replacer, text)

    # Generate query embeddings
    user_dense_vector = next(dense_model.query_embed(query))
    user_sparse_vector = next(sparse_model.query_embed(query)).as_object()
    user_multivector = next(colbert_model.query_embed(query))

    # Hybrid retrieval
    hybrid_query = [
        models.Prefetch(query=user_dense_vector, using="dense", limit=50),
        models.Prefetch(query=user_sparse_vector, using="sparse", limit=50),
    ]

    fusion_query = models.Prefetch(
        prefetch=hybrid_query,
        query=models.FusionQuery(fusion=models.Fusion.RRF),
        limit=50,
    )

    # ColBERT reranking
    response = client.query_points(
        collection_name=collection_name,
        prefetch=fusion_query,
        query=user_multivector,
        using="colbert",
        limit=3,
        with_payload=True,
    )

    # Build RAG context
    contexts = []

    for i, hit in enumerate(response.points, 1):

        raw_text = hit.payload.get("text", "")
        formatted_text = inject_code_blocks(raw_text, hit.payload)

        source = hit.payload.get("source", "unknown")

        block = f"""Context {i}: (from {source}):{formatted_text.strip()}"""
        contexts.append(block)

    structured_context = "\n\n".join(contexts)

    # Replace this with your retrieval pipeline

    system_prompt = """
    You are a technical documentation assistant.
    Answer the question using ONLY the sources below.
    If the answer is not contained in the sources, say:
    "I cannot find the answer in the provided documentation."
    Always cite the source number like [1], [2], or [3].
    Do not use prior knowledge. Only rely on the context.
    """

    user_prompt = f"""
    You are given the following documentation:
    {structured_context}

    Answer this question:
    {query}

    Answer:
    """

    return StreamingResponse(
        stream_llm(user_prompt, system_prompt),
        media_type="text/event-stream"
    )