---
title: Nomic
---
# Nomic
The `nomic-embed-text-v1` model is an open source 8192 context length text encoder.
While you can find it on the Hugging Face Hub,
you may find it easier to obtain them through the Nomic Text Embeddings.
Once installed, you can configure it with the official Python client, FastEmbed or through direct HTTP requests.
Using Nomic Embeddings via the Nomic API/SDK requires configuring the Nomic API token.
You can use Nomic embeddings directly in Qdrant client calls. There is a difference in the way the embeddings
are obtained for documents and queries.
#### Upsert using Nomic SDK
The `task_type` parameter defines the embeddings that you get.
For documents, set the `task_type` to `search_document`:
```python
from qdrant_client import QdrantClient, models
from nomic import embed
output = embed.text(
    texts=["Qdrant is the best vector database!"],
    model="nomic-embed-text-v1",
    task_type="search_document",
)
client = QdrantClient()
client.upsert(
    collection_name="my-collection",
    points=models.Batch(
        ids=[1],
        vectors=output["embeddings"],
    ),
)
```
#### Upsert using FastEmbed
```python
from fastembed import TextEmbedding
from client import QdrantClient, models
model = TextEmbedding("nomic-ai/nomic-embed-text-v1")
output = model.embed(["Qdrant is the best vector database!"])
client = QdrantClient()
client.upsert(
    collection_name="my-collection",
    points=models.Batch(
        ids=[1],
        vectors=[embeddings.tolist() for embeddings in output],
    ),
)
```
#### Search using Nomic SDK
To query the collection, set the `task_type` to `search_query`:
```python
output = embed.text(
    texts=["What is the best vector database?"],
    model="nomic-embed-text-v1",
    task_type="search_query",
)
client.search(
    collection_name="my-collection",
    query_vector=output["embeddings"][0],
)
```
#### Search using FastEmbed
```python
output = next(model.embed("What is the best vector database?"))
client.search(
    collection_name="my-collection",
    query_vector=output.tolist(),
)
```
For more information, see the Nomic documentation on Text embeddings.
