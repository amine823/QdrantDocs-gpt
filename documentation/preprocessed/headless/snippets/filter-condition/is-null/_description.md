This code snippet defines an `IsNullCondition` to check if a specified field (`reports`) is NULL in a dataset. This condition is used to test for `NULL` values instead of using the `match` condition.

```csharp
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

IsNull("reports");
```


```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewIsNull("reports")
```


```java
import static io.qdrant.client.ConditionFactory.isNull;

isNull("reports");
```


```json
{
    "is_null": {
        "key": "reports"
    }
}
```


```python
models.IsNullCondition(
    is_null=models.PayloadField(key="reports"),
)
```


```rust
use qdrant_client::qdrant::Condition;

Condition::is_null("reports")
```


```typescript
{
  is_null: {
    key: "reports"
  }
}
```
