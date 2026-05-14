from qdrant_client import QdrantClient, models
from fastembed import TextEmbedding, SparseTextEmbedding, LateInteractionTextEmbedding
import json
from datetime import datetime
import os


# Connect to Qdrant
client = QdrantClient(url="http://localhost:6333")
collection_name = "documentation"

# Load embedding models
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
        search_params=models.SearchParams(
            hnsw_ef=256
        ),
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
        search_params=models.SearchParams(hnsw_ef=256)
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
        search_params=models.SearchParams(hnsw_ef=256)
    )

if __name__ == "__main__":
    
    queries = {
        #Exact API Queries
        "1":"How to batch update points using Python?",
        "2":"How to delete specific payload keys using delete_payload?",
        "3":"Example of update_vectors operation.",
        #Semantic / Paraphrased Queries
        "4":"How can I modify several vectors at once?",
        "5":"How do I remove one metadata field without touching others?",
        "6":"How can I completely replace the metadata of a point?",
        #comparison queries
        "7":"What is the difference between set_payload and overwrite_payload?",
        "8":"When should I use clear_payload instead of delete_payload?",
        #Task oriented Queries
        "9":"How to migrate to a new embedding model without downtime?",
        "10":"How to perform bulk operations on points?",
        "11":"How does Qdrant handles versioning of data updates?",
        #Vague Queries
        "12":"How to change existing data in Qdrant?",
        "13":"How are vector updates precessed internally?",
        "14":"How does Qdrant manage metadata?",
        #Filtering + querying
        "15":"How to filter points by a payload field?",
        "16":"How to search vectors with a metadata condition?",
        "17":"How to apply multiple filters in a query?",
        #collection and index management
        "18":"How to create a collection with multiple vector fields?",
        "19":"How to configure vector size and distance metric?",
        "20":"How to add a sparse vector to an existing collection?",
        #Deletion and data integrity
        "21":"How to delete specific points by ID?",
        "22":"How to remove only vectors but keep payload?",
        #Hybrid and retrieval concepts
        "23":"What is hybrid search in Qdrant?",
        "24":"Difference between dense and sparse vectors?",
        "25":"How does RRF fusion work?",
        #Performance and internal mechanics
        "26":"How does Qdrant optimize storage after updates?",
        "27":"How are updates written internally (WAL or segments)?",
    }
    runs1 = {}
    runs2 = {}
    runs3 = {}
    runs4 = {}
    for query_id, query in queries.items():
        results1 = dense_retrieve(query)
        chunks_ids = [point.id for point in results1.points]
        runs1[query_id] = chunks_ids

        results2 = sparse_retrieve(query)
        chunks_ids = [point.id for point in results2.points]
        runs2[query_id] = chunks_ids

        results3 = hybrid_retrieve(query)
        chunks_ids = [point.id for point in results3.points]
        runs3[query_id] = chunks_ids

        results4 = colbert_retrieve(query)
        chunks_ids = [point.id for point in results4.points]
        runs4[query_id] = chunks_ids

    with open("evaluation/runs/dense.json", "w", encoding="utf-8") as f:
        json.dump(runs1, f, indent=2)

    with open("evaluation/runs/sparse.json", "w", encoding="utf-8") as f:
        json.dump(runs2, f, indent=2)

    with open("evaluation/runs/hybrid.json", "w", encoding="utf-8") as f:
        json.dump(runs3, f, indent=2)

    with open("evaluation/runs/colbert.json", "w", encoding="utf-8") as f:
        json.dump(runs4, f, indent=2)