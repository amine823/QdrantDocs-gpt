Creates a keyword payload index on the `author` field to enable fast exact-match filtering.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

await client.CreatePayloadIndexAsync(
    collectionName: "books",
    fieldName: "author",
    schemaType: PayloadSchemaType.Keyword
);
```


```go
client.CreateFieldIndex(context.Background(), &qdrant.CreateFieldIndexCollection{
	CollectionName: "books",
	FieldName:      "author",
	FieldType:      qdrant.FieldType_FieldTypeKeyword.Enum(),
})
```


```http
PUT /collections/books/index?wait=true
{
    "field_name": "author",
    "field_schema": "keyword"
}
```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;

QdrantClient client =

client
    .createPayloadIndexAsync(
        "books", "author", PayloadSchemaType.Keyword, null, null, null, null)
    .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333",
    api_key="<your-api-key>",
    cloud_inference=True,
)

client.create_payload_index(
    collection_name="books",
    field_name="author",
    field_schema=models.PayloadSchemaType.KEYWORD
)
```


```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{CreateFieldIndexCollectionBuilder, FieldType};

client
    .create_field_index(CreateFieldIndexCollectionBuilder::new(
        "books",
        "author",
        FieldType::Keyword,
    ))
    .await?;
```


```typescript
client.createPayloadIndex("books", {
  field_name: "author",
  field_schema: "keyword",
});
```
