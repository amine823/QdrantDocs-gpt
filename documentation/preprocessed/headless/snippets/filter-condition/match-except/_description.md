This code snippet uses a `FieldCondition` with a `MatchExcept` condition for the key "color". It specifies that the condition should match values except "black" and "yellow". This is useful when you want to ensure that the stored value is not one of the specified values.

```csharp
using static Qdrant.Client.Grpc.Conditions;

Match("color", ["black", "yellow"]);
```


```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewMatchExcept("color", "black", "yellow")
```


```java
import static io.qdrant.client.ConditionFactory.matchExceptKeywords;

import java.util.List;

matchExceptKeywords("color", List.of("black", "yellow"));
```


```json
{
  "key": "color",
  "match": {
    "except": ["black", "yellow"]
  }
}
```


```python
models.FieldCondition(
    key="color",
    match=models.MatchExcept(**{"except": ["black", "yellow"]}),
)
```


```rust
use qdrant_client::qdrant::r#match::MatchValue;

Condition::matches(
    "color",
    !MatchValue::from(vec!["black".to_string(), "yellow".to_string()]),
)
```


```typescript
{
    key: 'color',
    match: {except: ['black', 'yellow']}
}
```
