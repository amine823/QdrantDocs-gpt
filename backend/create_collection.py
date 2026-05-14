from qdrant_client import QdrantClient, models
client = QdrantClient(
    url="QDRANT_URL"
)
collection_name = "documentation"

# Clean state
if client.collection_exists(collection_name=collection_name):
    client.delete_collection(collection_name=collection_name)
client.create_collection(
    collection_name=collection_name,
    vectors_config={
        # Dense vectors for semantic understanding
        "dense": models.VectorParams(size=768, distance=models.Distance.COSINE),
        # ColBERT multivectors for fine-grained reranking
        "colbert": models.VectorParams(
            size=128,
            distance=models.Distance.COSINE,
            multivector_config=models.MultiVectorConfig(
                comparator=models.MultiVectorComparator.MAX_SIM
            ),
            hnsw_config=models.HnswConfigDiff(
                m=0  # Disable HNSW , used only for reranking
            ),
        ),
    },
    sparse_vectors_config={
        # Sparse vectors for exact keyword matching
        "sparse": models.SparseVectorParams(
            index=models.SparseIndexParams(on_disk=True)
        )
    },
)
print("✅ Collection created")
