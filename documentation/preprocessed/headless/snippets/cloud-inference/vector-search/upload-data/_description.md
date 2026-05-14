This code snipet shows how to load a dataset and upload dense and sparse vectors to Qdrant. While uploading the vectors we also include a payload known as text. 

```csharp
var denseModel = "sentence-transformers/all-minilm-l6-v2";
var bm25Model = "qdrant/bm25";
// NOTE: LoadDataset is a user-defined function.
// Implement it to handle dataset loading as needed.
var dataset = LoadDataset("miriad/miriad-4.4M", "train[0:100]");
var points = new List<PointStruct>();

foreach (var item in dataset)
{
    var passage = item["passage_text"].ToString();

    var point = new PointStruct
    {
        Id = Guid.NewGuid(),
        Vectors = new Dictionary<string, Vector>
        {
            ["dense_vector"] = new Document
            {
                Text = passage,
                Model = denseModel
            },
            ["bm25_sparse_vector"] = new Document
            {
                Text = passage,
                Model = bm25Model
            }
        },
    };

    points.Add(point);
}

await client.UpsertAsync(
    collectionName: "{collectionName}",
    points: points
);
```


```go
denseModel := "sentence-transformers/all-minilm-l6-v2"
bm25Model := "qdrant/bm25"
// NOTE: loadDataset is a user-defined function.
// Implement it to handle dataset loading as needed.
dataset := loadDataset("miriad/miriad-4.4M", "train[0:100]")
points := make([]*qdrant.PointStruct, 0, 100)

for _, item := range dataset {
	passage := item["passage_text"]
	point := &qdrant.PointStruct{
		Id: qdrant.NewID(uuid.New().String()),
		Vectors: qdrant.NewVectorsMap(map[string]*qdrant.Vector{
			"dense_vector": qdrant.NewVectorDocument(&qdrant.Document{
				Text:  passage,
				Model: denseModel,
			}),
			"bm25_sparse_vector": qdrant.NewVectorDocument(&qdrant.Document{
				Text:  passage,
				Model: bm25Model,
			}),
		}),
	}
	points = append(points, point)
}
_, err = client.Upsert(context.Background(), &qdrant.UpsertPoints{
	CollectionName: "{collection_name}",
	Points:         points,
})
```


```java
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.VectorFactory.vector;
import static io.qdrant.client.VectorsFactory.namedVectors;

import io.qdrant.client.grpc.Points.Document;
import io.qdrant.client.grpc.Points.PointStruct;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.UUID;

String denseModel = "sentence-transformers/all-minilm-l6-v2";
String bm25Model = "qdrant/bm25";
// NOTE: loadDataset is a user-defined function.
// Implement it to handle dataset loading as needed.
List<Map<String, String>> dataset = loadDataset("miriad/miriad-4.4M", "train[0:100]");
List<PointStruct> points = new ArrayList<>();

for (Map<String, String> item : dataset) {
  String passage = item.get("passage_text");
  PointStruct point =
      PointStruct.newBuilder()
          .setId(id(UUID.randomUUID()))
          .setVectors(
              namedVectors(
                  Map.of(
                      "dense_vector",
                      vector(
                          Document.newBuilder().setText(passage).setModel(denseModel).build()),
                      "bm25_sparse_vector",
                      vector(
                          Document.newBuilder().setText(passage).setModel(bm25Model).build()))))
          .build();
  points.add(point);
}

client.upsertAsync("{collection_name}", points).get();
```


```python
from qdrant_client.http.models import PointStruct, Document
from datasets import load_dataset
import uuid

dense_model = "sentence-transformers/all-minilm-l6-v2"

bm25_model = "qdrant/bm25"

ds = load_dataset("miriad/miriad-4.4M", split="train[0:100]")

points = []

for idx, item in enumerate(ds):
    passage = item["passage_text"]
    
    point = PointStruct(
        id=uuid.uuid4().hex,  # use unique string ID
        payload=item,
        vector={
            "dense_vector": Document(
                text=passage,
                model=dense_model
            ),
            "bm25_sparse_vector": Document(
                text=passage,
                model=bm25_model
            )
        }
    )
    points.append(point)

client.upload_points(
    collection_name="{collection_name}", 
    points=points, 
    batch_size=8
)
```


```rust
use qdrant_client::qdrant::{
    Document, NamedVectors, PointStruct, UpsertPointsBuilder,
};
use qdrant_client::Payload;
use uuid::Uuid;

let dense_model = "sentence-transformers/all-minilm-l6-v2";
let bm25_model = "qdrant/bm25";
// NOTE: load_dataset is a user-defined function.
// Implement it to handle dataset loading as needed.
let dataset: Vec<_> = load_dataset("miriad/miriad-4.4M", "train[0:100]");

let points: Vec<PointStruct> = dataset
    .iter()
    .map(|item| {
        let passage = item["passage_text"].as_str().unwrap();
        let vectors = NamedVectors::default()
            .add_vector(
                "dense_vector",
                Document::new(passage, dense_model),
            )
            .add_vector(
                "bm25_sparse_vector",
                Document::new(passage, bm25_model),
            );
        let payload = Payload::try_from(item.clone()).unwrap();
        PointStruct::new(Uuid::new_v4().to_string(), vectors, payload)
    })
    .collect();

client
    .upsert_points(UpsertPointsBuilder::new("{collection_name}", points))
    .await?;
```


```typescript
import { randomUUID } from "crypto";

const denseModel = "sentence-transformers/all-minilm-l6-v2";
const bm25Model = "qdrant/bm25";
// NOTE: loadDataset is a user-defined function.
// Implement it to handle dataset loading as needed.
const dataset = loadDataset("miriad/miriad-4.4M", "train[0:100]");

const points = dataset.map((item) => {
  const passage = item.passage_text;

  return {
    id: randomUUID().toString(),
    vector: {
      dense_vector: {
        text: passage,
        model: denseModel,
      },
      bm25_sparse_vector: {
        text: passage,
        model: bm25Model,
      },
    },
  };
});

await client.upsert("{collection_name}", { points });
```
