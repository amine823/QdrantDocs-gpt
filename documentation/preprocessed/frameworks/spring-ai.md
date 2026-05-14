---
title: Spring AI
---
# Spring AI
Spring AI is a Java framework that provides a Spring-friendly API and abstractions for developing AI applications.
Qdrant is available as supported vector database for use within your Spring AI projects.
## Installation
You can find the Spring AI installation instructions here.
Add the Qdrant boot starter package.
```xml
 org.springframework.ai
 spring-ai-qdrant-store-spring-boot-starter
```
## Usage
Configure Qdrant with Spring Boot’s `application.properties`.
```
spring.ai.vectorstore.qdrant.host=
spring.ai.vectorstore.qdrant.port=
spring.ai.vectorstore.qdrant.api-key=
spring.ai.vectorstore.qdrant.collection-name=
```
Learn more about these options in the configuration reference.
Or you can set up the Qdrant vector store with the `QdrantVectorStoreConfig` options.
```java
@Bean
public QdrantVectorStoreConfig qdrantVectorStoreConfig() {
    return QdrantVectorStoreConfig.builder()
        .withHost("")
        .withPort()
        .withCollectionName("")
        .withApiKey("")
        .build();
}
```
Build the vector store using the config and any of the support Spring AI embedding providers.
```java
@Bean
public VectorStore vectorStore(QdrantVectorStoreConfig config, EmbeddingClient embeddingClient) {
    return new QdrantVectorStore(config, embeddingClient);
}
```
You can now use the `VectorStore` instance backed by Qdrant as a vector store in the Spring AI APIs.
If the collection is not created in advance, QdrantVectorStore will attempt to create one using cosine similarity and the dimension of the configured EmbeddingClient.
## 📚 Further Reading
 Spring AI Qdrant reference
 Spring AI API reference
 Source Code
