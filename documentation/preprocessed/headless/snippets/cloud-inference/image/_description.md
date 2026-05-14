This code snippet shows how to use Qdrant Cloud Inference to automatically generate vector embeddings from images and text during upsert and search operations. 

In this example, a new point is inserted with an image URL and a specified model. The vector embedding is generated on the Qdrant Cloud side using the provided model. The `image` and `model` fields specify the image to embed and the model to use.

After the point is inserted, it becomes searchable. The snippet also demonstrates how to perform a search query using Qdrant Cloud Inference. A `text` and `model` are provided, and Qdrant Cloud generates the query vector automatically. This allows you to search your collection using natural language queries without manually generating embeddings.

This example demonstrates multimodal search using the `CLIP` model and Qdrant Cloud Inference.

```bash
# Create a new vector
curl -X PUT "https://xyz-example.qdrant.io:6333/collections/<your-collection>/points?wait=true" \
  -H "Content-Type: application/json" \
  -H "api-key: <paste-your-api-key-here>" \
  -d '{
    "points": [
      {
        "id": 1,
        "vector": {
          "image": "https://qdrant.tech/example.png",
          "model": "qdrant/clip-vit-b-32-vision"
        },
        "payload": {
          "title": "Example Image"
        }
      }
    ]
  }'

# Perform a search query
curl -X POST "https://xyz-example.qdrant.io:6333/collections/<your-collection>/points/query" \
  -H "Content-Type: application/json" \
  -H "api-key: <paste-your-api-key-here>" \
  -d '{
    "query": {
      "text": "Mission to Mars",
      "model": "qdrant/clip-vit-b-32-text"
    }
  }'
```


```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using Value = Qdrant.Client.Grpc.Value;

var client = new QdrantClient(
  host: "xyz-example.qdrant.io",
  port: 6334,
  https: true,
  apiKey: "<paste-your-api-key-here>"
);

await client.UpsertAsync(
  collectionName: "<your-collection>",
  points: new List <PointStruct> {
    new() {
      Id = 1,
        Vectors = new Image() {
          Image_ = "https://qdrant.tech/example.png",
          Model = "qdrant/clip-vit-b-32-vision",
        },
        Payload = {
          ["title"] = "Example Image"
        },
    },
  }
);

var points = await client.QueryAsync(
  collectionName: "<your-collection>",
  query: new Document() {
    Text = "Mission to Mars",
    Model = "qdrant/clip-vit-b-32-text"
  }
);

foreach(var point in points) {
  Console.WriteLine(point);
}
```


```go
package main

import (
    "context"
    "log"
    "time"

    "github.com/qdrant/go-client/qdrant"
)

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), time.Second)
    defer cancel()

    client, err := qdrant.NewClient(&qdrant.Config{
        Host:   "xyz-example.qdrant.io",
        Port:   6334,
        APIKey: "<paste-your-api-key-here>",
        UseTLS: true,
    })
    if err != nil {
        log.Fatalf("did not connect: %v", err)
    }
    defer client.Close()

    _, err = client.Upsert(ctx, &qdrant.UpsertPoints{
        CollectionName: "<your-collection>",
        Points: []*qdrant.PointStruct{
            {
                Id: qdrant.NewIDNum(1),
                Vectors: qdrant.NewVectorsImage(&qdrant.Image{
                    Model: "qdrant/clip-vit-b-32-vision",
                    Image: qdrant.NewValueString("https://qdrant.tech/example.png"),
                }),
                Payload: qdrant.NewValueMap(map[string]any{
                    "title": "Example image",
                }),
            },
        },
    })
    if err != nil {
        log.Fatalf("error creating point: %v", err)
    }

    points, err := client.Query(ctx, &qdrant.QueryPoints{
        CollectionName: "<your-collection>",
        Query: qdrant.NewQueryNearest(
            qdrant.NewVectorInputDocument(&qdrant.Document{
                Text:  "Mission to Mars",
                Model: "qdrant/clip-vit-b-32-text",
            }),
        ),
    })
    log.Printf("List of points: %s", points)
}
```


```http
# Insert new points with cloud-side inference
PUT /collections/<your-collection>/points?wait=true
{
  "points": [
    {
      "id": 1,
      "vector": {
        "image": "https://qdrant.tech/example.png",
        "model": "qdrant/clip-vit-b-32-vision"
      },
      "payload": {
        "title": "Example Image"
      }
    }
  ]
}

# Search in the collection using cloud-side inference
POST /collections/<your-collection>/points/query
{
  "query": {
    "text": "Mission to Mars",
    "model": "qdrant/clip-vit-b-32-text"
  }
}
```


```java
package org.example;

import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.QueryFactory.nearest;
import static io.qdrant.client.ValueFactory.value;
import static io.qdrant.client.VectorsFactory.vectors;

import io.qdrant.client.grpc.Points;
import io.qdrant.client.grpc.Points.Document;
import io.qdrant.client.grpc.Points.Image;
import io.qdrant.client.grpc.Points.PointStruct;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ExecutionException;

public class Main {
  public static void main(String[] args)
      throws ExecutionException, InterruptedException {
    QdrantClient client =
      new QdrantClient(
        QdrantGrpcClient.newBuilder("xyz-example.qdrant.io", 6334, true)
        .withApiKey("<paste-your-api-key-here>")
        .build());

    client
      .upsertAsync(
        "<your-collection>",
        List.of(
          PointStruct.newBuilder()
          .setId(id(1))
          .setVectors(
            vectors(
              Image.newBuilder()
              .setImage(value("https://qdrant.tech/example.png"))
              .setModel("qdrant/clip-vit-b-32-vision")
              .build()))
          .putAllPayload(Map.of("title", value("Example Image")))
          .build()))
      .get();

    List <Points.ScoredPoint> points =
      client
      .queryAsync(
        Points.QueryPoints.newBuilder()
        .setCollectionName("<your-collection>")
        .setQuery(
          nearest(
            Document.newBuilder()
            .setText("Mission to Mars")
            .setModel("qdrant/clip-vit-b-32-text")
            .build()))
        .build())
      .get();

    System.out.printf(points.toString());
  }
}
```


```python
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Image, Document

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333",
    api_key="<paste-your-api-key-here>",
    # IMPORTANT
    # If not enabled, inference will be performed locally
    cloud_inference=True,
)

points = [
    PointStruct(
        id=1,
        vector=Image(
            image="https://qdrant.tech/example.png",
            model="qdrant/clip-vit-b-32-vision"
        ),
        payload={
            "title": "Example Image"
        }
    )
]

client.upsert(collection_name="<your-collection>", points=points)

result = client.query_points(
    collection_name="<your-collection>",
    query=Document(
        text="Mission to Mars",
        model="qdrant/clip-vit-b-32-text"
    )
)

print(result)
```


```rust
use qdrant_client::qdrant::Query;
use qdrant_client::qdrant::QueryPointsBuilder;
use qdrant_client::Payload;
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{Document, Image};
use qdrant_client::qdrant::{PointStruct, UpsertPointsBuilder};

#[tokio::main]
async fn main() {
    let client = Qdrant::from_url("https://xyz-example.qdrant.io:6334")
        .api_key("<paste-your-api-key-here>")
        .build()
        .unwrap();

    let points = vec![
        PointStruct::new(
            1,
            Image::new_from_url(
                "https://qdrant.tech/example.png",
                "qdrant/clip-vit-b-32-vision"
            ),
            Payload::try_from(serde_json::json!({
                "title": "Example Image"
            })).unwrap(),
        )
    ];

    let upsert_request = UpsertPointsBuilder::new(
        "<your-collection>",
        points
    ).wait(true);

    let _ = client.upsert_points(upsert_request).await;

    let query_document = Document::new(
        "Mission to Mars",
        "qdrant/clip-vit-b-32-text"
    );

    let query_request = QueryPointsBuilder::new("<your-collection>")
        .query(Query::new_nearest(query_document));

    let result = client.query(query_request).await.unwrap();
    println!("Result: {:?}", result);
}
```


```typescript
import {QdrantClient} from "@qdrant/js-client-rest";

const client = new QdrantClient({
    url: 'https://xyz-example.qdrant.io:6333',
    apiKey: '<paste-your-api-key-here>',
});

const points = [
  {
    id: 1,
    vector: {
      image: "https://qdrant.tech/example.png",
      model: "qdrant/clip-vit-b-32-vision"
    },
    payload: {
      title: "Example Image"
    }
  }
];

await client.upsert("<your-collection>", { wait: true, points });

const result = await client.query(
    "<your-collection>",
    {
      query: {
          text: "Mission to Mars",
          model: "qdrant/clip-vit-b-32-text"
      },
    }
)

console.log(result);
```
