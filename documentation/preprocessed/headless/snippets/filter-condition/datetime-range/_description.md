This code snippet represents a filter condition based on date range for a specific field. The condition specifies that the date should be greater than "2023-02-08T10:49:00Z" and less than or equal to "2024-01-31T10:14:31Z". The comparison for dates is done based on the RFC 3339 format, and no conversion to UNIX timestamps is required. The dates are parsed and compared in UTC format.

```csharp
using Qdrant.Client.Grpc;

Conditions.DatetimeRange(
    field: "date",
    gt: new DateTime(2023, 2, 8, 10, 49, 0, DateTimeKind.Utc),
    lte: new DateTime(2024, 1, 31, 10, 14, 31, DateTimeKind.Utc)
);
```


```go
import (
	"time"

	"github.com/qdrant/go-client/qdrant"
	"google.golang.org/protobuf/types/known/timestamppb"
)

qdrant.NewDatetimeRange("date", &qdrant.DatetimeRange{
	Gt:  timestamppb.New(time.Date(2023, 2, 8, 10, 49, 0, 0, time.UTC)),
	Lte: timestamppb.New(time.Date(2024, 1, 31, 10, 14, 31, 0, time.UTC)),
})
```


```java
import static io.qdrant.client.ConditionFactory.datetimeRange;

import com.google.protobuf.Timestamp;
import io.qdrant.client.grpc.Common.DatetimeRange;
import java.time.Instant;

long gt = Instant.parse("2023-02-08T10:49:00Z").getEpochSecond();
long lte = Instant.parse("2024-01-31T10:14:31Z").getEpochSecond();

datetimeRange("date",
    DatetimeRange.newBuilder()
        .setGt(Timestamp.newBuilder().setSeconds(gt))
        .setLte(Timestamp.newBuilder().setSeconds(lte))
        .build());
```


```json
{
  "key": "date",
  "range": {
    "gt": "2023-02-08T10:49:00Z",
    "gte": null,
    "lt": null,
    "lte": "2024-01-31 10:14:31Z"
  }
}
```


```python
models.FieldCondition(
    key="date",
    range=models.DatetimeRange(
        gt="2023-02-08T10:49:00Z",
        gte=None,
        lt=None,
        lte="2024-01-31T10:14:31Z",
    ),
)
```


```rust
use qdrant_client::qdrant::{Condition, DatetimeRange, Timestamp};

Condition::datetime_range(
    "date",
    DatetimeRange {
        gt: Some(Timestamp::date_time(2023, 2, 8, 10, 49, 0).unwrap()),
        gte: None,
        lt: None,
        lte: Some(Timestamp::date_time(2024, 1, 31, 10, 14, 31).unwrap()),
    },
)
```


```typescript
{
    key: 'date',
    range: {
        gt: '2023-02-08T10:49:00Z',
        gte: null,
        lt: null,
        lte: '2024-01-31T10:14:31Z'
    }
}
```
