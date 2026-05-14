This code snippet sets up a field condition to search for multiple query terms within a text field. In this case, a special `text` match is defined with the target text being "good cheap". A text field is only considered a match if it contains all of the search terms. The behavior may vary depending on the configuration of the full-text index for the field. If there is no full-text index configured for the field, the condition will work as an exact substring match.

```csharp
using static Qdrant.Client.Grpc.Conditions;

MatchText("description", "good cheap");
```


```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewMatchText("description", "good cheap")
```


```java
import static io.qdrant.client.ConditionFactory.matchText;

matchText("description", "good cheap");
```


```json
{
  "key": "description",
  "match": {
    "text": "good cheap"
  }
}
```


```python
models.FieldCondition(
    key="description",
    match=models.MatchText(text="good cheap"),
)
```


```rust
use qdrant_client::qdrant::Condition;

Condition::matches_text("description", "good cheap")
```


```typescript
{
    key: 'description',
    match: {text: 'good cheap'}    
}
```
