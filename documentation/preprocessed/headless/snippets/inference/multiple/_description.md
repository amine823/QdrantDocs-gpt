This code snippet shows how to run multiple inference operations within a single request, even when models are hosted in different locations. The request generates three different named vectors for a single point: image embeddings using `jina-clip-v2` hosted by Jina AI, text embeddings using `all-minilm-l6-v2` hosted by Qdrant Cloud, and BM25 embeddings using the `bm25` model executed locally by the Qdrant cluster.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient(
host: "xyz-example.qdrant.io", port: 6334, https: true, apiKey: "<your-api-key>");

await client.UpsertAsync(
    collectionName: "{collection_name}",
    points: new List<PointStruct>
    {
        new()
        {
            Id = 1,
            Vectors = new Dictionary<string, Vector>
            {
                ["image"] = new Image()
                {
                    Model = "jinaai/jina-clip-v2",
                    Image_ = "https://qdrant.tech/example.png",
                    Options = { ["jina-api-key"] = "<YOUR_JINAAI_API_KEY>", ["dimensions"] = 512 },
                },
                ["text"] = new Document()
                {
                    Model = "sentence-transformers/all-minilm-l6-v2",
                    Text = "Mars, the red planet",
                },
                ["bm25"] = new Document() { Model = "qdrant/bm25", Text = "Mars, the red planet" },
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
				"image": qdrant.NewVectorImage(&qdrant.Image{
					Model: "jinaai/jina-clip-v2",
					Image: qdrant.NewValueString("https://qdrant.tech/example.png"),
					Options: qdrant.NewValueMap(map[string]any{
						"jina-api-key": "<YOUR_JINAAI_API_KEY>",
						"dimensions":   512,
					}),
				}),
				"text": qdrant.NewVectorDocument(&qdrant.Document{
					Model: "sentence-transformers/all-minilm-l6-v2",
					Text:  "Mars, the red planet",
				}),
				"my-bm25-vector": qdrant.NewVectorDocument(&qdrant.Document{
					Model: "qdrant/bm25",
					Text:  "Recipe for baking chocolate chip cookies",
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
        "image": {
          "image": "https://qdrant.tech/example.png",
          "model": "jinaai/jina-clip-v2",
          "options": {
            "jina-api-key": "<YOUR_JINAAI_API_KEY>",
            "dimensions": 512
          }
        },
        "text": {
          "text": "Mars, the red planet",
          "model": "sentence-transformers/all-minilm-l6-v2"
        },
        "bm25": {
          "text": "Mars, the red planet",
          "model": "qdrant/bm25"
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
import io.qdrant.client.grpc.Points.Image;
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
                            "image",
                            vector(
                                Image.newBuilder()
                                    .setModel("jinaai/jina-clip-v2")
                                    .setImage(value("https://qdrant.tech/example.png"))
                                    .putAllOptions(
                                        Map.of(
                                            "jina-api-key",
                                            value("<YOUR_JINAAI_API_KEY>"),
                                            "dimensions",
                                            value(512)))
                                    .build()),
                            "text",
                            vector(
                                Document.newBuilder()
                                    .setModel("sentence-transformers/all-minilm-l6-v2")
                                    .setText("Mars, the red planet")
                                    .build()),
                            "bm25",
                            vector(
                                Document.newBuilder()
                                    .setModel("qdrant/bm25")
                                    .setText("Mars, the red planet")
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
                "image": models.Image(
                    image="https://qdrant.tech/example.png",
                    model="jinaai/jina-clip-v2",
                    options={
                        "jina-api-key": "<your_jinaai_api_key>",
                        "dimensions": 512
                    },
                ),
                "text": models.Document(
                    text="Mars, the red planet",
                    model="sentence-transformers/all-minilm-l6-v2",
                ),
                "bm25": models.Document(
                    text="Mars, the red planet",
                    model="Qdrant/bm25",
                ),
            },
        )
    ],
)
```


```rust
use qdrant_client::{
    Payload, Qdrant,
    qdrant::{Document, Image, NamedVectors, PointStruct, UpsertPointsBuilder},
};
use std::collections::HashMap;

let client = Qdrant::from_url("<your-qdrant-url>").build()?;

let mut jina_options = HashMap::new();
jina_options.insert("jina-api-key".to_string(), "<YOUR_JINAAI_API_KEY>".into());
jina_options.insert("dimensions".to_string(), 512.into());

client
    .upsert_points(
        UpsertPointsBuilder::new(
            "{collection_name}",
            vec![PointStruct::new(
                1,
                NamedVectors::default()
                    .add_vector(
                        "image",
                        Image {
                            image: Some("https://qdrant.tech/example.png".into()),
                            model: "jinaai/jina-clip-v2".into(),
                            options: jina_options,
                        },
                    )
                    .add_vector(
                        "text",
                        Document {
                            text: "Mars, the red planet".into(),
                            model: "sentence-transformers/all-minilm-l6-v2".into(),
                            ..Default::default()
                        },
                    )
                    .add_vector(
                        "bm25",
                        Document {
                            text: "How to bake cookies?".into(),
                            model: "qdrant/bm25".into(),
                            ..Default::default()
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
                image: {
                    image: 'https://qdrant.tech/example.png',
                    model: 'jinaai/jina-clip-v2',
                    options: {
                        'jina-api-key': '<your_jinaai_api_key>',
                        dimensions: 512,
                    },
                },
                text: {
                    text: 'Mars, the red planet',
                    model: 'sentence-transformers/all-minilm-l6-v2',
                },
                bm25: {
                    text: 'Mars, the red planet',
                    model: 'Qdrant/bm25',
                },
            },
        },
    ],
});
```
