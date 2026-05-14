This code snippet demonstrates how to use the Cohere API for ingest-time inference on Qdrant Cloud. The example upserts a point, but instead of providing an explicit vector, the request includes text along with the name of a Cohere model. When the model name is prepended with `cohere/`, the Qdrant Cloud Inference proxy uses the Cohere API to infer embeddings out of the provided text. Qdrant will store the resulting vector. The request also shows how to pass Cohere-specific parameters to the API. In this case, the request provides the Cohere API key and the `output_dimension` parameter.

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
            Vectors = new Image()
            {
                Model = "cohere/embed-v4.0",
                Image_ =
                    "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC",
                Options =
                {
                    ["cohere-api-key"] = "<YOUR_COHERE_API_KEY>",
                    ["output_dimension"] = 512,
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
			Vectors: qdrant.NewVectorsImage(&qdrant.Image{
				Model: "cohere/embed-v4.0",
				Image: qdrant.NewValueString("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC"),
				Options: qdrant.NewValueMap(map[string]any{
					"cohere-api-key":   "<YOUR_COHERE_API_KEY>",
					"output_dimension": 512,
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
        "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC",
        "model": "cohere/embed-v4.0",
        "options": {
          "cohere-api-key": "<YOUR_COHERE_API_KEY>",
          "output_dimension": 512
        }
      }
    }
  ]
}
```

```java
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ValueFactory.value;
import static io.qdrant.client.VectorsFactory.vectors;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
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
                    vectors(
                        Image.newBuilder()
                            .setModel("cohere/embed-v4.0")
                            .setImage(
                                value(
                                    "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC"))
                            .putAllOptions(
                                Map.of(
                                    "cohere-api-key",
                                    value("<YOUR_COHERE_API_KEY>"),
                                    "output_dimension",
                                    value(512)))
                            .build()))
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
            vector=models.Document(
                text="a green square",
                model="cohere/embed-v4.0",
                options={
                    "cohere-api-key": "<your_cohere_api_key>",
                    "output_dimension": 512
                }
            )
        )
    ]
)
```


```rust
use qdrant_client::{
    Payload, Qdrant,
    qdrant::{Document, PointStruct, UpsertPointsBuilder},
};
use std::collections::HashMap;

let client = Qdrant::from_url("<your-qdrant-url>").build()?;
let mut options = HashMap::new();
options.insert("cohere-api-key".to_string(), "<YOUR_COHERE_API_KEY>".into());
options.insert("output_dimension".to_string(), 512.into());

client
    .upsert_points(UpsertPointsBuilder::new("{collection_name}",
        vec![
            PointStruct::new(1,
                Document {
                  text: "Recipe for baking chocolate chip cookies requires flour, sugar, eggs, and chocolate chips.".into(),
                  model: "openai/text-embedding-3-small".into(),
                  options,
                  },
                Payload::default())
            ]).wait(true))
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
                text: 'a green square',
                model: 'cohere/embed-v4.0',
                options: {
                    'cohere-api-key': '<your_cohere_api_key>',
                    output_dimension: 512,
                },
            },
        },
    ],
});
```
