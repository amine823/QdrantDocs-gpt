With this code snippet, you can perform batch operations on points like upserting, updating vectors, deleting vectors, setting, overwriting, deleting, and clearing payload data associated with points. The operations include inserting, updating, and deleting points along with their vectors and payload. Each operation is executed in order specified in the request payload.

```http
POST /collections/{collection_name}/points/batch
{
    "operations": [
        {
            "upsert": {
                "points": [
                    {
                        "id": 1,
                        "vector": [1.0, 2.0, 3.0, 4.0],
                        "payload": {}
                    }
                ]
            }
        },
        {
            "update_vectors": {
                "points": [
                    {
                        "id": 1,
                        "vector": [1.0, 2.0, 3.0, 4.0]
                    }
                ]
            }
        },
        {
            "delete_vectors": {
                "points": [1],
                "vector": [""]
            }
        },
        {
            "overwrite_payload": {
                "payload": {
                    "test_payload": "1"
                },
                "points": [1]
            }
        },
        {
            "set_payload": {
                "payload": {
                    "test_payload_2": "2",
                    "test_payload_3": "3"
                },
                "points": [1]
            }
        },
        {
            "delete_payload": {
                "keys": ["test_payload_2"],
                "points": [1]
            }
        },
        {
            "clear_payload": {
                "points": [1]
            }
        },
        {"delete": {"points": [1]}}
    ]
}
```


```java
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ValueFactory.value;
import static io.qdrant.client.VectorsFactory.vectors;

import io.qdrant.client.grpc.Points.PointStruct;
import io.qdrant.client.grpc.Points.PointVectors;
import io.qdrant.client.grpc.Points.PointsIdsList;
import io.qdrant.client.grpc.Points.PointsSelector;
import io.qdrant.client.grpc.Points.PointsUpdateOperation.ClearPayload;
import io.qdrant.client.grpc.Points.PointsUpdateOperation.DeletePayload;
import io.qdrant.client.grpc.Points.PointsUpdateOperation.DeletePoints;
import io.qdrant.client.grpc.Points.PointsUpdateOperation.DeleteVectors;
import io.qdrant.client.grpc.Points.PointsUpdateOperation.OverwritePayload;
import io.qdrant.client.grpc.Points.PointsUpdateOperation.PointStructList;
import io.qdrant.client.grpc.Points.PointsUpdateOperation.SetPayload;
import io.qdrant.client.grpc.Points.PointsUpdateOperation.UpdateVectors;
import io.qdrant.client.grpc.Points.PointsUpdateOperation;
import io.qdrant.client.grpc.Points.VectorsSelector;
import java.util.List;
import java.util.Map;

client
    .batchUpdateAsync(
        "{collection_name}",
        List.of(
            PointsUpdateOperation.newBuilder()
                .setUpsert(
                    PointStructList.newBuilder()
                        .addPoints(
                            PointStruct.newBuilder()
                                .setId(id(1))
                                .setVectors(vectors(1.0f, 2.0f, 3.0f, 4.0f))
                                .build())
                        .build())
                .build(),
            PointsUpdateOperation.newBuilder()
                .setUpdateVectors(
                    UpdateVectors.newBuilder()
                        .addPoints(
                            PointVectors.newBuilder()
                                .setId(id(1))
                                .setVectors(vectors(1.0f, 2.0f, 3.0f, 4.0f))
                                .build())
                        .build())
                .build(),
            PointsUpdateOperation.newBuilder()
                .setDeleteVectors(
                    DeleteVectors.newBuilder()
                        .setPointsSelector(
                            PointsSelector.newBuilder()
                                .setPoints(PointsIdsList.newBuilder().addIds(id(1)).build())
                                .build())
                        .setVectors(VectorsSelector.newBuilder().addNames("").build())
                        .build())
                .build(),
            PointsUpdateOperation.newBuilder()
                .setOverwritePayload(
                    OverwritePayload.newBuilder()
                        .setPointsSelector(
                            PointsSelector.newBuilder()
                                .setPoints(PointsIdsList.newBuilder().addIds(id(1)).build())
                                .build())
                        .putAllPayload(Map.of("test_payload", value(1)))
                        .build())
                .build(),
            PointsUpdateOperation.newBuilder()
                .setSetPayload(
                    SetPayload.newBuilder()
                        .setPointsSelector(
                            PointsSelector.newBuilder()
                                .setPoints(PointsIdsList.newBuilder().addIds(id(1)).build())
                                .build())
                        .putAllPayload(
                            Map.of("test_payload_2", value(2), "test_payload_3", value(3)))
                        .build())
                .build(),
            PointsUpdateOperation.newBuilder()
                .setDeletePayload(
                    DeletePayload.newBuilder()
                        .setPointsSelector(
                            PointsSelector.newBuilder()
                                .setPoints(PointsIdsList.newBuilder().addIds(id(1)).build())
                                .build())
                        .addKeys("test_payload_2")
                        .build())
                .build(),
            PointsUpdateOperation.newBuilder()
                .setClearPayload(
                    ClearPayload.newBuilder()
                        .setPoints(
                            PointsSelector.newBuilder()
                                .setPoints(PointsIdsList.newBuilder().addIds(id(1)).build())
                                .build())
                        .build())
                .build(),
            PointsUpdateOperation.newBuilder()
                .setDeletePoints(
                    DeletePoints.newBuilder()
                        .setPoints(
                            PointsSelector.newBuilder()
                                .setPoints(PointsIdsList.newBuilder().addIds(id(1)).build())
                                .build())
                        .build())
                .build()))
    .get();
```


```python
client.batch_update_points(
    collection_name="{collection_name}",
    update_operations=[
        models.UpsertOperation(
            upsert=models.PointsList(
                points=[
                    models.PointStruct(
                        id=1,
                        vector=[1.0, 2.0, 3.0, 4.0],
                        payload={},
                    ),
                ]
            )
        ),
        models.UpdateVectorsOperation(
            update_vectors=models.UpdateVectors(
                points=[
                    models.PointVectors(
                        id=1,
                        vector=[1.0, 2.0, 3.0, 4.0],
                    )
                ]
            )
        ),
        models.DeleteVectorsOperation(
            delete_vectors=models.DeleteVectors(points=[1], vector=[""])
        ),
        models.OverwritePayloadOperation(
            overwrite_payload=models.SetPayload(
                payload={"test_payload": 1},
                points=[1],
            )
        ),
        models.SetPayloadOperation(
            set_payload=models.SetPayload(
                payload={
                    "test_payload_2": 2,
                    "test_payload_3": 3,
                },
                points=[1],
            )
        ),
        models.DeletePayloadOperation(
            delete_payload=models.DeletePayload(keys=["test_payload_2"], points=[1])
        ),
        models.ClearPayloadOperation(clear_payload=models.PointIdsList(points=[1])),
        models.DeleteOperation(delete=models.PointIdsList(points=[1])),
    ],
)
```


```rust
use std::collections::HashMap;

use qdrant_client::qdrant::{
    points_update_operation::{
        ClearPayload, DeletePayload, DeletePoints, DeleteVectors, Operation, OverwritePayload,
        PointStructList, SetPayload, UpdateVectors,
    },
    PointStruct, PointVectors, PointsUpdateOperation, UpdateBatchPointsBuilder, VectorsSelector,
};
use qdrant_client::Payload;

client
    .update_points_batch(
        UpdateBatchPointsBuilder::new(
            "{collection_name}",
            vec![
                PointsUpdateOperation {
                    operation: Some(Operation::Upsert(PointStructList {
                        points: vec![PointStruct::new(
                            1,
                            vec![1.0, 2.0, 3.0, 4.0],
                            Payload::default(),
                        )],
                        ..Default::default()
                    })),
                },
                PointsUpdateOperation {
                    operation: Some(Operation::UpdateVectors(UpdateVectors {
                        points: vec![PointVectors {
                            id: Some(1.into()),
                            vectors: Some(vec![1.0, 2.0, 3.0, 4.0].into()),
                        }],
                        ..Default::default()
                    })),
                },
                PointsUpdateOperation {
                    operation: Some(Operation::DeleteVectors(DeleteVectors {
                        points_selector: Some(vec![1.into()].into()),
                        vectors: Some(VectorsSelector {
                            names: vec!["".into()],
                        }),
                        ..Default::default()
                    })),
                },
                PointsUpdateOperation {
                    operation: Some(Operation::OverwritePayload(OverwritePayload {
                        points_selector: Some(vec![1.into()].into()),
                        payload: HashMap::from([("test_payload".to_string(), 1.into())]),
                        ..Default::default()
                    })),
                },
                PointsUpdateOperation {
                    operation: Some(Operation::SetPayload(SetPayload {
                        points_selector: Some(vec![1.into()].into()),
                        payload: HashMap::from([
                            ("test_payload_2".to_string(), 2.into()),
                            ("test_payload_3".to_string(), 3.into()),
                        ]),
                        ..Default::default()
                    })),
                },
                PointsUpdateOperation {
                    operation: Some(Operation::DeletePayload(DeletePayload {
                        points_selector: Some(vec![1.into()].into()),
                        keys: vec!["test_payload_2".to_string()],
                        ..Default::default()
                    })),
                },
                PointsUpdateOperation {
                    operation: Some(Operation::ClearPayload(ClearPayload {
                        points: Some(vec![1.into()].into()),
                        ..Default::default()
                    })),
                },
                PointsUpdateOperation {
                    operation: Some(Operation::DeletePoints(DeletePoints {
                        points: Some(vec![1.into()].into()),
                        ..Default::default()
                    })),
                },
            ],
        )
        .wait(true),
    )
    .await?;
```


```typescript
client.batchUpdate("{collection_name}", {
  operations: [
    {
      upsert: {
        points: [
          {
            id: 1,
            vector: [1.0, 2.0, 3.0, 4.0],
            payload: {},
          },
        ],
      },
    },
    {
      update_vectors: {
        points: [
          {
            id: 1,
            vector: [1.0, 2.0, 3.0, 4.0],
          },
        ],
      },
    },
    {
      delete_vectors: {
        points: [1],
        vector: [""],
      },
    },
    {
      overwrite_payload: {
        payload: {
          test_payload: 1,
        },
        points: [1],
      },
    },
    {
      set_payload: {
        payload: {
          test_payload_2: 2,
          test_payload_3: 3,
        },
        points: [1],
      },
    },
    {
      delete_payload: {
        keys: ["test_payload_2"],
        points: [1],
      },
    },
    {
      clear_payload: {
        points: [1],
      },
    },
    {
      delete: {
        points: [1],
      },
    },
  ],
});
```
