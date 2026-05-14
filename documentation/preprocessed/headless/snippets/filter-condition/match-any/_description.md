This code snippet demonstrates the use of the Match Any condition in a field filter. In this case, it checks if the value stored in the "color" field is either "black" or "yellow". The Match Any condition functions as a logical OR operation for the specified values, akin to the `IN` operator in databases.

```csharp
using static Qdrant.Client.Grpc.Conditions;

Match("color", ["black", "yellow"]);
```


```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewMatchKeywords("color", "black", "yellow")
```


```java
import static io.qdrant.client.ConditionFactory.matchKeywords;

import java.util.List;

matchKeywords("color", List.of("black", "yellow"));
```


```json
{
  "key": "color",
  "match": {
    "any": ["black", "yellow"]
  }
}
```


```python
models.FieldCondition(
    key="color",
    match=models.MatchAny(any=["black", "yellow"]),
)
```


```rust
Condition::matches("color", vec!["black".to_string(), "yellow".to_string()])
```


```typescript
{
    key: 'color',
    match: {any: ['black', 'yellow']}    
}
```
