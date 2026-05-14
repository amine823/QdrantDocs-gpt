This code defines a filter condition for a field named "comments" where the search will only consider items with more than two comments.

```csharp
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

ValuesCount("comments", new ValuesCount { Gt = 2 });
```


```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewValuesCount("comments", &qdrant.ValuesCount{
	Gt: qdrant.PtrOf(uint64(2)),
})
```


```java
import static io.qdrant.client.ConditionFactory.valuesCount;

import io.qdrant.client.grpc.Common.ValuesCount;

valuesCount("comments", ValuesCount.newBuilder().setGt(2).build());
```


```json
{
  "key": "comments",
  "values_count": {
    "gt": 2
  }
}
```


```python
models.FieldCondition(
    key="comments",
    values_count=models.ValuesCount(gt=2),
)
```


```rust
use qdrant_client::qdrant::{Condition, ValuesCount};

Condition::values_count(
    "comments",
    ValuesCount {
        gt: Some(2),
        ..Default::default()
    },
)
```


```typescript
{
    key: 'comments',
    values_count: {gt: 2}    
}
```
