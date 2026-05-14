This code snippet illustrates how to use smaller vectors for the initial prefetching of candidates from a large collection, followed by re-scoring with the original-sized vectors to improve accuracy, combined with inference. For the smaller vector, it employs Matryoshka Representation Learning (MRL) to reduce the dimensionality of embeddings by specifying the `mrl` parameter in the `options` object.

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
    prefetch:
    [
        new()
        {
            Query = new Document()
            {
                Model = "openai/text-embedding-3-small",
                Text = "How to bake cookies?",
                Options = { ["openai-api-key"] = "<YOUR_OPENAI_API_KEY>", ["mrl"] = 64 },
            },
            Using = "small",
            Limit = 1000,
        },
    ],
    query: new Document()
    {
        Model = "openai/text-embedding-3-small",
        Text = "How to bake cookies?",
        Options = { ["openai-api-key"] = "<YOUR_OPENAI_API_KEY>" },
    },
    usingVector: "large",
    limit: 10
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
	Prefetch: []*qdrant.PrefetchQuery{
		{
			Query: qdrant.NewQueryNearest(
				qdrant.NewVectorInputDocument(&qdrant.Document{
					Model: "openai/text-embedding-3-small",
					Text:  "How to bake cookies?",
					Options: qdrant.NewValueMap(map[string]any{
						"mrl":            64,
						"openai-api-key": "<YOUR_OPENAI_API_KEY>",
					}),
				}),
			),
			Using: qdrant.PtrOf("small"),
			Limit: qdrant.PtrOf(uint64(1000)),
		},
	},
	Query: qdrant.NewQueryNearest(
		qdrant.NewVectorInputDocument(&qdrant.Document{
			Model: "openai/text-embedding-3-small",
			Text:  "How to bake cookies?",
			Options: qdrant.NewValueMap(map[string]any{
				"openai-api-key": "<YOUR_OPENAI_API_KEY>",
			}),
		}),
	),
	Using: qdrant.PtrOf("large"),
	Limit: qdrant.PtrOf(uint64(10)),
})
```


```http
POST /collections/{collection_name}/points/query
{
  "prefetch": {
    "query": {
      "text": "How to bake cookies?",
      "model": "openai/text-embedding-3-small",
      "options": {
        "openai-api-key": "<YOUR_OPENAI_API_KEY>",
        "mrl": 64
      }
    },
    "using": "small",
    "limit": 1000
  },
  "query": {
    "text": "How to bake cookies?",
    "model": "openai/text-embedding-3-small",
    "options": {
      "openai-api-key": "<YOUR_OPENAI_API_KEY>"
    }
  },
  "using": "large",
  "limit": 10
}
```


```java
import static io.qdrant.client.QueryFactory.nearest;
import static io.qdrant.client.ValueFactory.value;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points;
import io.qdrant.client.grpc.Points.Document;
import io.qdrant.client.grpc.Points.PrefetchQuery;
import java.util.Map;

QdrantClient client =
    new QdrantClient(
        QdrantGrpcClient.newBuilder("xyz-example.qdrant.io", 6334, true)
            .withApiKey("<your-api-key")
            .build());

client
    .queryAsync(
        Points.QueryPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .addPrefetch(
                PrefetchQuery.newBuilder()
                    .setQuery(
                        nearest(
                            Document.newBuilder()
                                .setModel("openai/text-embedding-3-small")
                                .setText("How to bake cookies?")
                                .putAllOptions(
                                    Map.of(
                                        "openai-api-key",
                                        value("<YOUR_OPENAI_API_KEY>"),
                                        "mrl",
                                        value(64)))
                                .build()))
                    .setUsing("small")
                    .setLimit(1000)
                    .build())
            .setQuery(
                nearest(
                    Document.newBuilder()
                        .setModel("openai/text-embedding-3-small")
                        .setText("How to bake cookies?")
                        .putAllOptions(Map.of("openai-api-key", value("<YOUR_OPENAI_API_KEY>")))
                        .build()))
            .setUsing("large")
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
        text="How to bake cookies?", 
        model="openai/text-embedding-3-small",
        options={"openai-api-key": "<YOUR_OPENAI_API_KEY>"}
    ),
    using="large",
    limit=10,
    prefetch=models.Prefetch(
        query=models.Document(
            text="How to bake cookies?",
            model="openai/text-embedding-3-small",
            options={
                "openai-api-key": "<YOUR_OPENAI_API_KEY>", 
                "mrl": 64
            } 
        ),
        using="small",
        limit=1000,
    )
)
```


```rust
use std::collections::HashMap;

use qdrant_client::{
    Qdrant,
    qdrant::{Document, PrefetchQueryBuilder, Query, QueryPointsBuilder, Value},
};

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .query(
        QueryPointsBuilder::new("{collection_name}")
            .add_prefetch(
                PrefetchQueryBuilder::default()
                    .query(Query::new_nearest(Document {
                        text: "How to bake cookies?".into(),
                        model: "openai/text-embedding-3-small".into(),
                        options: HashMap::<String, Value>::from_iter(vec![
                            (
                                "openai-api-key".to_string(),
                                Value::from("<YOUR_OPENAI_API_KEY>"),
                            ),
                            ("mrl".into(), Value::from(64)),
                        ]),
                    }))
                    .using("small")
                    .limit(1000_u64),
            )
            .query(Query::new_nearest(Document {
                text: "How to bake cookies?".into(),
                model: "openai/text-embedding-3-small".into(),
                options: HashMap::from_iter(vec![(
                    "openai-api-key".into(),
                    "<YOUR_OPENAI_API_KEY>".into(),
                )]),
            }))
            .using("large")
            .limit(10_u64)
            .build(),
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.query("{collection_name}", {
    prefetch: {
        query: {
            text: "How to bake cookies?",
            model: "openai/text-embedding-3-small",
            options: {
                "openai-api-key": "<YOUR_OPENAI_API_KEY>",
                mrl: 64,
            }
        },
        using: 'small',
        limit: 1000,
    },
    query: {
        text: "How to bake cookies?",
        model: "openai/text-embedding-3-small",
        options: {
            "openai-api-key": "<YOUR_OPENAI_API_KEY>"
        }
    },
    using: 'large',
    limit: 10,
});
```
