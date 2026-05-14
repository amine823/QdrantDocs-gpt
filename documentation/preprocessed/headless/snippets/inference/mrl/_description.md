This code snippet illustrates how to reduce the dimensionality of embeddings using Matryoshka Representation Learning (MRL) when using inference. It demonstrates how to insert a point into a Qdrant collection with a reduced-size vector by specifying the `mrl` parameter in the `options` object.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient(
    host: "xyz-example.qdrant.io",
    port: 6334,
    https: true,
    apiKey: "<your-api-key>"
);

await client.UpsertAsync(
    collectionName: "{collection_name}",
    points: new List<PointStruct>
    {
        new()
        {
            Id = 1,
            Vectors = new Dictionary<string, Vector>
            {
                ["large"] = new Document()
                {
                    Model = "openai/text-embedding-3-small",
                    Text = "Recipe for baking chocolate chip cookies",
                    Options = { ["openai-api-key"] = "<YOUR_OPENAI_API_KEY>" },
                },
                ["small"] = new Document()
                {
                    Model = "openai/text-embedding-3-small",
                    Text = "Recipe for baking chocolate chip cookies",
                    Options = { ["openai-api-key"] = "<YOUR_OPENAI_API_KEY>", ["mrl"] = 64 },
                },
            },
        },
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

client.Upsert(context.Background(), &qdrant.UpsertPoints{
	CollectionName: "{collection_name}",
	Points: []*qdrant.PointStruct{
		{
			Id: qdrant.NewIDNum(uint64(1)),
			Vectors: qdrant.NewVectorsMap(map[string]*qdrant.Vector{
				"large": qdrant.NewVectorDocument(&qdrant.Document{
					Model: "openai/text-embedding-3-small",
					Text:  "Recipe for baking chocolate chip cookies",
					Options: qdrant.NewValueMap(map[string]any{
						"openai-api-key": "<YOUR_OPENAI_API_KEY>",
					}),
				}),
				"small": qdrant.NewVectorDocument(&qdrant.Document{
					Model: "openai/text-embedding-3-small",
					Text:  "Recipe for baking chocolate chip cookies",
					Options: qdrant.NewValueMap(map[string]any{
						"openai-api-key": "<YOUR_OPENAI_API_KEY>",
						"mrl":            64,
					}),
				}),
			}),
		},
	},
})
```


```http
PUT /collections/{collection_name}/points?wait=true
{
  "points": [
    {
      "id": 1,
      "vector": {
        "large": {
          "text": "Recipe for baking chocolate chip cookies",
          "model": "openai/text-embedding-3-small",
          "options": {
            "openai-api-key": "<YOUR_OPENAI_API_KEY>"
          }
        },
        "small": {
          "text": "Recipe for baking chocolate chip cookies",
          "model": "openai/text-embedding-3-small",
          "options": {
            "openai-api-key": "<YOUR_OPENAI_API_KEY>",
            "mrl": 64
          }
        }
      }
    }
  ]
}
```


```java
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ValueFactory.value;
import static io.qdrant.client.VectorFactory.vector;
import static io.qdrant.client.VectorsFactory.namedVectors;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.Document;
import io.qdrant.client.grpc.Points.PointStruct;
import java.util.List;
import java.util.Map;

QdrantClient client =
    new QdrantClient(
        QdrantGrpcClient.newBuilder("xyz-example.qdrant.io", 6334, true)
            .withApiKey("<your-api-key")
            .build());

client
    .upsertAsync(
        "{collection_name}",
        List.of(
            PointStruct.newBuilder()
                .setId(id(1))
                .setVectors(
                    namedVectors(
                        Map.of(
                            "large",
                            vector(
                                Document.newBuilder()
                                    .setModel("openai/text-embedding-3-small")
                                    .setText("Recipe for baking chocolate chip cookies")
                                    .putAllOptions(
                                        Map.of(
                                            "openai-api-key", value("<YOUR_OPENAI_API_KEY>")))
                                    .build()),
                            "small",
                            vector(
                                Document.newBuilder()
                                    .setModel("openai/text-embedding-3-small")
                                    .setText("Recipe for baking chocolate chip cookies")
                                    .putAllOptions(
                                        Map.of(
                                            "openai-api-key",
                                            value("<YOUR_OPENAI_API_KEY>"),
                                            "mrl",
                                            value(64)))
                                    .build()))))
                .build()))
    .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333", 
    api_key="<your-api-key>", 
    cloud_inference=True
)

client.upsert(
    collection_name="{collection_name}",
    points=[
        models.PointStruct(
            id=1,
            vector={
                "large": models.Document(
                    text="Recipe for baking chocolate chip cookies",
                    model="openai/text-embedding-3-small",
                    options={"openai-api-key": "<YOUR_OPENAI_API_KEY>"}
                ),
                "small": models.Document(
                    text="Recipe for baking chocolate chip cookies",
                    model="openai/text-embedding-3-small",
                    options={
                        "openai-api-key": "<YOUR_OPENAI_API_KEY>",
                        "mrl": 64
                    },
                )
            },
        )
    ],
)
```


```rust
use std::collections::HashMap;

use qdrant_client::{
    Payload, Qdrant,
    qdrant::{Document, NamedVectors, PointStruct, UpsertPointsBuilder, Value},
};

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .upsert_points(
        UpsertPointsBuilder::new(
            "{collection_name}",
            vec![PointStruct::new(
                1,
                NamedVectors::default()
                    .add_vector(
                        "large",
                        Document {
                            text: "Recipe for baking chocolate chip cookies".into(),
                            model: "openai/text-embedding-3-small".into(),
                            options: HashMap::<String, Value>::from_iter(vec![(
                                "openai-api-key".into(),
                                "<YOUR_OPENAI_API_KEY>".into(),
                            )]),
                        },
                    )
                    .add_vector(
                        "small",
                        Document {
                            text: "Recipe for baking chocolate chip cookies".into(),
                            model: "openai/text-embedding-3-small".into(),
                            options: HashMap::<String, Value>::from_iter(vec![
                                (
                                    "openai-api-key".into(),
                                    Value::from("<YOUR_OPENAI_API_KEY>"),
                                ),
                                ("mrl".into(), Value::from(64)),
                            ]),
                        },
                    ),
                Payload::default(),
            )],
        )
        .wait(true),
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.upsert("{collection_name}", {
    points: [
        {
            id: 1,
            vector: {
                large: {
                    text: 'Recipe for baking chocolate chip cookies',
                    model: 'openai/text-embedding-3-small',
                    options: {
                        'openai-api-key': '<YOUR_OPENAI_API_KEY>',
                    },
                },
                small: {
                    text: 'Recipe for baking chocolate chip cookies',
                    model: 'openai/text-embedding-3-small',
                    options: {
                        'openai-api-key': '<YOUR_OPENAI_API_KEY>',
                        mrl: 64,
                    },
                },
            },
        },
    ],
});
```
