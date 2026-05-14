Creates a full-text index on `title` with phrase matching and ASCII folding enabled.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

await client.CreatePayloadIndexAsync(
    collectionName: "books",
    fieldName: "title",
    schemaType: PayloadSchemaType.Text,
    indexParams: new PayloadIndexParams
    {
        TextIndexParams = new TextIndexParams
        {
            Tokenizer = TokenizerType.Word,
            AsciiFolding = true,
            PhraseMatching = true,
            Lowercase = true,
        },
    }
);
```


```go
client.CreateFieldIndex(context.Background(), &qdrant.CreateFieldIndexCollection{
	CollectionName: "books",
	FieldName:      "title",
	FieldType:      qdrant.FieldType_FieldTypeText.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsText(
		&qdrant.TextIndexParams{
			Tokenizer:      qdrant.TokenizerType_Word,
			Lowercase:      qdrant.PtrOf(true),
			AsciiFolding:   qdrant.PtrOf(true),
			PhraseMatching: qdrant.PtrOf(true),
		}),
})
```


```http
PUT /collections/books/index?wait=true
{
  "field_name": "title",
  "field_schema": {
    "type": "text",
    "ascii_folding": true,
    "phrase_matching": true
  }
}
```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;
import io.qdrant.client.grpc.Collections.TextIndexParams;
import io.qdrant.client.grpc.Collections.TokenizerType;

QdrantClient client =

client
    .createPayloadIndexAsync(
        "books",
        "title",
        PayloadSchemaType.Text,
        PayloadIndexParams.newBuilder()
            .setTextIndexParams(
                TextIndexParams.newBuilder()
                    .setTokenizer(TokenizerType.Word)
                    .setAsciiFolding(true)
                    .setPhraseMatching(true)
                    .setLowercase(true)
                    .build())
            .build(),
        null,
        null,
        null)
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
    field_name="title",
    field_schema=models.TextIndexParams(type=models.TextIndexType.TEXT, ascii_folding=True, phrase_matching=True),
)
```


```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder, FieldType, TextIndexParamsBuilder, TokenizerType,
};

let params = TextIndexParamsBuilder::new(TokenizerType::Word)
    .ascii_folding(true)
    .phrase_matching(true)
    .lowercase(true)
    .build();

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new("books", "title", FieldType::Text)
            .field_index_params(params),
    )
    .await?;
```


```typescript
client.createPayloadIndex("books", {
  field_name: "title",
  field_schema: {
    type: "text",
    ascii_folding: true,
    phrase_matching: true,
  },
});
```
