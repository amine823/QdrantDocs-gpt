This code snippet demonstrates how to set a new value 'qux' for the nested property within the payload of a specified key named 'property1'.

```http
POST /collections/{collection_name}/points/payload
{
    "payload": {
        "nested_property": "qux",
    },
    "key": "property1",
    "points": [1]
}
```
