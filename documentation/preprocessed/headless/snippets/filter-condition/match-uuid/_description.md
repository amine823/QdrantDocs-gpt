This code snippet demonstrates a field condition where the key is "uuid" and the value is set to a specific UUID value "f47ac10b-58cc-4372-a567-0e02b2c3d479" for matching purposes. It highlights the functionality of matching UUID values efficiently.

```csharp
using static Qdrant.Client.Grpc.Conditions;

MatchKeyword("uuid", "f47ac10b-58cc-4372-a567-0e02b2c3d479");
```


```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewMatch("uuid", "f47ac10b-58cc-4372-a567-0e02b2c3d479")
```


```java
import static io.qdrant.client.ConditionFactory.matchKeyword;

matchKeyword("uuid", "f47ac10b-58cc-4372-a567-0e02b2c3d479");
```


```json
{
  "key": "uuid",
  "match": {
    "value": "f47ac10b-58cc-4372-a567-0e02b2c3d479"
  }
}
```


```python
models.FieldCondition(
    key="uuid",
    match=models.MatchValue(value="f47ac10b-58cc-4372-a567-0e02b2c3d479"),
)
```


```rust
Condition::matches("uuid", "f47ac10b-58cc-4372-a567-0e02b2c3d479".to_string())
```


```typescript
{
    key: 'uuid',
    match: {value: 'f47ac10b-58cc-4372-a567-0e02b2c3d479'}    
}
```
