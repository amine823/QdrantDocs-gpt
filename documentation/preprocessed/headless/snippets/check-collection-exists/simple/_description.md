This code snippet demonstrates a feature to check if a collection exists by making a GET request to a specified endpoint that includes the collection name. This functionality is available starting from version 1.8.0.

```bash
curl -X GET http://localhost:6333/collections/{collection_name}/exists
```


```csharp
await client.CollectionExistsAsync("{collection_name}");
```


```go
import "context"

client.CollectionExists(context.Background(), "my_collection")
```


```http
GET http://localhost:6333/collections/{collection_name}/exists
```


```java
client.collectionExistsAsync("{collection_name}").get();
```


```python
client.collection_exists(collection_name="{collection_name}")
```


```rust
client.collection_exists("{collection_name}").await?;
```


```typescript
client.collectionExists("{collection_name}");
```
