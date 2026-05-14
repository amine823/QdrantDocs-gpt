---
title: Kotaemon
---
# Kotaemon
Kotaemon is open-source clean & customizable RAG UI for chatting with your documents. Built with both end users and developers in mind.
Qdrant is supported as a vectorstore in Kotaemon for ingesting and retrieving documents.
## Configuration
 Refer to Getting started guide to set up Kotaemon.
 To configure Kotaemon to use Qdrant as the vector store, update the `flowsettings.py` as follows.
```python
KH_VECTORSTORE = {
    "__type__": "kotaemon.storages.QdrantVectorStore",
    "url": "the linked resource
    "api_key": "'",
    "client_kwargs": {} # Additional options to pass to qdrant_client.QdrantClient
}
```
 Restart Kotaemon for the changes to take effect.
The reference for all the Qdrant client options can be found here
## Further reading
 Kotaemon Documentation
 Source
