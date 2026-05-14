from qdrant_client import QdrantClient, models
from fastembed import TextEmbedding, SparseTextEmbedding, LateInteractionTextEmbedding
import json
from datetime import datetime
import os


# -----------------------
# Connect to Qdrant
# -----------------------
client = QdrantClient(url="http://localhost:6333")
collection_name = "documentation"

# -----------------------
# Load embedding models
# -----------------------
DENSE_MODEL_ID = "BAAI/bge-base-en-v1.5"
SPARSE_MODEL_ID = "prithivida/Splade_PP_en_v1"
COLBERT_MODEL_ID = "colbert-ir/colbertv2.0"

dense_model = TextEmbedding(DENSE_MODEL_ID)
sparse_model = SparseTextEmbedding(SPARSE_MODEL_ID)
colbert_model = LateInteractionTextEmbedding(COLBERT_MODEL_ID)

def dense_retrieve(query):
    # Generate dense embedding
    dense_query = next(dense_model.query_embed(query))
    return client.query_points(
        collection_name=collection_name,
        query=dense_query,
        using="dense",
        limit=10,
        with_payload=True,
    )

def sparse_retrieve(query):
    # Generate sparse embedding
    sparse_vector = next(sparse_model.query_embed(query))
    sparse_query = models.SparseVector(
    indices=sparse_vector.indices,
    values=sparse_vector.values,
    )
    return client.query_points(
        collection_name=collection_name,
        query=sparse_query,
        using="sparse",
        limit=10,
        with_payload=True,
    )

def hybrid_retrieve(query):
    # Generate both embeddings
    dense_query = next(dense_model.query_embed(query))
    sparse_query = next(sparse_model.query_embed(query)).as_object()

    # Prefetch queries - global filter will be automatically applied to both
    hybrid_query = [
        models.Prefetch(query=dense_query, using="dense", limit=100),
        models.Prefetch(query=sparse_query, using="sparse", limit=100),
    ]

    return client.query_points(
        collection_name=collection_name,
        prefetch=hybrid_query,
        query=models.FusionQuery(fusion=models.Fusion.RRF),  # Final stage can use either embedding
        limit=10,
        with_payload=True,
    )

def colbert_retrieve(query):
    # Generate both embeddings
    dense_query = next(dense_model.query_embed(query))
    sparse_query = next(sparse_model.query_embed(query)).as_object()

    # Prefetch queries - global filter will be automatically applied to both
    hybrid_query = [
        models.Prefetch(query=dense_query, using="dense", limit=100),
        models.Prefetch(query=sparse_query, using="sparse", limit=100),
    ]

    # Fusion stage - combine candidates with RRF
    fusion_query = models.Prefetch(
        prefetch=hybrid_query,
        query=models.FusionQuery(fusion=models.Fusion.RRF),
        limit=100,
    )
    # Generate ColBERT multivector
    colbert_query = next(colbert_model.query_embed(query))

    return client.query_points(
        collection_name=collection_name,
        prefetch=fusion_query,
        query=colbert_query,
        using="colbert",
        limit=10,
        with_payload=True,
    )

def store(output_file, new_entry):
    # If file exists, load it
    if os.path.exists(output_file):
        with open(output_file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Append new entry
    data.append(new_entry)

    # Write back full file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def merge_results(query, systems_dict):
    pooled = {}
    
    for system_name, response in systems_dict.items():
        for rank, point in enumerate(response.points, start=1):
            chunk_id = str(point.id)

            if chunk_id not in pooled:
                pooled[chunk_id] = {
                    "id": chunk_id,
                    "section": point.payload.get("section"),
                    "text": point.payload.get("text"),
                    "systems": {system_name: rank},  # store rank
                }
            else:
                pooled[chunk_id]["systems"][system_name] = rank

    return {
        "query": query,
        "candidate_chunks": list(pooled.values())
    }


def export_readable(entry, output_file):
    with open(output_file, "a", encoding="utf-8") as f:
        f.write("\n")
        f.write("=" * 80 + "\n")
        f.write(f"QUERY:\n{entry['query']}\n")
        f.write("=" * 80 + "\n\n")

        for chunk in entry["candidate_chunks"]:
            f.write("-" * 80 + "\n")
            f.write(f"Chunk ID: {chunk['id']}\n")

            # Format systems with ranks
            systems_with_ranks = ", ".join(
                f"{sys} {rank}"
                for sys, rank in chunk["systems"].items()
            )

            f.write(f"Retrieved by: {systems_with_ranks}\n")
            f.write(f"Section: {chunk.get('section', '')}\n")
            f.write("-" * 80 + "\n\n")

            text = chunk.get("text", "")
            f.write(text + "\n\n")

            f.write("[RELEVANT? 2 / 1 / 0]\n\n")

        f.write("\n\n")


if __name__ == "__main__":
    
    results_file = "./evaluation/evaluation_dataset.json"
    queries = [
        #Exact API Queries
        "How to batch update points using Python?",
        "How to delete specific payload keys using delete_payload?",
        "Example of update_vectors operation.",
        #Semantic / Paraphrased Queries
        "How can I modify several vectors at once?",
        "How do I remove one metadata field without touching others?",
        "How can I completely replace the metadata of a point?",
        #comparison queries
        "What is the difference between set_payload and overwrite_payload?",
        "When should I use clear_payload instead of delete_payload?",
        #Task oriented Queries
        "How to migrate to a new embedding model without downtime?",
        "How to perform bulk operations on points?",
        "How does Qdrant handles versioning of data updates?",
        #Vague Queries
        "How to change existing data in Qdrant?",
        "How are vector updates precessed internally?",
        "How does Qdrant manage metadata?",
        #Filtering + querying
        "How to filter points by a payload field?",
        "How to search vectors with a metadata condition?",
        "How to apply multiple filters in a query?",
        #collection and index management
        "How to create a collection with multiple vector fields?",
        "How to configure vector size and distance metric?",
        "How to add a sparse vector to an existing collection?",
        #Deletion and data integrity
        "How to delete specific points by ID?",
        "How to remove only vectors but keep payload?",
        #Hybrid and retrieval concepts
        "What is hybrid search in Qdrant?",
        "Difference between dense and sparse vectors?",
        "How does RRF fusion work?",
        #Performance and internal mechanics
        "How does Qdrant optimize storage after updates?",
        "How are updates written internally (WAL or segments)?",
    ]
    for query in queries:
        systems = {
            "dense": dense_retrieve(query),
            "sparse": sparse_retrieve(query),
            "hybrid": hybrid_retrieve(query),
            "colbert": colbert_retrieve(query),
        }

        merged_entry = merge_results(query, systems)

        store(results_file, merged_entry)
        export_readable(merged_entry, "./evaluation/annotation_readable.md")
