This code snippet showcases a feature where you can retrieve information about an existing collection in order to understand how the points are distributed and indexed within it.

```bash
curl -X GET http://localhost:6333/collections/{collection_name}
```


```csharp
await client.GetCollectionInfoAsync("{collection_name}");
```


```go
import "context"

client.GetCollectionInfo(context.Background(), "{collection_name}")
```


```http
GET /collections/{collection_name}
```


```java
client.getCollectionInfoAsync("{collection_name}").get();
```


```python
client.get_collection(collection_name="{collection_name}")
```


```rust
client.collection_info("{collection_name}").await?;
```


```typescript
client.getCollection("{collection_name}");
```
