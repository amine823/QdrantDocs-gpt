This code snippet defines a field condition specifying that the key is "count" and the matching value for the field is set to 0.

```csharp
using static Qdrant.Client.Grpc.Conditions;

Match("count", 0);
```


```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewMatchInt("count", 0)
```


```java
import static io.qdrant.client.ConditionFactory.match;

match("count", 0);
```


```json
{
  "key": "count",
  "match": {
    "value": 0
  }
}
```


```python
models.FieldCondition(
    key="count",
    match=models.MatchValue(value=0),
)
```


```rust
Condition::matches("count", 0)
```


```typescript
{
    key: 'count',
    match: {value: 0}    
}
```
