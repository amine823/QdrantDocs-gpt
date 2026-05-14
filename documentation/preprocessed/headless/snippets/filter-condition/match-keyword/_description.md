This code snippet sets a filter condition to match records where the key is "color" and the value is "red".

```csharp
using static Qdrant.Client.Grpc.Conditions;

MatchKeyword("color", "red");
```


```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewMatch("color", "red")
```


```java
import static io.qdrant.client.ConditionFactory.matchKeyword;

matchKeyword("color", "red");
```


```json
{
  "key": "color",
  "match": {
    "value": "red"
  }
}
```


```python
models.FieldCondition(
    key="color",
    match=models.MatchValue(value="red"),
)
```


```rust
Condition::matches("color", "red".to_string())
```


```typescript
{
    key: 'color', 
    match: {value: 'red'}
}
```
