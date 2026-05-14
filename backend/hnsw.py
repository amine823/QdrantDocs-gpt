from qdrant_client import QdrantClient, models

client = QdrantClient(url="QDRANT_URL")

client.update_collection(
    collection_name="documentation",
    vectors_config={
        "dense": models.VectorParamsDiff(
            hnsw_config=models.HnswConfigDiff(
                m=64,
                ef_construct=200
            )
        )
    }
)
