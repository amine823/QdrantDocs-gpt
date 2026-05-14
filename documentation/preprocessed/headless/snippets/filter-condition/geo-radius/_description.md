This code snippet sets a filter condition based on a geographical radius. It specifies the center point with latitude and longitude coordinates, and sets a radius of 1000 meters from that center point.

```csharp
using static Qdrant.Client.Grpc.Conditions;

GeoRadius("location", 52.520711, 13.403683, 1000.0f);
```


```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewGeoRadius("location", 52.520711, 13.403683, 1000.0)
```


```java
import static io.qdrant.client.ConditionFactory.geoRadius;

geoRadius("location", 52.520711, 13.403683, 1000.0f);
```


```json
{
  "key": "location",
  "geo_radius": {
    "center": {
      "lon": 13.403683,
      "lat": 52.520711
    },
    "radius": 1000.0
  }
}
```


```python
models.FieldCondition(
    key="location",
    geo_radius=models.GeoRadius(
        center=models.GeoPoint(
            lon=13.403683,
            lat=52.520711,
        ),
        radius=1000.0,
    ),
)
```


```rust
use qdrant_client::qdrant::{Condition, GeoPoint, GeoRadius};

Condition::geo_radius(
    "location",
    GeoRadius {
        center: Some(GeoPoint {
            lon: 13.403683,
            lat: 52.520711,
        }),
        radius: 1000.0,
    },
)
```


```typescript
{
    key: 'location',
    geo_radius: {
        center: {
            lon: 13.403683,
            lat: 52.520711
        },
        radius: 1000.0
    }    
}
```
