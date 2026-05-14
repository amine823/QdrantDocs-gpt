---
title: Sycamore
---
## Sycamore
Sycamore is an LLM-powered data preparation, processing, and analytics system for complex, unstructured documents like PDFs, HTML, presentations, and more. With Aryn, you can prepare data for GenAI and RAG applications, power high-quality document processing workflows, and run analytics on large document collections with natural language.
You can use the Qdrant connector to write into and read documents from Qdrant collections.
You can find an end-to-end example usage of the Qdrant connector here.
## Writing to Qdrant
To write a Docset to a Qdrant collection in Sycamore, use the `docset.write.qdrant(....)` function. The Qdrant writer accepts the following arguments:
 `client_params`: Parameters that are passed to the Qdrant client constructor. See more information in the Client API Reference.
 `collection_params`: Parameters that are passed into the `qdrant_client.QdrantClient.create_collection` method. See more information in the Client API Reference.
 `vector_name`: The name of the vector in the Qdrant collection. Defaults to `None`.
 `execute`: Execute the pipeline and write to Qdrant on adding this operator. If `False`, will return a `DocSet` with this write in the plan. Defaults to `True`.
 `kwargs`: Keyword arguments to pass to the underlying execution engine.
```python
ds.write.qdrant(
    {
        "url": "the local Qdrant dashboard",
        "timeout": 50,
    },
    {
        "collection_name": "{collection_name}",
        "vectors_config": {
            "size": 384,
            "distance": "Cosine",
        },
    },
)
```
## Reading from Qdrant
To read a Docset from a Qdrant collection in Sycamore, use the `docset.read.qdrant(....)` function. The Qdrant reader accepts the following arguments:
 `client_params`: Parameters that are passed to the Qdrant client constructor. See more information in theClient API Reference.
 `query_params`: Parameters that are passed into the `qdrant_client.QdrantClient.query_points` method. See more information in the Client API Reference.
 `kwargs`: Keyword arguments to pass to the underlying execution engine.
```python
docs = ctx.read.qdrant(
    {
        "url": "the linked resource
        "api_key": "",
    },
    {"collection_name": "{collection_name}", "limit": 100, "using": "{optional_vector_name}"},
).take_all()
```
## 📚 Further Reading
 Sycamore Reference
 Sycamore
