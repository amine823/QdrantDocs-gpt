This code snippet demonstrates how to utilize the `order_by` key parameter to define the sorting criteria. Additionally, it showcases the inclusion of supplementary fields like `direction` to specify the sorting order and `start_from` to set a specific starting point for ordering.

```csharp
using Qdrant.Client.Grpc;

new OrderBy
{
 Key = "timestamp",
 Direction = Direction.Desc,
 StartFrom = 123
};
```


```go
import "github.com/qdrant/go-client/qdrant"

qdrant.OrderBy{
	Key:       "timestamp",
	Direction: qdrant.Direction_Desc.Enum(),
	StartFrom: qdrant.NewStartFromInt(123),
}
```


```http
"order_by": {
    "key": "timestamp",
    "direction": "desc" // default is "asc"
    "start_from": 123, // start from this value
}
```


```java
import io.qdrant.client.grpc.Points.Direction;
import io.qdrant.client.grpc.Points.OrderBy;
import io.qdrant.client.grpc.Points.StartFrom;

OrderBy.newBuilder()
  .setKey("timestamp")
  .setDirection(Direction.Desc)
  .setStartFrom(StartFrom.newBuilder()
    .setInteger(123)
    .build())
  .build();
```


```python
order_by=models.OrderBy(
    key="timestamp",
    direction=models.Direction.DESC,  # default is "ASC"
    start_from=123,  # start from this value
)
```


```rust
use qdrant_client::qdrant::{start_from::Value, Direction, OrderByBuilder};

OrderByBuilder::new("timestamp")
    .direction(Direction::Desc.into())
    .start_from(Value::Integer(123))
    .build();
```


```typescript
order_by: {
    key: "timestamp",
    direction: "desc", // default is "asc"
    start_from: 123, // start from this value
}
```
