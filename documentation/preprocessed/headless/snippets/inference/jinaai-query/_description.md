This code snippet illustrates how to use the Jina AI API for query-time inference on Qdrant Cloud. Instead of supplying an explicit query vector, the query provides text, along with the name of an Jina AI model. When the model name is prepended with `jinaai/`, the Qdrant Cloud Inference proxy uses the Jina AI API to infer embeddings out of the provided text. Qdrant will search with the resulting vector. The request also shows how to pass Jina AI-specific parameters to the API. In this case, the request provides the Jina AI API key and the `dimensions` parameter.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient(
  host: "xyz-example.qdrant.io",
  port: 6334,
  https: true,
  apiKey: "<your-api-key>"
);

await client.QueryAsync(
    collectionName: "{collection_name}",
    query: new Document()
    {
        Model = "jinaai/jina-clip-v2",
        Text = "Mission to Mars",
        Options = { ["jina-api-key"] = "<YOUR_JINAAI_API_KEY>", ["dimensions"] = 512 },
    }
);
```


```go
import (
	"context"

	"github.com/qdrant/go-client/qdrant"
)

client, err := qdrant.NewClient(&qdrant.Config{
    Host:   "xyz-example.qdrant.io",
    Port:   6334,
    APIKey: "<paste-your-api-key-here>",
    UseTLS: true,
})

client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "{collection_name}",
	Query: qdrant.NewQueryNearest(
		qdrant.NewVectorInputDocument(&qdrant.Document{
			Text:  "Mission to Mars",
			Model: "jinaai/jina-clip-v2",
			Options: qdrant.NewValueMap(map[string]any{
				"jina-api-key": "<YOUR_JINAAI_API_KEY>",
				"dimensions":   512,
			}),
		}),
	),
})
```


```http
POST /collections/{collection_name}/points/query
{
  "query": {
    "text": "Mission to Mars",
    "model": "jinaai/jina-clip-v2",
    "options": {
      "jina-api-key": "<YOUR_JINAAI_API_KEY>",
      "dimensions": 512
    }
  }
}
```


```java
import static io.qdrant.client.QueryFactory.nearest;
import static io.qdrant.client.ValueFactory.value;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.Document;
import io.qdrant.client.grpc.Points.QueryPoints;
import java.util.Map;

QdrantClient client =
    new QdrantClient(
        QdrantGrpcClient.newBuilder("xyz-example.qdrant.io", 6334, true)
            .withApiKey("<your-api-key")
            .build());
client
    .queryAsync(
        QueryPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setQuery(
                nearest(
                    Document.newBuilder()
                        .setModel("jinaai/jina-clip-v2")
                        .setText("Mission to Mars")
                        .putAllOptions(
                            Map.of(
                                "jina-api-key",
                                value("<YOUR_JINAAI_API_KEY>"),
                                "dimensions",
                                value(512)))
                        .build()))
            .build())
    .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333", 
    api_key="<your-api-key>", 
    cloud_inference=True
)

client.query_points(
    collection_name="{collection_name}",
    query=models.Document(
        text="Mission to Mars", 
        model="jinaai/jina-clip-v2", 
        options={
            "jina-api-key": "<your_jinaai_api_key>", 
            "dimensions": 512
        }
    )
)
```


```rust
use qdrant_client::{
    Qdrant,
    qdrant::{Document, Query, QueryPointsBuilder, Value},
};
use std::collections::HashMap;

let client = Qdrant::from_url("<your-qdrant-url>").build().unwrap();

let mut options = HashMap::<String, Value>::new();
options.insert("jina-api-key".to_string(), "<YOUR_JINAAI_API_KEY>".into());
options.insert("dimensions".to_string(), 512.into());

client
    .query(
        QueryPointsBuilder::new("{collection_name}")
            .query(Query::new_nearest(Document {
                text: "Mission to Mars".into(),
                model: "jinaai/jina-clip-v2".into(),
                options,
            }))
            .build(),
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.query("{collection_name}", {
    query: {
        text: 'Mission to Mars',
        model: 'jinaai/jina-clip-v2',
        options: {
            'jina-api-key': '<your_jinaai_api_key>',
            dimensions: 512,
        },
    },
});
```
