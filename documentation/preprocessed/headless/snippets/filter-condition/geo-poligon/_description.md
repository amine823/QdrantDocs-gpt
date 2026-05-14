This code snippet represents a geo polygon filter condition for location data. It defines an irregularly shaped area with an exterior boundary and an optional interior boundary. The exterior boundary is specified with a sequence of points, while the interior boundary is also defined with a separate sequence of points. The code uses longitude and latitude coordinates to create the geo polygon, offering a way to filter points based on their location within the specified polygon.

```csharp
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

GeoPolygon(
	field: "location",
	exterior: new GeoLineString
	{
		Points =
		{
			new GeoPoint { Lat = -70.0, Lon = -70.0 },
			new GeoPoint { Lat = 60.0, Lon = -70.0 },
			new GeoPoint { Lat = 60.0, Lon = 60.0 },
			new GeoPoint { Lat = -70.0, Lon = 60.0 },
			new GeoPoint { Lat = -70.0, Lon = -70.0 }
		}
	},
	interiors: [
		new()
		{
			Points =
			{
				new GeoPoint { Lat = -65.0, Lon = -65.0 },
				new GeoPoint { Lat = 0.0, Lon = -65.0 },
				new GeoPoint { Lat = 0.0, Lon = 0.0 },
				new GeoPoint { Lat = -65.0, Lon = 0.0 },
				new GeoPoint { Lat = -65.0, Lon = -65.0 }
			}
		}
	]
);
```


```go
import "github.com/qdrant/go-client/qdrant"

qdrant.NewGeoPolygon("location",
	&qdrant.GeoLineString{
		Points: []*qdrant.GeoPoint{
			{Lat: -70, Lon: -70},
			{Lat: 60, Lon: -70},
			{Lat: 60, Lon: 60},
			{Lat: -70, Lon: 60},
			{Lat: -70, Lon: -70},
		},
	}, &qdrant.GeoLineString{
		Points: []*qdrant.GeoPoint{
			{Lat: -65, Lon: -65},
			{Lat: 0, Lon: -65},
			{Lat: 0, Lon: 0},
			{Lat: -65, Lon: 0},
			{Lat: -65, Lon: -65},
		},
	})
```


```java
import static io.qdrant.client.ConditionFactory.geoPolygon;

import io.qdrant.client.grpc.Common.GeoLineString;
import io.qdrant.client.grpc.Common.GeoPoint;
import java.util.List;

geoPolygon(
    "location",
    GeoLineString.newBuilder()
        .addAllPoints(
            List.of(
                GeoPoint.newBuilder().setLon(-70.0).setLat(-70.0).build(),
                GeoPoint.newBuilder().setLon(60.0).setLat(-70.0).build(),
                GeoPoint.newBuilder().setLon(60.0).setLat(60.0).build(),
                GeoPoint.newBuilder().setLon(-70.0).setLat(60.0).build(),
                GeoPoint.newBuilder().setLon(-70.0).setLat(-70.0).build()))
        .build(),
    List.of(
        GeoLineString.newBuilder()
            .addAllPoints(
                List.of(
                    GeoPoint.newBuilder().setLon(-65.0).setLat(-65.0).build(),
                    GeoPoint.newBuilder().setLon(0.0).setLat(-65.0).build(),
                    GeoPoint.newBuilder().setLon(0.0).setLat(0.0).build(),
                    GeoPoint.newBuilder().setLon(-65.0).setLat(0.0).build(),
                    GeoPoint.newBuilder().setLon(-65.0).setLat(-65.0).build()))
            .build()));
```


```json

{
  "key": "location",
  "geo_polygon": {
    "exterior": {
      "points": [
        { "lon": -70.0, "lat": -70.0 },
        { "lon": 60.0, "lat": -70.0 },
        { "lon": 60.0, "lat": 60.0 },
        { "lon": -70.0, "lat": 60.0 },
        { "lon": -70.0, "lat": -70.0 }
      ]
    },
    "interiors": [
      {
        "points": [
          { "lon": -65.0, "lat": -65.0 },
          { "lon": 0.0, "lat": -65.0 },
          { "lon": 0.0, "lat": 0.0 },
          { "lon": -65.0, "lat": 0.0 },
          { "lon": -65.0, "lat": -65.0 }
        ]
      }
    ]
  }
}
```


```python
models.FieldCondition(
    key="location",
    geo_polygon=models.GeoPolygon(
        exterior=models.GeoLineString(
            points=[
                models.GeoPoint(
                    lon=-70.0,
                    lat=-70.0,
                ),
                models.GeoPoint(
                    lon=60.0,
                    lat=-70.0,
                ),
                models.GeoPoint(
                    lon=60.0,
                    lat=60.0,
                ),
                models.GeoPoint(
                    lon=-70.0,
                    lat=60.0,
                ),
                models.GeoPoint(
                    lon=-70.0,
                    lat=-70.0,
                ),
            ]
        ),
        interiors=[
            models.GeoLineString(
                points=[
                    models.GeoPoint(
                        lon=-65.0,
                        lat=-65.0,
                    ),
                    models.GeoPoint(
                        lon=0.0,
                        lat=-65.0,
                    ),
                    models.GeoPoint(
                        lon=0.0,
                        lat=0.0,
                    ),
                    models.GeoPoint(
                        lon=-65.0,
                        lat=0.0,
                    ),
                    models.GeoPoint(
                        lon=-65.0,
                        lat=-65.0,
                    ),
                ]
            )
        ],
    ),
)
```


```rust
use qdrant_client::qdrant::{Condition, GeoLineString, GeoPoint, GeoPolygon};

Condition::geo_polygon(
    "location",
    GeoPolygon {
        exterior: Some(GeoLineString {
            points: vec![
                GeoPoint {
                    lon: -70.0,
                    lat: -70.0,
                },
                GeoPoint {
                    lon: 60.0,
                    lat: -70.0,
                },
                GeoPoint {
                    lon: 60.0,
                    lat: 60.0,
                },
                GeoPoint {
                    lon: -70.0,
                    lat: 60.0,
                },
                GeoPoint {
                    lon: -70.0,
                    lat: -70.0,
                },
            ],
        }),
        interiors: vec![GeoLineString {
            points: vec![
                GeoPoint {
                    lon: -65.0,
                    lat: -65.0,
                },
                GeoPoint {
                    lon: 0.0,
                    lat: -65.0,
                },
                GeoPoint { lon: 0.0, lat: 0.0 },
                GeoPoint {
                    lon: -65.0,
                    lat: 0.0,
                },
                GeoPoint {
                    lon: -65.0,
                    lat: -65.0,
                },
            ],
        }],
    },
)
```


```typescript
{
  key: "location",
  geo_polygon: {
    exterior: {
      points: [
        {
          lon: -70.0,
          lat: -70.0
        },
        {
          lon: 60.0,
          lat: -70.0
        },
        {
          lon: 60.0,
          lat: 60.0
        },
        {
          lon: -70.0,
          lat: 60.0
        },
        {
          lon: -70.0,
          lat: -70.0
        }
      ]
    },
    interiors: [
      {
        points: [
          {
            lon: -65.0,
            lat: -65.0
          },
          {
            lon: 0,
            lat: -65.0
          },
          {
            lon: 0,
            lat: 0
          },
          {
            lon: -65.0,
            lat: 0
          },
          {
            lon: -65.0,
            lat: -65.0
          }
        ]
      }
    ]
  }
}
```
