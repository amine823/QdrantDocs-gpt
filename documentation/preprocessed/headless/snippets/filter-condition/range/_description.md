This code snippet creates a field condition for the "price" key with a specified range. The range includes values greater than or equal to 100.0 and less than or equal to 450.0.

```csharp
using static Qdrant.Client.Grpc.Conditions;

Range("price", new Qdrant.Client.Grpc.Range { Gte = 100.0, Lte = 450 });
```


```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewRange("price", &qdrant.Range{
	Gte: qdrant.PtrOf(100.0),
	Lte: qdrant.PtrOf(450.0),
})
```


```java
import static io.qdrant.client.ConditionFactory.range;

import io.qdrant.client.grpc.Common.Range;

range("price", Range.newBuilder().setGte(100.0).setLte(450).build());
```


```json
{
  "key": "price",
  "range": {
    "gt": null,
    "gte": 100.0,
    "lt": null,
    "lte": 450.0
  }
}
```


```python
models.FieldCondition(
    key="price",
    range=models.Range(
        gt=None,
        gte=100.0,
        lt=None,
        lte=450.0,
    ),
)
```


```rust
use qdrant_client::qdrant::{Condition, Range};

Condition::range(
    "price",
    Range {
        gt: None,
        gte: Some(100.0),
        lt: None,
        lte: Some(450.0),
    },
)
```


```typescript
{
    key: 'price',
    range: {
        gt: null,
        gte: 100.0,
        lt: null,
        lte: 450.0    
    }    
}
```
