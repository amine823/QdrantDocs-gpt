---
title: CocoIndex
---
# CocoIndex
CocoIndex is a high performance ETL framework to transform data for AI, with real-time incremental processing.
Qdrant is available as a native built-in vector database to store and retrieve embeddings.
Install CocoIndex:
```bash
pip install -U cocoindex
```
Install Postgres with Docker Compose:
```bash
docker compose -f ",
    ),
    primary_key_fields=["id_field"],
    setup_by_user=True,
)
```
The spec takes the following fields:
 `collection_name` (type: str, required): The name of the collection to export the data to.
 `grpc_url` (type: str, optional): The gRPC URL of the Qdrant instance. Defaults to
 `api_key` (type: str, optional). API key to authenticate requests with.
Before exporting, you must create a collection with a vector name that matches the vector field name in CocoIndex, and set `setup_by_user=True` during export.
## Further Reading
 CocoIndex Documentation
 Example Code to build text embeddings with Qdrant
