This code represents a filtering condition where records can be checked for a specific field (in this case, "reports") if it is empty. This can help in filtering out records based on the absence of a value in the specified field.

```csharp
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

IsEmpty("reports");
```


```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewIsEmpty("reports")
```


```java
import static io.qdrant.client.ConditionFactory.isEmpty;

isEmpty("reports");
```


```json
{
  "is_empty": {
    "key": "reports"
  }
}
```


```python
models.IsEmptyCondition(
    is_empty=models.PayloadField(key="reports"),
)
```


```rust
use qdrant_client::qdrant::Condition;

Condition::is_empty("reports")
```


```typescript
{
  is_empty: {
    key: "reports"
  }
}
```
