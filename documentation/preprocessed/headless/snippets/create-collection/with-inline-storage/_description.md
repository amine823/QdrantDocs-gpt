When creating a collection with inline storage enabled, the HNSW index stores copies of both the original vectors and quantized vectors within the index file itself.
This reduces random disk seeks during search, trading disk space for improved search speed.
The `inline_storage` option requires quantization to be enabled and does not support multi-vectors.
Set `hnsw_config.inline_storage` to `true` and configure quantization to use this feature.


```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateCollectionAsync(
	collectionName: "{collection_name}",
	vectorsConfig: new VectorParams { Size = 768, Distance = Distance.Cosine, OnDisk = true },
	quantizationConfig: new QuantizationConfig
	{
		Binary = new BinaryQuantization { AlwaysRam = false }
	},
	hnswConfig: new HnswConfigDiff { OnDisk = true, InlineStorage = true }
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
		Size:     768,
		Distance: qdrant.Distance_Cosine,
		OnDisk:   qdrant.PtrOf(true),
	}),
	QuantizationConfig: qdrant.NewQuantizationBinary(
		&qdrant.BinaryQuantization{
			AlwaysRam: qdrant.PtrOf(false),
		},
	),
	HnswConfig: &qdrant.HnswConfigDiff{
		OnDisk:        qdrant.PtrOf(true),
		InlineStorage: qdrant.PtrOf(true),
	},
})
```


```http
PUT /collections/{collection_name}
{
    "vectors": {
      "size": 768,
      "distance": "Cosine",
      "on_disk": true
    },
    "quantization_config": {
        "binary": {
            "always_ram": false
        }
    },
    "hnsw_config": {
        "on_disk": true,
        "inline_storage": true
    }
}
```


```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.BinaryQuantization;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.HnswConfigDiff;
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
                            .setSize(768)
                            .setDistance(Distance.Cosine)
                            .setOnDisk(true)
                            .build())
                    .build())
            .setQuantizationConfig(
                QuantizationConfig.newBuilder()
                    .setBinary(BinaryQuantization.newBuilder().setAlwaysRam(false).build())
                    .build())
            .setHnswConfig(HnswConfigDiff.newBuilder().setOnDisk(true).setInlineStorage(true).build())
            .build())
    .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="{collection_name}",
    vectors_config=models.VectorParams(
        size=768, distance=models.Distance.COSINE, on_disk=True
    ),
    quantization_config=models.BinaryQuantization(
        binary=models.BinaryQuantizationConfig(always_ram=False),
    ),
    hnsw_config=models.HnswConfigDiff(on_disk=True, inline_storage=True),
)
```


```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{
    BinaryQuantizationBuilder, CreateCollectionBuilder, Distance, HnswConfigDiffBuilder,
    VectorParamsBuilder,
};

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .vectors_config(VectorParamsBuilder::new(768, Distance::Cosine).on_disk(true))
            .quantization_config(BinaryQuantizationBuilder::new(false))
            .hnsw_config(
                HnswConfigDiffBuilder::default()
                    .on_disk(true)
                    .inline_storage(true),
            ),
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createCollection("{collection_name}", {
  vectors: {
    size: 768,
    distance: "Cosine",
    on_disk: true,
  },
  quantization_config: {
    binary: {
      always_ram: false,
    },
  },
  hnsw_config: {
    on_disk: true,
    inline_storage: true,
  },
});
```
