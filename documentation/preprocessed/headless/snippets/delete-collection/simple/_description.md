This code snippet is for deleting a collection.

```bash
curl -X DELETE http://localhost:6333/collections/{collection_name}
```


```csharp
await client.DeleteCollectionAsync("{collection_name}");
```


```go
import "context"

client.DeleteCollection(context.Background(), "{collection_name}")
```


```http
DELETE http://localhost:6333/collections/{collection_name}
```


```java
client.deleteCollectionAsync("{collection_name}").get();
```


```python
client.delete_collection(collection_name="{collection_name}")
```


```rust
client.delete_collection("{collection_name}").await?;
```


```typescript
client.deleteCollection("{collection_name}");
```
