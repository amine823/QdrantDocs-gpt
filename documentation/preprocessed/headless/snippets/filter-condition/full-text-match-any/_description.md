This code snippet sets up a field condition to search for one or more query terms within a text field. In this case, a special `text_any` match is defined with the target text being "good cheap". A text field is considered a match if it contains any of the search terms. The behavior may vary depending on the configuration of the full-text index for the field. If there is no full-text index configured for the field, the condition will work as an exact substring match.

```csharp
using static Qdrant.Client.Grpc.Conditions;

MatchTextAny("description", "good cheap");
```


```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewMatchTextAny("description", "good cheap")
```


```java
import static io.qdrant.client.ConditionFactory.matchTextAny;

matchTextAny("description", "good cheap");
```


```json
{
  "key": "description",
  "match": {
    "text_any": "good cheap"
  }
}
```


```python
models.FieldCondition(
    key="description",
    match=models.MatchTextAny(text_any="good cheap"),
)
```


```rust
use qdrant_client::qdrant::Condition;

Condition::matches_text_any("description", "good cheap")
```


```typescript
{
    key: 'description',
    match: {text_any: 'good cheap'}    
}
```
