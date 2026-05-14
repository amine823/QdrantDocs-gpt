This code configures a new collection with 2-bit binary quantization.
2-bit binary quantization allows to improve precision of the search results at a slight cost of storage size.
There are other bit depths available: for example: `two_bits` and `one_and_half_bits`.


```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateCollectionAsync(
  collectionName: "{collection_name}",
  vectorsConfig: new VectorParams { Size = 1536, Distance = Distance.Cosine },
  quantizationConfig: new QuantizationConfig
  {
    Binary = new BinaryQuantization {
      Encoding = BinaryQuantizationEncoding.TwoBits,
      AlwaysRam = true
    }
  }
);
```


```go
import (
    "context"

    "github.com/qdrant/go-client/qdrant"
)

client, err := qdrant.NewClient(&qdrant.Config{
    Host: "localhost",
    Port: 6334,
})

client.CreateCollection(context.Background(), &qdrant.CreateCollection{
    CollectionName: "{collection_name}",
    VectorsConfig: qdrant.NewVectorsConfig(&qdrant.VectorParams{
        Size:     1536,
        Distance: qdrant.Distance_Cosine,
    }),
    QuantizationConfig: qdrant.NewQuantizationBinary(
        &qdrant.BinaryQuantization{
            Encoding: qdrant.BinaryQuantizationEncoding_TwoBits.Enum(),
            AlwaysRam: qdrant.PtrOf(true),
        },
    ),
})
```


```http
PUT /collections/{collection_name}
{
    "vectors": {
      "size": 1536,
      "distance": "Cosine"
    },
    "quantization_config": {
        "binary": {
            "encoding": "two_bits",
            "always_ram": true
        }
    }
}
```


```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.BinaryQuantization;
import io.qdrant.client.grpc.Collections.BinaryQuantizationEncoding;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.QuantizationConfig;
import io.qdrant.client.grpc.Collections.VectorParams;
import io.qdrant.client.grpc.Collections.VectorsConfig;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createCollectionAsync(
        CreateCollection.newBuilder()
            .setCollectionName("{collection_name}")
            .setVectorsConfig(
                VectorsConfig.newBuilder()
                    .setParams(
                        VectorParams.newBuilder()
                            .setSize(1536)
                            .setDistance(Distance.Cosine)
                            .build())
                    .build())
            .setQuantizationConfig(
                QuantizationConfig.newBuilder()
                    .setBinary(BinaryQuantization
                        .newBuilder()
                        .setEncoding(BinaryQuantizationEncoding.TwoBits)
                        .setAlwaysRam(true)
                        .build())
                    .build())
            .build())
    .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="{collection_name}",
    vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
    quantization_config=models.BinaryQuantization(
        binary=models.BinaryQuantizationConfig(
            encoding=models.BinaryQuantizationEncoding.TWO_BITS,
            always_ram=True,
        ),
    ),
)
```


```rust
use qdrant_client::qdrant::{
    BinaryQuantizationBuilder,
    CreateCollectionBuilder,
    Distance,
    VectorParamsBuilder,
    BinaryQuantizationEncoding,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .vectors_config(VectorParamsBuilder::new(1536, Distance::Cosine))
            .quantization_config(BinaryQuantizationBuilder::new(true)
                .encoding(BinaryQuantizationEncoding::TwoBits)
            ),
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createCollection("{collection_name}", {
  vectors: {
    size: 1536,
    distance: "Cosine",
  },
  quantization_config: {
    binary: {
      encoding: "two_bits",
      always_ram: true,
    },
  },
});
```
