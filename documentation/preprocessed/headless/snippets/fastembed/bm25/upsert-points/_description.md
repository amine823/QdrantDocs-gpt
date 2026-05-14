This code snippet uses the Qdrant and FastEmbed integration to infer and upsert documents into a collection configured for BM25 sparse vectors. Each document is converted into a sparse BM25 vector, with the conversion incorporating the avg_len parameter of the BM25 scoring formula — the average document length in the corpus — which must be provided by the user. The resulting vector and the document’s text, stored as payload, are then upserted to the collection.

```python
#Estimating the average length of the documents in the corpus
avg_documents_length = sum(len(document.split()) for document in documents) / len(documents)

client.upsert(
    collection_name="{bm25_collection_name}",
    points=[
        models.PointStruct(
            id=i,
            payload={
                "text": documents[i]
            },
            vector={
                # Sparse vector from BM25
                "bm25": models.Document(
                    text=documents[i],
                    model="Qdrant/bm25",
                    options={"avg_len": avg_documents_length}   
                    #Average length of documents in the corpus 
                    # (a part of the BM25 formula)
                )
            },
        )
        for i in range(len(documents))
    ],
)
```
