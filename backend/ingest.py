import json
from pathlib import Path
from qdrant_client import QdrantClient, models
from fastembed import TextEmbedding, SparseTextEmbedding, LateInteractionTextEmbedding
import onnxruntime as ort

# Load qdrant client
client = QdrantClient(
    url="QDRANT_URL"
)
collection_name = "documentation"

# Model configurations
DENSE_MODEL_ID = "BAAI/bge-base-en-v1.5"  # 768-dim
SPARSE_MODEL_ID = "prithivida/Splade_PP_en_v1"  # SPLADE sparse
COLBERT_MODEL_ID = "colbert-ir/colbertv2.0"  # 128-dim multivector

'''available_providers = ort.get_available_providers()
if "CUDAExecutionProvider" in available_providers:
    print("CUDA is available. Using GPU for embedding generation.")
    dense_model = TextEmbedding(DENSE_MODEL_ID, providers=["CUDAExecutionProvider"])
    sparse_model = SparseTextEmbedding(SPARSE_MODEL_ID)
    colbert_model = LateInteractionTextEmbedding(COLBERT_MODEL_ID, providers=["CUDAExecutionProvider"])
else:

print("CUDA is not available. Using CPU for embedding generation.")
'''
dense_model = TextEmbedding(DENSE_MODEL_ID)
sparse_model = SparseTextEmbedding(SPARSE_MODEL_ID)
colbert_model = LateInteractionTextEmbedding(COLBERT_MODEL_ID)
# Config

CHUNKS_FILE = Path("./documentation/dataset/chunks.json")
BATCH_SIZE = 64

# Load chunks

chunks = json.loads(CHUNKS_FILE.read_text(encoding="utf-8"))
total_batches = (len(chunks) - 1) // BATCH_SIZE + 1

for batch_idx, start in enumerate(range(0, len(chunks), BATCH_SIZE),1):
    batch_chunks = chunks[start:start + BATCH_SIZE]
    texts = [c["text"] for c in batch_chunks]
    # generate embeddings for all items 
    dense_embeds = list(dense_model.embed(texts, normalize_embeddings=True))
    sparse_embeds = list(sparse_model.embed(texts))
    colbert_multivectors = list(colbert_model.embed(texts))

# Indexing

    points = []
    for i ,chunk in enumerate(batch_chunks):

    # Create sparse vector (keyword matching)
        sparse_vector = sparse_embeds[i].as_object()

        # Create dense vector (semantic understanding)
        dense_vector = dense_embeds[i]

        # Create ColBERT multivector (token-level understanding)
        colbert_vector = colbert_multivectors[i]

        points.append(
            models.PointStruct(
                id= start + i,
                vector={
                    "dense": dense_vector,
                    "sparse": sparse_vector,
                    "colbert": colbert_vector,
                },
                payload=chunk
            )
        )

    #  Upsert batch
    client.upsert(collection_name=collection_name, points=points)
    print(f"✅ Uploaded batch {batch_idx}/{total_batches} ({len(points)} points)")

print("🎉 All chunks uploaded successfully!")