This code snippet connects to Qdrant Cloud with Cloud Inference enabled. This is done by setting `cloud_inference` to `True` in the initializer of the `QdrantClient` class.

```csharp
using Qdrant.Client;

var client = new QdrantClient(
  host: "xyz-example.cloud-region.cloud-provider.cloud.qdrant.io",
  https: true,
  apiKey: "<paste-your-api-key-here>"
);
```


```go
import "github.com/qdrant/go-client/qdrant"

client, err := qdrant.NewClient(&qdrant.Config{
	Host:   "xyz-example.cloud-region.cloud-provider.cloud.qdrant.io",
	Port:   6334,
	APIKey: "<paste-your-api-key-here>",
	UseTLS: true,
})
```


```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
      new QdrantClient(
        QdrantGrpcClient.newBuilder("xyz-example.qdrant.io", 6334, true)
        .withApiKey("<paste-your-api-key-here>")
        .build());
```


```python
from qdrant_client import QdrantClient

client = QdrantClient(
    "xyz-example.cloud-region.cloud-provider.cloud.qdrant.io",
    api_key="<paste-your-api-key-here>",
    cloud_inference=True,
    timeout=30,
)
```


```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("https://xyz-example.qdrant.io:6334")
    .api_key("<paste-your-api-key-here>")
    .build()
    .unwrap();
```


```typescript
import {QdrantClient} from "@qdrant/js-client-rest";

const client = new QdrantClient({
    url: 'https://xyz-example.qdrant.io:6333',
    apiKey: '<paste-your-api-key-here>',
});
```
