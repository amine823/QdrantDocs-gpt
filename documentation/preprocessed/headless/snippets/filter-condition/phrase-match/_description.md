This code snippet sets up a field condition to search for an exact (token) phrase within a text field. In this case, a special `phrase` match is defined with the target text being "brown fox". The behavior may vary depending on the configuration of the full-text index for the field. If there is no full-text index configured for the field, the condition will work as an exact substring match.


```csharp
using static Qdrant.Client.Grpc.Conditions;

MatchPhrase("description", "brown fox");
```


```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewMatchPhrase("description", "brown fox")
```


```java
import static io.qdrant.client.ConditionFactory.matchPhrase;

matchPhrase("description", "brown fox");
```


```json
{
  "key": "description",
  "match": {
    "phrase": "brown fox"
  }
}
```


```python
models.FieldCondition(
    key="description",
    match=models.MatchPhrase(phrase="brown fox"),
)
```


```rust
use qdrant_client::qdrant::Condition;

Condition::matches_phrase("description", "brown fox")
```


```typescript
{
    key: 'description',
    match: {phrase: 'brown fox'}
}
```
