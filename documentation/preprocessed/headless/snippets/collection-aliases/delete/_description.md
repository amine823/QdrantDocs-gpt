This code snippet is aiming to perform an action of removing an alias named "production_collection" within a collection alias in a system.

```bash
curl -X POST http://localhost:6333/collections/aliases \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "actions": [
        {
            "delete_alias": {
                "alias_name": "production_collection"
            }
        }
    ]
}'
```


```csharp
await client.DeleteAliasAsync("production_collection");
```


```go
import "context"

client.DeleteAlias(context.Background(), "production_collection")
```


```http
POST /collections/aliases
{
    "actions": [
        {
            "delete_alias": {
                "alias_name": "production_collection"
            }
        }
    ]
}
```


```java
client.deleteAliasAsync("production_collection").get();
```


```python
client.update_collection_aliases(
    change_aliases_operations=[
        models.DeleteAliasOperation(
            delete_alias=models.DeleteAlias(alias_name="production_collection")
        ),
    ]
)
```


```rust
client.delete_alias("production_collection").await?;
```


```typescript
client.updateCollectionAliases({
  actions: [
    {
      delete_alias: {
        alias_name: "production_collection",
      },
    },
  ],
});
```
