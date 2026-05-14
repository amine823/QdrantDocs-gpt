This code defines a filter condition based on a geo bounding box for a location field. The bounding box is specified by its top-left and bottom-right coordinates on a map.

```csharp
using static Qdrant.Client.Grpc.Conditions;

GeoBoundingBox("location", 52.520711, 13.403683, 52.495862, 13.455868);
```


```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewGeoBoundingBox("location", 52.520711, 13.403683, 52.495862, 13.455868)
```


```java
import static io.qdrant.client.ConditionFactory.geoBoundingBox;

geoBoundingBox("location", 52.520711, 13.403683, 52.495862, 13.455868);
```


```json
{
  "key": "location",
  "geo_bounding_box": {
    "bottom_right": {
      "lon": 13.455868,
      "lat": 52.495862
    },
    "top_left": {
      "lon": 13.403683,
      "lat": 52.520711
    }
  }
}
```


```python
models.FieldCondition(
    key="location",
    geo_bounding_box=models.GeoBoundingBox(
        bottom_right=models.GeoPoint(
            lon=13.455868,
            lat=52.495862,
        ),
        top_left=models.GeoPoint(
            lon=13.403683,
            lat=52.520711,
        ),
    ),
)
```


```rust
use qdrant_client::qdrant::{Condition, GeoBoundingBox, GeoPoint};

Condition::geo_bounding_box(
    "location",
    GeoBoundingBox {
        bottom_right: Some(GeoPoint {
            lon: 13.455868,
            lat: 52.495862,
        }),
        top_left: Some(GeoPoint {
            lon: 13.403683,
            lat: 52.520711,
        }),
    },
)
```


```typescript
{
    key: 'location',
    geo_bounding_box: {
        bottom_right: {
            lon: 13.455868,
            lat: 52.495862
        },
        top_left: {
            lon: 13.403683,
            lat: 52.520711
        }
    }
}
```
