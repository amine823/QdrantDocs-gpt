This code snippet demonstrates how to use cloud inference in Qdrant Cloud to automatically create vector embeddings from text documents during upsert and query operations. In this example we create a new point with a new vector, generated in Qdrant Cloud.

The `Document` object contains the text which will be used as an input for inference model. The model which should be used for inference is defined in the `model` parameter.

After the point is inserted it becomes searchable. The snippet contains an example of search query request, that uses Qdrant Cloud inferene. The `Document` object is used to create the query vector with the configured inference `model`. 


```bash
# Create a new vector
curl -X PUT "https://xyz-example.qdrant.io:6333/collections/<your-collection>/points?wait=true" \
  -H "Content-Type: application/json" \
  -H "api-key: <paste-your-api-key-here>" \
  -d '{
    "points": [
      {
        "id": 1,
        "payload": { "topic": "cooking", "type": "dessert" },
        "vector": {
          "text": "Recipe for baking chocolate chip cookies",
          "model": "<the-model-to-use>"
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
      "text": "How to bake cookies?",
      "model": "<the-model-to-use>"
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
        Vectors = new Document() {
          Text = "Recipe for baking chocolate chip cookies",
          Model = "<the-model-to-use>",
        },
        Payload = {
          ["topic"] = "cooking",
          ["type"] = "dessert"
        },
    },
  }
);

var points = await client.QueryAsync(
  collectionName: "<your-collection>",
  query: new Document() {
    Text = "How to bake cookies?",
    Model = "<the-model-to-use>"
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
                Vectors: qdrant.NewVectorsDocument(&qdrant.Document{
                    Text:  "Recipe for baking chocolate chip cookies",
                    Model: "<the-model-to-use>",
                }),
                Payload: qdrant.NewValueMap(map[string]any{
                    "topic": "cooking",
                    "type":  "dessert",
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
                Text:  "How to bake cookies?",
                Model: "<the-model-to-use>",
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
      "payload": { "topic": "cooking", "type": "dessert" },
      "vector": {
        "text": "Recipe for baking chocolate chip cookies",
        "model": "<the-model-to-use>"
      }
    }
  ]
}

# Search in the collection using cloud-side inference
POST /collections/<your-collection>/points/query
{
  "query": {
    "text": "How to bake cookies?",
    "model": "<the-model-to-use>"
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
              Document.newBuilder()
              .setText("Recipe for baking chocolate chip cookies")
              .setModel("<the-model-to-use>")
              .build()))
          .putAllPayload(Map.of("topic", value("cooking"), "type", value("dessert")))
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
            .setText("How to bake cookies?")
            .setModel("<the-model-to-use>")
            .build()))
        .build())
      .get();

    System.out.printf(points.toString());
  }
}
```


```python
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Document

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
        payload={"topic": "cooking", "type": "dessert"},
        vector=Document(
            text="Recipe for baking chocolate chip cookies",
            model="<the-model-to-use>"
        )
    )
]

client.upsert(collection_name="<your-collection>", points=points)

result = client.query_points(
    collection_name="<your-collection>",
    query=Document(
        text="How to bake cookies?",
        model="<the-model-to-use>"
    )
)

print(result)
```


```rust
use qdrant_client::qdrant::Query;
use qdrant_client::qdrant::QueryPointsBuilder;
use qdrant_client::Payload;
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{Document};
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
            Document::new(
                "Recipe for baking chocolate chip cookies",
                "<the-model-to-use>"
            ),
            Payload::try_from(serde_json::json!(
                {"topic": "cooking", "type": "dessert"}
            )).unwrap(),
        )
    ];

    let upsert_request = UpsertPointsBuilder::new(
        "<your-collection>",
        points
    ).wait(true);

    let _ = client.upsert_points(upsert_request).await;

    let query_document = Document::new(
        "How to bake cookies?",
        "<the-model-to-use>"
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
    payload: { topic: "cooking", type: "dessert" },
    vector: {
        text: "Recipe for baking chocolate chip cookies",
        model: "<the-model-to-use>"
      }
  }
];

await client.upsert("<your-collection>", { wait: true, points });

const result = await client.query(
    "<your-collection>",
    {
      query: {
          text: "How to bake cookies?",
          model: "<the-model-to-use>"
      },
    }
)

console.log(result);
```
