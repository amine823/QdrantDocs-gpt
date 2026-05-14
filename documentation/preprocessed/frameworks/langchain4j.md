---
title: LangChain4j
---
# LangChain for Java
LangChain for Java, also known as Langchain4J, is a community port of Langchain for building context-aware AI applications in Java
You can use Qdrant as a vector store in LangChain4j through the `langchain4j-qdrant` module.
## Setup
Add the `langchain4j-qdrant` to your project dependencies.
```xml
    dev.langchain4j
    langchain4j-qdrant
    VERSION
```
## Usage
Before you use the following code sample, customize the following values for your configuration:
 `YOUR_COLLECTION_NAME`: Use our Collections guide to create or
 list collections.
 `YOUR_HOST_URL`: Use the GRPC URL for your system. If you used the Quick Start guide,
 it may be If you've deployed in the Qdrant Cloud, you may have a
 longer URL such as `
 `YOUR_API_KEY`: Substitute the API key associated with your configuration.
```java
import dev.langchain4j.store.embedding.EmbeddingStore;
import dev.langchain4j.store.embedding.qdrant.QdrantEmbeddingStore;
EmbeddingStore embeddingStore =
    QdrantEmbeddingStore.builder()
        // Ensure the collection is configured with the appropriate dimensions
        // of the embedding model.
        // Reference the linked resource
        .collectionName("YOUR_COLLECTION_NAME")
        .host("YOUR_HOST_URL")
        // GRPC port of the Qdrant server
        .port(6334)
        .apiKey("YOUR_API_KEY")
        .build();
```
`QdrantEmbeddingStore` supports all the semantic features of LangChain4j.
## Further Reading
 You can refer to the LangChain4j examples to get started.
 Source Code
