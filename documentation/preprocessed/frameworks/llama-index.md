---
title: LlamaIndex
---
# LlamaIndex
Llama Index acts as an interface between your external data and Large Language Models. So you can bring your
private data and augment LLMs with it. LlamaIndex simplifies data ingestion and indexing, integrating Qdrant as a vector index.
Installing Llama Index is straightforward if we use pip as a package manager. Qdrant is not installed by default, so we need to
install it separately. The integration of both tools also comes as another package.
```bash
pip install llama-index llama-index-vector-stores-qdrant
```
Llama Index requires providing an instance of `QdrantClient`, so it can interact with Qdrant server.
```python
from llama_index.core.indices.vector_store.base import VectorStoreIndex
from llama_index.vector_stores.qdrant import QdrantVectorStore
import qdrant_client
client = qdrant_client.QdrantClient(
    "",
    api_key="", # For Qdrant Cloud, None for local instance
)
vector_store = QdrantVectorStore(client=client, collection_name="documents")
index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
```
## Further Reading
 LlamaIndex Documentation
 Example Notebook
 Source Code
