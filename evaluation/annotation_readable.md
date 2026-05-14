
================================================================================
QUERY:
How to batch update points using Python?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 501
Retrieved by: dense 1, sparse 1, hybrid 1, colbert 7
Section: Points — Batch update
--------------------------------------------------------------------------------

Points — Batch update

_Available as of v1.5.0_
You can batch multiple point update operations. This includes inserting,
updating and deleting points, vectors and payload.
A batch update request consists of a list of operations. These are executed in
order. These operations can be batched:
 Upsert points: `upsert` or `UpsertOperation`
 Delete points: `delete_points` or `DeleteOperation`
 Update vectors: `update_vectors` or `UpdateVectorsOperation`
 Delete vectors: `delete_vectors` or `DeleteVectorsOperation`
 Set payload: `set_payload` or `SetPayloadOperation`
 Overwrite payload: `overwrite_payload` or `OverwritePayload`
 Delete payload: `delete_payload` or `DeletePayloadOperation`
 Clear payload: `clear_payload` or `ClearPayloadOperation`
The following example snippet makes use of all operations.
REST API (Schema):
{{}}
To batch many points with a single operation type, please use batching
functionality in that operation directly.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1459
Retrieved by: dense 2, sparse 2, hybrid 2, colbert 4
Section: Introduction
--------------------------------------------------------------------------------

Introduction

You can efficiently upload multiple points into Qdrant with a single API call using batching. This snippet demonstrates the process of creating new points with a batch operation. The batch contains IDs, payloads (such as color information), and vectors for each point. By grouping points together, you can reduce network connection overhead and improve performance.

```http_code_1```


```python_code_2```


```typescript_code_3```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1357
Retrieved by: dense 3, sparse 4, hybrid 3, colbert 1
Section: Introduction
--------------------------------------------------------------------------------

Introduction

With this code snippet, you can perform batch operations on points like upserting, updating vectors, deleting vectors, setting, overwriting, deleting, and clearing payload data associated with points. The operations include inserting, updating, and deleting points along with their vectors and payload. Each operation is executed in order specified in the request payload.

```http_code_1```


```java_code_2```


```python_code_3```


```rust_code_4```


```typescript_code_5```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1707
Retrieved by: dense 4, sparse 8, hybrid 5
Section: N8N — Operations — Point
--------------------------------------------------------------------------------

N8N — Operations — Point

Upsert Points Insert or update points in a collection
 Retrieve Point Get a single point by ID
 Retrieve Points Get multiple points by their IDs
 Delete Points Remove points from a collection
 Count Points Count points in a collection with optional filtering
 Scroll Points Scroll through all points in a collection
 Batch Update Points Perform multiple point operations in a single request

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1708
Retrieved by: dense 5, hybrid 10
Section: N8N — Operations — Vector
--------------------------------------------------------------------------------

N8N — Operations — Vector

Update Vectors Update vectors for existing points
 Delete Vectors Remove vectors from points

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1709
Retrieved by: dense 6
Section: N8N — Operations — Search
--------------------------------------------------------------------------------

N8N — Operations — Search

Query Points Search for similar vectors
 Query Points In Batch Perform multiple vector searches in batch
 Query Points Groups Group search results by payload field
 Matrix Pairs Calculate distance matrix between pairs of points
 Matrix Offsets Calculate distance matrix using offsets

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 486
Retrieved by: dense 7, sparse 3, hybrid 4, colbert 5
Section: Points — Upload points — Python client optimizations
--------------------------------------------------------------------------------

Points — Upload points — Python client optimizations

The Python client has additional features for loading points, which include:
 Parallelization
 A retry mechanism
 Lazy batching support
For example, you can read your data directly from hard drives, to avoid storing all data in RAM. You can use these
features with the `upload_collection` and `upload_points` methods.
Similar to the basic upsert API, these methods support both record-oriented and column-oriented formats.
upload_points is available as of v1.7.1. It has replaced upload_records which is now deprecated.
Column-oriented format:
```python_code_1```
If ids are not provided, Qdrant Client will generate them automatically as random UUIDs.
Record-oriented format:
```python_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 485
Retrieved by: dense 8, hybrid 8
Section: Points — Upload points
--------------------------------------------------------------------------------

Points — Upload points

To optimize performance, Qdrant supports batch loading of points. I.e., you can load several points into the service in one API call.
Batching allows you to minimize the overhead of creating a network connection.
The Qdrant API supports two ways of creating batches record-oriented and column-oriented.
Internally, these options do not differ and are made only for the convenience of interaction.
Create points with batch:
{{}}
or record-oriented equivalent:
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1592
Retrieved by: dense 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet represents an operation to update vectors associated with points in a collection. The operation uses a PUT request to update vectors for specific points by providing their IDs along with the new vector data. This method ensures that only the specified vectors are updated, while leaving any unspecified vectors unchanged. It is important to note that all the provided points must already exist in the collection for the update to be successful.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 633
Retrieved by: dense 10, colbert 3
Section: Migrate to a New Embedding Model with Zero Downtime — Step 3: Migrate the Existing Points into the New Collection
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — Step 3: Migrate the Existing Points into the New Collection

Now that you're in dual-write mode, it is time to migrate the existing points from the old collection to the new one. This can be done in a separate process that runs
in parallel with the regular upsert services.
The migration process reads the points from the old collection, re-embeds them using the new model, and writes them to the new collection, making sure not to overwrite existing points inserted by the update service. Here's an example of what the code for such a migration process could look like:
```python_code_1```
Breaking down this code step by step:
 Data is read from the old collection in batches of 100 points using a scroll. The `last_offset` variable keeps track of the scroll position in the collection.
 For each batch of points, the process re-embeds the vectors using the new embedding model. It assumes that the original text used for embedding is stored in the payload under the key `text`.
 With the re-embedded vectors, it prepares conditional upsert operations for the new collection, keeping the original IDs and payloads. The conditional upserts use a filter condition to ensure that a point is only inserted if it does not already exist in the new collection. The filter checks whether a point with the given ID already exists. A point is only upserted if the ID does not exist in the new collection. This prevents overwriting newer updates from the regular update service.
 Finally, the process uses a batch update to upsert the re-embedded points into the new collection. Note that it uses `batch_update_points` instead of `upsert`, because `batch_update_points` allows you to specify an update condition per upsert operation.
This kind of migration process can take some time, and the offset can be stored in a persistent way, so you can resume the migration process in case of a failure. You can use a database, a file, or any other persistent storage to keep track of the last offset. Having said that, because the conditional upserts would not overwrite any points in the new collection, you could safely restart the migration process from the beginning if needed.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 670
Retrieved by: sparse 5, hybrid 6, colbert 8
Section: Qdrant Edge Quickstart — Work with Points
--------------------------------------------------------------------------------

Qdrant Edge Quickstart — Work with Points

An Edge Shard has several methods to work with points. To add points, use the `update` method:
```python_code_1```
To retrieve a point by ID, use the `retrieve` method:
```python_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1466
Retrieved by: sparse 6, hybrid 9, colbert 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates how to insert a point with conditionally. Update condition is represented by a filter, if the filter matches existing points, the point will be updated. If condition doesn't match the point, the upsert operation will be ignored. If the point doesn't exist, it will be inserted as a new point.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1460
Retrieved by: sparse 7, hybrid 7, colbert 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet represents a functionality to update points in a collection. In this instance, it updates a point with id 1 by changing its payload to have a color of "red" and its vector coordinates to [0.9, 0.1, 0.1].

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1533
Retrieved by: sparse 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Update the specified properties with the provided values for the selected points within a collection. This code snippet demonstrates setting the payload data for specific points identified by their unique IDs in the collection.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 492
Retrieved by: sparse 10
Section: Points — Modify points — Update vectors
--------------------------------------------------------------------------------

Points — Modify points — Update vectors

_Available as of v1.2.0_
This method updates the specified vectors on the given points. Unspecified
vectors are kept unchanged. All given points must exist.
REST API (Schema):
{{}}
To update points and replace all of its vectors, see uploading
points.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 632
Retrieved by: colbert 2
Section: Migrate to a New Embedding Model with Zero Downtime — Step 2: Enable Dual Writes
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — Step 2: Enable Dual Writes

To ensure that both collections are kept up-to-date during the migration, you need to write any changes to both collections simultaneously. This way, any new data or updates to existing data are reflected in both collections.
Ideally, the data in Qdrant is updated by an update service reading from an update queue. This service is responsible for embedding the documents and writing them to Qdrant. It uses code similar to this:
```python_code_1```
To update the new collection, deploy a second service that updates the new collection in parallel with the existing one. This service uses the new embedding model to encode the documents and writes them to the new collection:
```python_code_2```
A good practice is to always ensure that both operations succeed. Any errors need to be handled on the client side. You could store errors in a log or "dead letter queue" for later processing. Transient errors can be retried at a later time. Other errors need to be analyzed and addressed accordingly.
If instead of update services, you have a monolithic application, you need to modify your application code to write to both collections simultaneously during the transition period. In your code, where you handle the embedding of the documents, you should add the logic to write to both collections.
Note that the method outlined in this tutorial only works for `upsert` operations. For example, a `delete` operation would fail on the new collection if a point does not exist yet, and that point would later be erroneously added by the migration process. If you use one of the following methods to modify points in your collection, you will need to pause those operations during the migration or implement additional logic to handle them:
 `.delete` removing specified points from the collection
 `.update_vectors` updating specified vectors on points
 `.delete_vectors` deleting specified vectors from points
 `.set_payload` setting payload values for specified points
 `.overwrite_payload` overwriting the entire payload of a specified point with a new payload
 `.delete_payload` deleting a specified key payload for points
 `.clear_payload` removing the entire payload for specified points
 `.batch_update_points` making batch updates to points, including their respective vectors and payloads
Please refer to the documentation of the SDK you are using, or the
HTTP/gRPC definitions, for the exact method names, as they may vary between languages.
After making these changes, you will be in a dual-write mode, where any change is written to both the old and new collection. This allows you to keep both collections up-to-date during the migration process.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 677
Retrieved by: colbert 6
Section: Synchronizing Qdrant Edge with a Server — Update a Server Collection from an Edge Shard
--------------------------------------------------------------------------------

Synchronizing Qdrant Edge with a Server — Update a Server Collection from an Edge Shard

To synchronize data from an Edge Shard to a server collection, implement a dual-write mechanism in your application. When you add or update a point in the Edge Shard, simultaneously store it in a server collection using the Qdrant client.
Instead of writing to the server collection directly, you may want to set up a background job or a message queue that handles the synchronization asynchronously. The device running the Edge Shard may not always have a stable internet connection, so queuing updates ensures that data is eventually synchronized when connectivity is restored.
First, initialize:
 an Edge Shard from scratch or from server-side snapshot
 Qdrant server connection.
Details
Initialize an Edge Shard:
```python_code_1```
Initialize a Qdrant client connection to the server and create the target collection if it does not exist:
```python_code_2```
Next, instantiate the queue that will hold the points that need to be synchronized with the server:
```python_code_3```
When adding or updating points in the Edge Shard, also enqueue the point for synchronization with the server.
```python_code_4```
A background worker can process the upload queue and synchronize points with the server collection.
This example uploads points in batches of up to 10 points at a time:
```python_code_5```
Make sure to properly handle errors and retries in case of network issues or server unavailability.

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How to delete specific payload keys using delete_payload?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 479
Retrieved by: dense 1, sparse 1, hybrid 1, colbert 1
Section: Payload — Update payload — Delete payload keys
--------------------------------------------------------------------------------

Payload — Update payload — Delete payload keys

Delete specific payload keys from points.
REST API (Schema):
{{}}
Alternatively, you can use filters to delete payload keys from the points.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 478
Retrieved by: dense 2, sparse 3, hybrid 2, colbert 3
Section: Payload — Update payload — Clear payload
--------------------------------------------------------------------------------

Payload — Update payload — Clear payload

This method removes all payload keys from specified points
REST API (Schema):
{{}}
You can also use models.FilterSelector to remove the points matching given filter criteria, instead of providing the ids.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1710
Retrieved by: dense 3, hybrid 5, colbert 10
Section: N8N — Operations — Payload
--------------------------------------------------------------------------------

N8N — Operations — Payload

Set Payload Set payload for points
 Overwrite Payload Replace entire payload for points
 Delete Payload Remove payload from points
 Clear Payload Clear all payload fields
 Payload Facets Get payload field statistics
 Create Payload Index Create an index for payload fields
 Delete Payload Index Remove a payload field index

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1418
Retrieved by: dense 4, sparse 5, hybrid 4, colbert 5
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet pertains to deleting specific keys from the payload of points. It specifies the keys to be deleted as 'color' and 'price' from the points with IDs 0, 3, and 100 within a collection.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1417
Retrieved by: dense 5, sparse 2, hybrid 3, colbert 2
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet shows an example of using filters to delete specific keys from a payload based on defined criteria. In this example, it showcases how to delete keys "color" and "price" where the "color" key matches the value "red".

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 476
Retrieved by: dense 6, sparse 6, hybrid 7, colbert 7
Section: Payload — Update payload — Set payload
--------------------------------------------------------------------------------

Payload — Update payload — Set payload

Set only the given payload values on a point.
REST API (Schema):
{{}}
You don't need to know the ids of the points you want to modify. The alternative
is to use filters.
{{}}
_Available as of v1.8.0_
It is possible to modify only a specific key of the payload by using the `key` parameter.
For instance, given the following payload JSON object on a point:
```json_code_1```
You can modify the `nested_property` of `property1` with the following request:
{{}}
Resulting in the following payload:
```json_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1359
Retrieved by: dense 7, sparse 8, hybrid 8, colbert 6
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates a functionality to clear payload keys from specific points by providing a list of point identifiers.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1113
Retrieved by: dense 8
Section: Mastra — Methods — `deleteIndex()`
--------------------------------------------------------------------------------

Mastra — Methods — `deleteIndex()`

`indexName` — `string` — Name of the index to delete

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 477
Retrieved by: dense 9, hybrid 10
Section: Payload — Update payload — Overwrite payload
--------------------------------------------------------------------------------

Payload — Update payload — Overwrite payload

Fully replace any existing payload with the given one.
REST API (Schema):
{{}}
Like set payload, you don't need to know the ids of the points
you want to modify. The alternative is to use filters.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 475
Retrieved by: dense 10, sparse 4, hybrid 6, colbert 4
Section: Payload — Update payload
--------------------------------------------------------------------------------

Payload — Update payload

Updating payloads in Qdrant offers flexible methods to manage vector metadata. The set payload method updates specific fields while keeping others unchanged, while the overwrite method replaces the entire payload. Developers can also use clear payload to remove all metadata or delete fields to remove specific keys without affecting the rest. These options provide precise control for adapting to dynamic datasets.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 481
Retrieved by: sparse 7, hybrid 9
Section: Payload — Facet counts
--------------------------------------------------------------------------------

Payload — Facet counts

Available as of v1.12.0
Faceting is a special counting technique that can be used for various purposes:
 Know which unique values exist for a payload key.
 Know the number of points that contain each unique value.
 Know how restrictive a filter would become by matching a specific value.
Specifically, it is a counting aggregation for the values in a field, akin to a `GROUP BY` with `COUNT(*)` commands in SQL.
These results for a specific field is called a "facet". For example, when you look at an e-commerce search results page, you might see a list of brands on the sidebar, showing the number of products for each brand. This would be a facet for a `"brand"` field.
In Qdrant you can facet on a field only if you have created a field index that supports MatchValue conditions for it, like a keyword index.
To get the facet counts for a field, you can use the following:
By default, the number of hits returned is limited to 10. To change this, use the limit parameter. Keep this in mind when checking the number of unique values a payload field contains.
REST API (Facet)
{{}}
The response will contain the counts for each unique value in the field:
```json_code_1```
The results are sorted by the count in descending order, then by the value in ascending order.
Only values with non-zero counts will be returned.
By default, the way Qdrant the counts for each value is approximate to achieve fast results. This should accurate enough for most cases, but if you need to debug your storage, you can use the `exact` parameter to get exact counts.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1404
Retrieved by: sparse 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Creates a payload index for a specific collection where the field is defined as a keyword type and marked as tenant-specific. This configuration allows Qdrant to optimize storage and retrieval by structuring the data based on the specified field for improved search efficiency of tenant-specific data subsets within the collection. This feature is particularly beneficial in multi-tenant environments where data subsets belong to different tenants, enabling more targeted and faster searches within the collection.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 499
Retrieved by: sparse 10
Section: Points — Scroll points — Order points by payload key
--------------------------------------------------------------------------------

Points — Scroll points — Order points by payload key

_Available as of v1.8.0_
When using the `scroll` API, you can sort the results by payload key. For example, you can retrieve points in chronological order if your payloads have a `"timestamp"` field, as is shown from the example below:
Without an appropriate index, payload-based ordering would create too much load on the system for each request. Qdrant therefore requires a payload index which supports Range filtering conditions on the field used for order_by
{{}}
You need to use the `order_by` `key` parameter to specify the payload key. Then you can add other fields to control the ordering, such as `direction` and `start_from`:
{{}}
When you use the order_by parameter, pagination is disabled.
When sorting is based on a non-unique value, it is not possible to rely on an ID offset. Thus, next_page_offset is not returned within the response. However, you can still do pagination by combining `"order_by": { "start_from": ... }` with a `{ "must_not": [{ "has_id": [...] }] }` filter.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1193
Retrieved by: colbert 8
Section: Administration — Strict mode — Disable retrieving via non indexed payload
--------------------------------------------------------------------------------

Administration — Strict mode — Disable retrieving via non indexed payload

Setting `unindexed_filtering_retrieve` to false prevents retrieving points by filtering on a non indexed payload key which can be very slow.
{{}}
Or turn it off later on an existing collection through the collection update API.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1326
Retrieved by: colbert 9
Section: Security — Authentication — Table of access
--------------------------------------------------------------------------------

Security — Authentication — Table of access

Check out this table to see which actions are allowed or denied based on the access level.
This is also applicable to using api keys instead of tokens. In that case, `api_key` maps to manage, while `read_only_api_key` maps to read-only.
 Symbols: ✅ Allowed | ❌ Denied | 🟡 Allowed, but filtered
list collections — ✅ — ✅ — 🟡 — 🟡
get collection info — ✅ — ✅ — ✅ — ✅
create collection — ✅ — ❌ — ❌ — ❌
delete collection — ✅ — ❌ — ❌ — ❌
update collection params — ✅ — ❌ — ❌ — ❌
get collection cluster info — ✅ — ✅ — ✅ — ✅
collection exists — ✅ — ✅ — ✅ — ✅
update collection cluster setup — ✅ — ❌ — ❌ — ❌
update aliases — ✅ — ❌ — ❌ — ❌
list collection aliases — ✅ — ✅ — 🟡 — 🟡
list aliases — ✅ — ✅ — 🟡 — 🟡
create shard key — ✅ — ❌ — ❌ — ❌
delete shard key — ✅ — ❌ — ❌ — ❌
create payload index — ✅ — ❌ — ✅ — ❌
delete payload index — ✅ — ❌ — ✅ — ❌
list collection snapshots — ✅ — ✅ — ✅ — ✅
create collection snapshot — ✅ — ❌ — ✅ — ❌
delete collection snapshot — ✅ — ❌ — ✅ — ❌
download collection snapshot — ✅ — ✅ — ✅ — ✅
upload collection snapshot — ✅ — ❌ — ❌ — ❌
recover collection snapshot — ✅ — ❌ — ❌ — ❌
list shard snapshots — ✅ — ✅ — ✅ — ✅
create shard snapshot — ✅ — ❌ — ✅ — ❌
delete shard snapshot — ✅ — ❌ — ✅ — ❌
download shard snapshot — ✅ — ✅ — ✅ — ✅
upload shard snapshot — ✅ — ❌ — ❌ — ❌
recover shard snapshot — ✅ — ❌ — ❌ — ❌
list full snapshots — ✅ — ✅ — ❌ — ❌
create full snapshot — ✅ — ❌ — ❌ — ❌
delete full snapshot — ✅ — ❌ — ❌ — ❌
download full snapshot — ✅ — ✅ — ❌ — ❌
get cluster info — ✅ — ✅ — ❌ — ❌
recover raft state — ✅ — ❌ — ❌ — ❌
delete peer — ✅ — ❌ — ❌ — ❌
get point — ✅ — ✅ — ✅ — ✅
get points — ✅ — ✅ — ✅ — ✅
upsert points — ✅ — ❌ — ✅ — ❌
update points batch — ✅ — ❌ — ✅ — ❌
| delete points | ✅ | ❌ | ✅ | ❌ | ❌ /
| delete vectors | ✅ | ❌ | ✅ | ❌ | ❌ /
overwrite payload — ✅ — ❌ — ✅ — ❌
delete payload — ✅ — ❌ — ✅ — ❌
clear payload — ✅ — ❌ — ✅ — ❌
scroll points — ✅ — ✅ — ✅ — ✅
query points — ✅ — ✅ — ✅ — ✅
search points — ✅ — ✅ — ✅ — ✅
search groups — ✅ — ✅ — ✅ — ✅
recommend points — ✅ — ✅ — ✅ — ✅
recommend groups — ✅ — ✅ — ✅ — ✅
discover points — ✅ — ✅ — ✅ — ✅
count points — ✅ — ✅ — ✅ — ✅
version — ✅ — ✅ — ✅ — ✅
readyz, healthz, livez — ✅ — ✅ — ✅ — ✅
telemetry — ✅ — ✅ — ❌ — ❌
metrics — ✅ — ✅ — ❌ — ❌

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
Example of update_vectors operation.
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 1708
Retrieved by: dense 1, sparse 4, hybrid 2, colbert 3
Section: N8N — Operations — Vector
--------------------------------------------------------------------------------

N8N — Operations — Vector

Update Vectors Update vectors for existing points
 Delete Vectors Remove vectors from points

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1592
Retrieved by: dense 2, sparse 1, hybrid 1, colbert 2
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet represents an operation to update vectors associated with points in a collection. The operation uses a PUT request to update vectors for specific points by providing their IDs along with the new vector data. This method ensures that only the specified vectors are updated, while leaving any unspecified vectors unchanged. It is important to note that all the provided points must already exist in the collection for the update to be successful.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1730
Retrieved by: dense 3, hybrid 6
Section: Vectorize.io — Further Reading
--------------------------------------------------------------------------------

Vectorize.io — Further Reading

Vectorize Documentation
 Vectorize Tutorials.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1590
Retrieved by: dense 4, sparse 7, hybrid 4
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Update the collection by setting the vectors to be saved on disk for a specific vector named 'my_vector'. This code snippet demonstrates the configuration to ensure that the vector data is saved on disk within the collection.

```bash_code_1```


```http_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1357
Retrieved by: dense 5, hybrid 10, colbert 7
Section: Introduction
--------------------------------------------------------------------------------

Introduction

With this code snippet, you can perform batch operations on points like upserting, updating vectors, deleting vectors, setting, overwriting, deleting, and clearing payload data associated with points. The operations include inserting, updating, and deleting points along with their vectors and payload. Each operation is executed in order specified in the request payload.

```http_code_1```


```java_code_2```


```python_code_3```


```rust_code_4```


```typescript_code_5```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1589
Retrieved by: dense 6, sparse 9, hybrid 7, colbert 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Update the collection with patch requests to put vector data on disk. This functionality allows you to specify vector parameters, such as setting vectors to be stored on disk, for a specific collection. In cases where the collection does not have named vectors, an empty name (`""`) should be used to perform this update. This feature provided by Qdrant version 1.4 enables modifications to collection parameters, including HNSW index, quantization, and disk configurations dynamically, without the need to recreate the collection. Additionally, segments containing index and quantized data will be automatically rebuilt in the background to align with the new parameters.

```bash_code_1```


```http_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1586
Retrieved by: dense 7
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates updating HNSW index and quantization parameters for a collection, as well as for a specific vector within the collection called `my_vector`. The values like `m`, `ef_construct`, compression type, and quantization settings are adjusted for optimization.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1469
Retrieved by: dense 8, sparse 8, hybrid 8
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet is for inserting a point with a multivector into a collection. It defines an operation to update a collection with a new point containing an ID and a vector represented by multiple arrays of values.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 364
Retrieved by: dense 9, colbert 5
Section: Collections — Update collection parameters — Update vector parameters
--------------------------------------------------------------------------------

Collections — Update collection parameters — Update vector parameters

Available as of v1.4.0
To update vector parameters using the collection update API, you must always specify a vector name. If your collection does not have named vectors, use an empty ("") name.
Qdrant 1.4 adds support for updating more collection parameters at runtime. HNSW
index, quantization and disk configurations can now be changed without
recreating a collection. Segments (with index and quantized data) will
automatically be rebuilt in the background to match updated parameters.
To put vector data on disk for a collection that does not have named vectors,
use `""` as name:
{{}}
To put vector data on disk for a collection that does have named vectors:
Note: To create a vector name, follow the procedure from our Points.
{{}}
In the following example the HNSW index and quantization parameters are updated,
both for the whole collection, and for `my_vector` specifically:
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 492
Retrieved by: dense 10, colbert 6
Section: Points — Modify points — Update vectors
--------------------------------------------------------------------------------

Points — Modify points — Update vectors

_Available as of v1.2.0_
This method updates the specified vectors on the given points. Unspecified
vectors are kept unchanged. All given points must exist.
REST API (Schema):
{{}}
To update points and replace all of its vectors, see uploading
points.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1706
Retrieved by: sparse 2, hybrid 3
Section: N8N — Operations — Collection
--------------------------------------------------------------------------------

N8N — Operations — Collection

List Collections List all collections in the Qdrant instance
 Create Collection Create a new collection with specified vector parameters
 Update Collection Update parameters of an existing collection
 Get Collection Get information about a specific collection
 Collection Exists Check if a collection exists
 Delete Collection Delete a collection

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 363
Retrieved by: sparse 3, hybrid 5, colbert 4
Section: Collections — Update collection parameters
--------------------------------------------------------------------------------

Collections — Update collection parameters

Dynamic parameter updates may be helpful, for example, for more efficient initial loading of vectors.
For example, you can disable indexing during the upload process, and enable it immediately after the upload is finished.
As a result, you will not waste extra computation resources on rebuilding the index.
The following command enables indexing for segments that have more than 10000 kB of vectors stored:
{{}}
The following parameters can be updated:
* `optimizers_config` see optimizer for details.
* `hnsw_config` see indexing for details.
* `quantization_config` see quantization for details.
* `vectors_config` vector-specific configuration, including individual `hnsw_config`, `quantization_config` and `on_disk` settings.
* `params` other collection parameters, including `write_consistency_factor` and `on_disk_payload`.
* `strict_mode_config` see strict mode for details.
Full API specification is available in schema definitions.
Calls to this endpoint may be blocking as it waits for existing optimizers to
finish. We recommended against using this in a production database as it may
introduce huge overhead due to the rebuilding of the index.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 496
Retrieved by: sparse 5, hybrid 9, colbert 9
Section: Points — Conditional updates
--------------------------------------------------------------------------------

Points — Conditional updates

_Available as of v1.16.0_
All update operations (including point insertion, vector updates, payload updates, and deletions) support configurable pre-conditions based on filters.
{{}}
While conditional payload modification and deletion covers the use-case of mass data modification, conditional point insertion and vector updates are particularly useful for implementing optimistic concurrency control in distributed systems.
A common scenario for such mechanism is when multiple clients try to update the same point independently.
Consider the following sequence of events:
 Client A reads point P.
 Client B reads point P.
 Client A modifies point P and writes it back to Qdrant.
 Client B modifies point P (based on the stale data) and writes it back to Qdrant, unintentionally overwriting changes made by Client A.
To prevent such situations, Client B can use conditional updates.
For this, we would need to introduce an additional field in the payload, e.g. `version`, which would be incremented on each update.
When Client A writes back the modified point P, it would set the condition that the `version` field must be equal to the value it read initially.
If Client B tries to write back its changes later, the condition would fail (as the `version` has been incremented by Client A), and Qdrant would reject the update, preventing accidental overwrites.
Instead of `version`, applications can use timestamps (assuming synchronized clocks) or any other monotonically increasing value that fits their data model.
This mechanism is especially useful in the scenarios of embedding model migration, where we need to resolve conflicts between regular application updates and background re-embedding tasks.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 501
Retrieved by: sparse 6, colbert 1
Section: Points — Batch update
--------------------------------------------------------------------------------

Points — Batch update

_Available as of v1.5.0_
You can batch multiple point update operations. This includes inserting,
updating and deleting points, vectors and payload.
A batch update request consists of a list of operations. These are executed in
order. These operations can be batched:
 Upsert points: `upsert` or `UpsertOperation`
 Delete points: `delete_points` or `DeleteOperation`
 Update vectors: `update_vectors` or `UpdateVectorsOperation`
 Delete vectors: `delete_vectors` or `DeleteVectorsOperation`
 Set payload: `set_payload` or `SetPayloadOperation`
 Overwrite payload: `overwrite_payload` or `OverwritePayload`
 Delete payload: `delete_payload` or `DeletePayloadOperation`
 Clear payload: `clear_payload` or `ClearPayloadOperation`
The following example snippet makes use of all operations.
REST API (Schema):
{{}}
To batch many points with a single operation type, please use batching
functionality in that operation directly.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1460
Retrieved by: sparse 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet represents a functionality to update points in a collection. In this instance, it updates a point with id 1 by changing its payload to have a color of "red" and its vector coordinates to [0.9, 0.1, 0.1].

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 488
Retrieved by: colbert 8
Section: Points — Upload points — Named vectors
--------------------------------------------------------------------------------

Points — Upload points — Named vectors

_Available as of v0.10.0_
If the collection was created with multiple vectors, each vector data can be provided using the vector's name:
{{}}
_Available as of v1.2.0_
Named vectors are optional. When uploading points, some vectors may be omitted.
For example, you can upload one point with only the `image` vector and a second
one with only the `text` vector.
When uploading a point with an existing ID, the existing point is deleted first,
then it is inserted with just the specified vectors. In other words, the entire
point is replaced, and any unspecified vectors are set to null. To keep existing
vectors unchanged and only update specified vectors, see update vectors.

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How can I modify several vectors at once?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 1708
Retrieved by: dense 1, hybrid 3
Section: N8N — Operations — Vector
--------------------------------------------------------------------------------

N8N — Operations — Vector

Update Vectors Update vectors for existing points
 Delete Vectors Remove vectors from points

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 491
Retrieved by: dense 2, sparse 4, hybrid 1, colbert 1
Section: Points — Modify points
--------------------------------------------------------------------------------

Points — Modify points

To change a point, you can modify its vectors or its payload. There are several
ways to do this.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1377
Retrieved by: dense 3, hybrid 6
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code defines a collection with the ability to store multiple vectors per record. Each vector, such as 'image' and 'text', has a unique name and is associated with specific distance and size parameters. The 'image' vector has a size of 4 and a distance metric of 'Dot', while the 'text' vector has a size of 8 and a distance metric of 'Cosine'. This feature enables the storage of different types of vectors within the same collection.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1592
Retrieved by: dense 4, hybrid 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet represents an operation to update vectors associated with points in a collection. The operation uses a PUT request to update vectors for specific points by providing their IDs along with the new vector data. This method ensures that only the specified vectors are updated, while leaving any unspecified vectors unchanged. It is important to note that all the provided points must already exist in the collection for the update to be successful.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1462
Retrieved by: dense 5, hybrid 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet allows inserting a point with named vectors into a collection. The point has an ID and contains vectors labeled as "image," "text," and "text-sparse." The "image" vector has four values, the "text" vector has five values, and the "text-sparse" vector includes indices and corresponding values.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 546
Retrieved by: dense 6, sparse 6, hybrid 7
Section: Vectors — Vector Types — Multivectors
--------------------------------------------------------------------------------

Vectors — Vector Types — Multivectors

Available as of v1.10.0
Qdrant supports the storing of a variable amount of same-shaped dense vectors in a single point.
This means that instead of a single dense vector, you can upload a matrix of dense vectors.
The length of the matrix is fixed, but the number of vectors in the matrix can be different for each point.
Multivectors look like this:
```json_code_1```
There are two scenarios where multivectors are useful:
 Multiple representation of the same object* For example, you can store multiple embeddings for pictures of the same object, taken from different angles. This approach assumes that the payload is same for all vectors.
 Late interaction embeddings* Some text embedding models can output multiple vectors for a single text.
For example, a family of models such as ColBERT output a relatively small vector for each token in the text.
In order to use multivectors, we need to specify a function that will be used to compare between matrices of vectors
Currently, Qdrant supports `max_sim` function, which is defined as a sum of maximum similarities between each pair of vectors in the matrices.
$$
score = \sum_{i=1}^{N} \max_{j=1}^{M} \text{Sim}(\text{vectorA}_i, \text{vectorB}_j)
$$
Where $N$ is the number of vectors in the first matrix, $M$ is the number of vectors in the second matrix, and $\text{Sim}$ is a similarity function, for example, cosine similarity.
To use multivectors, create a collection with the following configuration:
{{}}
To insert a point with multivector:
{{}}
To search with multivector (available in `query` API):
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1587
Retrieved by: dense 7
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Update collection parameters to adjust the optimizer's configuration. In this case, the code snippet demonstrates how to patch the collection by setting an indexing threshold of 10000 for more efficient initial loading of vectors. This allows you to optimize resource usage by enabling indexing selectively based on the number of vectors stored in each segment.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 757
Retrieved by: dense 8
Section: Twelve Labs — Creating a collection to insert the vectors
--------------------------------------------------------------------------------

Twelve Labs — Creating a collection to insert the vectors

```python_code_1```
```typescript_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 547
Retrieved by: dense 9, sparse 3, hybrid 5, colbert 2
Section: Vectors — Named Vectors
--------------------------------------------------------------------------------

Vectors — Named Vectors

In Qdrant, you can store multiple vectors of different sizes and types in the same data point. This is useful when you need to define your data with multiple embeddings to represent different features or modalities (e.g., image, text or video).
To store different vectors for each point, you need to create separate named vector spaces in the collection. You can define these vector spaces during collection creation and manage them independently.
Each vector should have a unique name. Vectors can represent different modalities and you can use different embedding models to generate them.
To create a collection with named vectors, you need to specify a configuration for each vector:
{{}}
To insert a point with named vectors:
{{}}
To search with named vectors (available in `query` API):
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 617
Retrieved by: dense 10
Section: Bulk Upload Vectors to a Qdrant Collection — Choose an Indexing Strategy — Defer HNSW graph construction (`m: 0`)
--------------------------------------------------------------------------------

Bulk Upload Vectors to a Qdrant Collection — Choose an Indexing Strategy — Defer HNSW graph construction (`m: 0`)

For dense vectors, setting the HNSW `m` parameter to `0` disables index building entirely. Vectors will still be stored, but not indexed until you enable indexing later.
```http_code_1```
```python_code_2```
```typescript_code_3```
```rust_code_4```
```java_code_5```
```csharp_code_6```
```go_code_7```
Once ingestion is complete, re-enable HNSW by setting `m` to your production value (usually 16 or 32).
```http_code_8```
```python_code_9```
```typescript_code_10```
```rust_code_11```
```java_code_12```
```csharp_code_13```
```go_code_14```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 620
Retrieved by: sparse 1, hybrid 2
Section: Bulk Upload Vectors to a Qdrant Collection — Parallel upload into multiple shards
--------------------------------------------------------------------------------

Bulk Upload Vectors to a Qdrant Collection — Parallel upload into multiple shards

In Qdrant, each collection is split into shards. Each shard has a separate Write-Ahead-Log (WAL), which is responsible for ordering operations.
By creating multiple shards, you can parallelize upload of a large dataset. From 2 to 4 shards per one machine is a reasonable number.
```http_code_1```
```python_code_2```
```typescript_code_3```
```rust_code_4```
```java_code_5```
```csharp_code_6```
```go_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 357
Retrieved by: sparse 2, hybrid 4, colbert 7
Section: Collections — Create a collection — Collection with multiple vectors
--------------------------------------------------------------------------------

Collections — Create a collection — Collection with multiple vectors

Available as of v0.10.0
It is possible to have multiple vectors per record.
This feature allows for multiple vector storages per collection.
To distinguish vectors in one record, they should have a unique name defined when creating the collection.
Each named vector in this mode has its distance and size:
{{}}
For rare use cases, it is possible to create a collection without any vector storage.
Available as of v1.1.1
For each named vector you can optionally specify
`hnsw_config` or
`quantization_config` to
deviate from the collection configuration. This can be useful to fine-tune
search performance on a vector level.
Available as of v1.2.0
Vectors all live in RAM for very quick access. On a per-vector basis you can set
`on_disk` to true to store all vectors on disk at all times. This will enable
the use of
memmaps,
which is suitable for ingesting a large amount of data.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1455
Retrieved by: sparse 5, hybrid 8
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet shows how to run multiple inference operations within a single request, even when models are hosted in different locations. The request generates three different named vectors for a single point: image embeddings using `jina-clip-v2` hosted by Jina AI, text embeddings using `all-minilm-l6-v2` hosted by Qdrant Cloud, and BM25 embeddings using the `bm25` model executed locally by the Qdrant cluster.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1378
Retrieved by: sparse 7
Section: Introduction
--------------------------------------------------------------------------------

Introduction

You can create a collection with named vectors in Qdrant by defining multiple vector spaces for different features or modalities like image and text. Each vector space can have a unique name along with specific size and distance calculation method. Additionally, you can include sparse vectors in the collection configuration for more efficient representation of data points.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 488
Retrieved by: sparse 8, colbert 6
Section: Points — Upload points — Named vectors
--------------------------------------------------------------------------------

Points — Upload points — Named vectors

_Available as of v0.10.0_
If the collection was created with multiple vectors, each vector data can be provided using the vector's name:
{{}}
_Available as of v1.2.0_
Named vectors are optional. When uploading points, some vectors may be omitted.
For example, you can upload one point with only the `image` vector and a second
one with only the `text` vector.
When uploading a point with an existing ID, the existing point is deleted first,
then it is inserted with just the specified vectors. In other words, the entire
point is replaced, and any unspecified vectors are set to null. To keep existing
vectors unchanged and only update specified vectors, see update vectors.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 459
Retrieved by: sparse 9
Section: Inference — Multiple Inference Operations
--------------------------------------------------------------------------------

Inference — Multiple Inference Operations

You can run multiple inference operations within a single request, even when models are hosted in different locations. This example generates three different named vectors for a single point: image embeddings using `jina-clip-v2` hosted by Jina AI, text embeddings using `all-minilm-l6-v2` hosted by Qdrant Cloud, and BM25 embeddings using the `bm25` model executed locally by the Qdrant cluster:
{{}}
When specifying multiple identical inference objects in a single request, the inference service generates embeddings only once and reuses the resulting vectors. This optimization is particularly beneficial when working with external model providers, as it reduces both latency and cost.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 383
Retrieved by: sparse 10
Section: Explore the data — Recommendation API — Multiple vectors
--------------------------------------------------------------------------------

Explore the data — Recommendation API — Multiple vectors

Available as of v0.10.0
If the collection was created with multiple vectors, the name of the vector should be specified in the recommendation request:
{{}}
Parameter `using` specifies which stored vectors to use for the recommendation.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 492
Retrieved by: colbert 3
Section: Points — Modify points — Update vectors
--------------------------------------------------------------------------------

Points — Modify points — Update vectors

_Available as of v1.2.0_
This method updates the specified vectors on the given points. Unspecified
vectors are kept unchanged. All given points must exist.
REST API (Schema):
{{}}
To update points and replace all of its vectors, see uploading
points.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 493
Retrieved by: colbert 4
Section: Points — Modify points — Delete vectors
--------------------------------------------------------------------------------

Points — Modify points — Delete vectors

_Available as of v1.2.0_
This method deletes just the specified vectors from the given points. Other
vectors are kept unchanged. Points are never deleted.
REST API (Schema):
{{}}
To delete entire points, see deleting points.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 482
Retrieved by: colbert 5
Section: Points
--------------------------------------------------------------------------------

Points

The points are the central entity that Qdrant operates with.
A point is a record consisting of a vector and an optional payload.
It looks like this:
```json_code_1```
You can search among the points grouped in one collection based on vector similarity.
This procedure is described in more detail in the search and filtering sections.
This section explains how to create and manage vectors.
Any point modification operation is asynchronous and takes place in 2 steps.
At the first stage, the operation is written to the Write-ahead-log.
After this moment, the service will not lose the data, even if the machine loses power supply.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 354
Retrieved by: colbert 8
Section: Collections
--------------------------------------------------------------------------------

Collections

A collection is a named set of points (vectors with a payload) among which you can search. The vector of each point within the same collection must have the same dimensionality and be compared by a single metric. Named vectors can be used to have multiple vectors in a single point, each of which can have their own dimensionality and metric requirements.
Distance metrics are used to measure similarities among vectors.
The choice of metric depends on the way vectors obtaining and, in particular, on the method of neural network encoder training.
Qdrant supports these most popular types of metrics:
* Dot product: `Dot` [[wiki]](
* Cosine similarity: `Cosine` [[wiki]](
* Euclidean distance: `Euclid` [[wiki]](
* Manhattan distance: `Manhattan` [[wiki]](
For search efficiency, Cosine similarity is implemented as dot-product over normalized vectors. Vectors are automatically normalized during upload
In addition to metrics and vector size, each collection uses its own set of parameters that controls collection optimization, index construction, and vacuum.
These settings can be changed at any time by a corresponding request.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1399
Retrieved by: colbert 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

When creating a collection with vectors and HNSW index stored on disk, it is recommended to set the `memmap_threshold` parameter based on your use case. For a balanced scenario, keep it equal to the `indexing_threshold` (default is 20000) to optimize all thresholds at once. If facing high write load and low RAM, set `memmap_threshold` lower than `indexing_threshold`, for example 10000, to prioritize converting segments to memmap storage before indexing. Remember, you can store both vectors and the HNSW index on disk by setting `hnsw_config.on_disk` to `true` during collection creation or updating.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1272
Retrieved by: colbert 10
Section: Configure Multitenancy — Partition by payload
--------------------------------------------------------------------------------

Configure Multitenancy — Partition by payload

When an instance is shared between multiple users, you may need to partition vectors by user. This is done so that each user can only access their own vectors and can't see the vectors of other users.
 Note: The key doesn't necessarily need to be named group_id. You can choose a name that best suits your data structure and naming conventions.
{{}}
2. Use a filter along with `group_id` to filter vectors for each user.
{{}}

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How do I remove one metadata field without touching others?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 372
Retrieved by: dense 1, hybrid 3
Section: Collections — Collection aliases — Remove alias
--------------------------------------------------------------------------------

Collections — Collection aliases — Remove alias

{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1591
Retrieved by: dense 2, sparse 4, hybrid 2, colbert 2
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Update collection metadata. This example demonstrates how to overwrite a specific field in the collection's metadata while leaving other fields unchanged. Collection metadata can be any JSON object that provides additional information about the collection.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 362
Retrieved by: dense 3, hybrid 6
Section: Collections — Delete collection
--------------------------------------------------------------------------------

Collections — Delete collection

{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 520
Retrieved by: dense 4, hybrid 7
Section: Snapshots — Create snapshot — Delete snapshot
--------------------------------------------------------------------------------

Snapshots — Create snapshot — Delete snapshot

Available as of v1.0.0
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 530
Retrieved by: dense 5
Section: Snapshots — Snapshots for the whole storage — Delete full storage snapshot
--------------------------------------------------------------------------------

Snapshots — Snapshots for the whole storage — Delete full storage snapshot

Available as of v1.0.0
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 478
Retrieved by: dense 6, hybrid 9
Section: Payload — Update payload — Clear payload
--------------------------------------------------------------------------------

Payload — Update payload — Clear payload

This method removes all payload keys from specified points
REST API (Schema):
{{}}
You can also use models.FilterSelector to remove the points matching given filter criteria, instead of providing the ids.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1113
Retrieved by: dense 7
Section: Mastra — Methods — `deleteIndex()`
--------------------------------------------------------------------------------

Mastra — Methods — `deleteIndex()`

`indexName` — `string` — Name of the index to delete

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1710
Retrieved by: dense 8, hybrid 10
Section: N8N — Operations — Payload
--------------------------------------------------------------------------------

N8N — Operations — Payload

Set Payload Set payload for points
 Overwrite Payload Replace entire payload for points
 Delete Payload Remove payload from points
 Clear Payload Clear all payload fields
 Payload Facets Get payload field statistics
 Create Payload Index Create an index for payload fields
 Delete Payload Index Remove a payload field index

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 635
Retrieved by: dense 9
Section: Migrate to a New Embedding Model with Zero Downtime — Step 5: Wrapping Up
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — Step 5: Wrapping Up

Once your application has switched to the new collection, disable the dual-write mode you implemented in Step 2. From now on, the application should only write to the new collection.
All searches are now performed using the new embeddings. If the old collection is no longer needed, you can safely delete it. To ensure you can roll back if necessary, keep a snapshot of the old collection.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 479
Retrieved by: dense 10
Section: Payload — Update payload — Delete payload keys
--------------------------------------------------------------------------------

Payload — Update payload — Delete payload keys

Delete specific payload keys from points.
REST API (Schema):
{{}}
Alternatively, you can use filters to delete payload keys from the points.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 475
Retrieved by: sparse 1, hybrid 1, colbert 1
Section: Payload — Update payload
--------------------------------------------------------------------------------

Payload — Update payload

Updating payloads in Qdrant offers flexible methods to manage vector metadata. The set payload method updates specific fields while keeping others unchanged, while the overwrite method replaces the entire payload. Developers can also use clear payload to remove all metadata or delete fields to remove specific keys without affecting the rest. These options provide precise control for adapting to dynamic datasets.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1394
Retrieved by: sparse 2, hybrid 4
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet is used to create a collection with a specific vector configuration and additional metadata. The metadata is provided as a JSON object, allowing you to store custom information about the collection. In this example, we add two metadata fields.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1356
Retrieved by: sparse 3, hybrid 5, colbert 9
Section: Usage statistics — Request information deletion
--------------------------------------------------------------------------------

Usage statistics — Request information deletion

We provide an email address so that users can request the complete removal of their data from all of our tools.
To do so, send an email to privacy@qdrant.com containing the unique identifier generated for your Qdrant installation.
You can find this identifier in the telemetry API response (`"id"` field), or in the logs of your Qdrant instance.
Any questions regarding the management of the data we collect can also be sent to this email address.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 947
Retrieved by: sparse 5, colbert 6
Section: Frequently Asked Questions: General Topics — Should I create one Qdrant collection per user?
--------------------------------------------------------------------------------

Frequently Asked Questions: General Topics — Should I create one Qdrant collection per user?

No. Creating one collection per user is more resource intensive.
Instead of creating separate collections for each user, we recommend creating a single collection and separate access using payloads. Each Qdrant point can have a payload as metadata. For multitenancy, you can include a `user_id` or `tenant_id` for each point. To optimize storage further, you can enable tenant indexing for payload fields.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1614
Retrieved by: sparse 6
Section: Creating a Hybrid Cloud Environment — Deleting a Hybrid Cloud Environment
--------------------------------------------------------------------------------

Creating a Hybrid Cloud Environment — Deleting a Hybrid Cloud Environment

To delete a Hybrid Cloud Environment, first delete all Qdrant database clusters in it. Then you can delete the environment itself.
To clean up your Kubernetes cluster, after deleting the Hybrid Cloud Environment, you can download the script from to remove all Qdrant related resources.
 This will destroy all Qdrant related resources from your cluster and is non reversible. Please make sure to double check your environment and that you have created and tested your backups before proceeding.
Run the following command while being connected to your Kubernetes cluster. The script requires `kubectl` and `helm` to be installed.
```shell_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1336
Retrieved by: sparse 7
Section: Filtering — Filtering on an Exact String
--------------------------------------------------------------------------------

Filtering — Filtering on an Exact String

To filter on exact strings, first create a payload index of type `keyword`for the field you want to filter on. A payload index makes filtering faster and reduces the load on the system.
Filtering on a field without an index is not possible on collections that run in strict mode. Strict mode is enabled by default on Qdrant Cloud.
For example, to filter books by author name, create a keyword index on the "author" field:
{{}}
Next, when querying the data, you also add a filter clause to the request. The following example searches for books related to "time travel" but only returns books written by H.G. Wells:
{{}}
The ranking of the results of this request is based on the vector similarity of the query. The filter only narrows down the results to those points where the `author` field exactly matches `H.G. Wells`. Furthermore, the filter is case-sensitive. Filtering for the lowercase value `h.g. wells` would not return any results.
The previous example only returns points that match the filter value. If you want the opposite: exclude points with a specific value, use a `must_not` clause instead of `must`. The following example only returns books not written by H.G. Wells:
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 369
Retrieved by: sparse 8, hybrid 8, colbert 3
Section: Collections — Collection info — Collection metadata
--------------------------------------------------------------------------------

Collections — Collection info — Collection metadata

Available as of v1.16.0
For convenience and better data organization, Qdrant allows attaching custom metadata to collections in the form of key-value pairs.
Adding metadata is treated as a part of collection configuration and synchronized across all nodes in a cluster with consensus protocol.
Collection metadata can be specified during collection creation:
{{}}
as well as updated later:
{{}}
Note, that update operation only modifies the specified metadata fields, leaving other fields unchanged.
When specified, metadata is returned as part of collection info:
``` json
{
    "result": {
        "config": {
            "metadata": {
                "my-metadata-field": {
                    "key-a": "value-a",
                    "key-b": 42
                },
                "another-field": 123
            }
        }
    }
}
```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 172
Retrieved by: sparse 9
Section: Navigate Your Codebase with Semantic Search and Qdrant — Data preparation — Code to natural language conversion
--------------------------------------------------------------------------------

Navigate Your Codebase with Semantic Search and Qdrant — Data preparation — Code to natural language conversion

Each programming language has its own syntax which is not a part of the natural
language. Thus, a general-purpose model probably does not understand the code
as is. We can, however, normalize the data by removing code specifics and
including additional context, such as module, class, function, and file name.
We took the following steps:
1. Extract the signature of the function, method, or other code construct.
2. Divide camel case and snake case names into separate words.
3. Take the docstring, comments, and other important metadata.
4. Build a sentence from the extracted data using a predefined template.
5. Remove the special characters and replace them with spaces.
As input, expect dictionaries with the same structure. Define a `textify`
function to do the conversion. We'll use an `inflection` library to convert
with different naming conventions.
```shell_code_1```
Once all dependencies are installed, we define the `textify` function:
```python_code_2```
Now we can use `textify` to convert all chunks into text representations:
```python_code_3```
This is how the `await_ready_for_timeout` function description appears:
```text_code_4```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1191
Retrieved by: sparse 10, colbert 4
Section: Administration — Recovery mode
--------------------------------------------------------------------------------

Administration — Recovery mode

Available as of v1.2.0
Recovery mode can help in situations where Qdrant fails to start repeatedly.
When starting in recovery mode, Qdrant only loads collection metadata to prevent
going out of memory. This allows you to resolve out of memory situations, for
example, by deleting a collection. After resolving Qdrant can be restarted
normally to continue operation.
In recovery mode, collection operations are limited to
deleting a
collection. That is because only collection metadata is loaded during recovery.
To enable recovery mode with the Qdrant Docker image you must set the
environment variable `QDRANT_ALLOW_RECOVERY_MODE=true`. The container will try
to start normally first, and restarts in recovery mode if initialisation fails
due to an out of memory error. This behavior is disabled by default.
If using a Qdrant binary, recovery mode can be enabled by setting a recovery
message in an environment variable, such as
`QDRANT__STORAGE__RECOVERY_MODE="My recovery message"`.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1421
Retrieved by: colbert 5
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates a way to delete specific vectors from specified points in a collection. It allows users to remove selected vectors while retaining other vectors associated with the points. The points themselves are not deleted during this process, only certain vectors are removed. This method is available starting from version 1.2.0.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 344
Retrieved by: colbert 7
Section: User Management — Removing a User from an Account
--------------------------------------------------------------------------------

User Management — Removing a User from an Account

Users can be removed from an account by clicking on their name in either User Management (via Actions). This option is only available after they've accepted the invitation to join, ensuring that only active users can be removed.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1501
Retrieved by: colbert 8
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates a technique to disable quantization for querying points from a collection. By setting the "ignore" parameter to true within the request parameters, quantization can be turned off, allowing for more precise search results without quantization affecting the output.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1232
Retrieved by: colbert 10
Section: Distributed deployment — Sharding — Moving shards
--------------------------------------------------------------------------------

Distributed deployment — Sharding — Moving shards

Available as of v0.9.0
Qdrant allows moving shards between nodes in the cluster and removing nodes from the cluster. This functionality unlocks the ability to dynamically scale the cluster size without downtime. It also allows you to upgrade or migrate nodes without downtime.
If your cluster is running in Qdrant Cloud, shards are balanced across the cluster nodes automatically. For more information see the Configuring Cloud Clusters and Cloud Cluster Scaling documentation.
Qdrant provides the information regarding the current shard distribution in the cluster with the Collection Cluster info API.
Use the Update collection cluster setup API to initiate the shard transfer:
```http_code_1```
You likely want to select a specific shard transfer method to get desired performance and guarantees.
After the transfer is initiated, the service will process it based on the used
transfer method keeping both shards in sync. Once the
transfer is completed, the old shard is deleted from the source node.
In case you want to downscale the cluster, you can move all shards away from a peer and then remove the peer using the remove peer API.
```http_code_2```
After that, Qdrant will exclude the node from the consensus, and the instance will be ready for shutdown.

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How can I completely replace the metadata of a point?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 1708
Retrieved by: dense 1, hybrid 1
Section: N8N — Operations — Vector
--------------------------------------------------------------------------------

N8N — Operations — Vector

Update Vectors Update vectors for existing points
 Delete Vectors Remove vectors from points

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 492
Retrieved by: dense 2, sparse 10, hybrid 3, colbert 10
Section: Points — Modify points — Update vectors
--------------------------------------------------------------------------------

Points — Modify points — Update vectors

_Available as of v1.2.0_
This method updates the specified vectors on the given points. Unspecified
vectors are kept unchanged. All given points must exist.
REST API (Schema):
{{}}
To update points and replace all of its vectors, see uploading
points.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1710
Retrieved by: dense 3, hybrid 5
Section: N8N — Operations — Payload
--------------------------------------------------------------------------------

N8N — Operations — Payload

Set Payload Set payload for points
 Overwrite Payload Replace entire payload for points
 Delete Payload Remove payload from points
 Clear Payload Clear all payload fields
 Payload Facets Get payload field statistics
 Create Payload Index Create an index for payload fields
 Delete Payload Index Remove a payload field index

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 477
Retrieved by: dense 4, hybrid 7, colbert 1
Section: Payload — Update payload — Overwrite payload
--------------------------------------------------------------------------------

Payload — Update payload — Overwrite payload

Fully replace any existing payload with the given one.
REST API (Schema):
{{}}
Like set payload, you don't need to know the ids of the points
you want to modify. The alternative is to use filters.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1474
Retrieved by: dense 5, hybrid 10, colbert 6
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet represents a functionality to overwrite the payload for specified points within a collection. It allows you to replace the current payload of the specified points with a new set of properties and values provided in the request body. The points that will have their payloads overwritten are identified by their respective IDs within the collection.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 476
Retrieved by: dense 6
Section: Payload — Update payload — Set payload
--------------------------------------------------------------------------------

Payload — Update payload — Set payload

Set only the given payload values on a point.
REST API (Schema):
{{}}
You don't need to know the ids of the points you want to modify. The alternative
is to use filters.
{{}}
_Available as of v1.8.0_
It is possible to modify only a specific key of the payload by using the `key` parameter.
For instance, given the following payload JSON object on a point:
```json_code_1```
You can modify the `nested_property` of `property1` with the following request:
{{}}
Resulting in the following payload:
```json_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1591
Retrieved by: dense 7, sparse 6, hybrid 6
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Update collection metadata. This example demonstrates how to overwrite a specific field in the collection's metadata while leaving other fields unchanged. Collection metadata can be any JSON object that provides additional information about the collection.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 495
Retrieved by: dense 8
Section: Points — Delete points
--------------------------------------------------------------------------------

Points — Delete points

REST API (Schema):
{{}}
Alternative way to specify which points to remove is to use filter.
{{}}
This example removes all points with `{ "color": "red" }` from the collection.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 491
Retrieved by: dense 9, colbert 9
Section: Points — Modify points
--------------------------------------------------------------------------------

Points — Modify points

To change a point, you can modify its vectors or its payload. There are several
ways to do this.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 633
Retrieved by: dense 10
Section: Migrate to a New Embedding Model with Zero Downtime — Step 3: Migrate the Existing Points into the New Collection
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — Step 3: Migrate the Existing Points into the New Collection

Now that you're in dual-write mode, it is time to migrate the existing points from the old collection to the new one. This can be done in a separate process that runs
in parallel with the regular upsert services.
The migration process reads the points from the old collection, re-embeds them using the new model, and writes them to the new collection, making sure not to overwrite existing points inserted by the update service. Here's an example of what the code for such a migration process could look like:
```python_code_1```
Breaking down this code step by step:
 Data is read from the old collection in batches of 100 points using a scroll. The `last_offset` variable keeps track of the scroll position in the collection.
 For each batch of points, the process re-embeds the vectors using the new embedding model. It assumes that the original text used for embedding is stored in the payload under the key `text`.
 With the re-embedded vectors, it prepares conditional upsert operations for the new collection, keeping the original IDs and payloads. The conditional upserts use a filter condition to ensure that a point is only inserted if it does not already exist in the new collection. The filter checks whether a point with the given ID already exists. A point is only upserted if the ID does not exist in the new collection. This prevents overwriting newer updates from the regular update service.
 Finally, the process uses a batch update to upsert the re-embedded points into the new collection. Note that it uses `batch_update_points` instead of `upsert`, because `batch_update_points` allows you to specify an update condition per upsert operation.
This kind of migration process can take some time, and the offset can be stored in a persistent way, so you can resume the migration process in case of a failure. You can use a database, a file, or any other persistent storage to keep track of the last offset. Having said that, because the conditional upserts would not overwrite any points in the new collection, you could safely restart the migration process from the beginning if needed.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 103
Retrieved by: sparse 1, hybrid 2
Section: Send S3 Data to Qdrant Vector Store with LangChain — Step 3: Loading Embeddings into Qdrant — Creating a Collection in Qdrant
--------------------------------------------------------------------------------

Send S3 Data to Qdrant Vector Store with LangChain — Step 3: Loading Embeddings into Qdrant — Creating a Collection in Qdrant

In Qdrant, data is organized in collections, each representing a set of embeddings (or points) and their associated metadata (payload). To store the embeddings generated earlier, you’ll first need to create a collection.
Here’s how to create a collection in Qdrant to store both text and image embeddings:
```python_code_1```
This function creates a collection for storing text (384 dimensions) and image (512 dimensions) embeddings, using cosine similarity to compare embeddings within the collection.
Once the collection is set up, you can load the embeddings into Qdrant. This involves inserting (or updating) the embeddings and their associated metadata (payload) into the specified collection.
Here’s the code for loading embeddings into Qdrant:
```python_code_2```
Explanation of Ingestion
1. Upserting the Data Point: The upsert method on the `qdrant_client` inserts each PointStruct into the specified collection. If a point with the same ID already exists, it will be updated with the new values.
2. Operation Info: The function returns `operation_info`, which contains details about the upsert operation, such as success status or any potential errors.
Running the Ingestion Code
Here’s how to call the function and ingest data:
```python_code_3```
The `PointStruct` is instantiated with these key parameters:
 id: A unique identifier for each embedding, typically an incremental index.
 vector: A dictionary holding the text and image inputs to be embedded. `qdrant-client` uses FastEmbed under the hood to automatically generate vector representations from these inputs locally.
 payload: A dictionary storing additional metadata, like product reviews and image references, which is invaluable for retrieval and context during searches.
The code dynamically loads folders from an S3 bucket, processes text and image files separately, and stores their embeddings and associated data in dedicated lists. It then creates a `PointStruct` for each data entry and calls the ingestion function to load it into Qdrant.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 947
Retrieved by: sparse 2, hybrid 4, colbert 2
Section: Frequently Asked Questions: General Topics — Should I create one Qdrant collection per user?
--------------------------------------------------------------------------------

Frequently Asked Questions: General Topics — Should I create one Qdrant collection per user?

No. Creating one collection per user is more resource intensive.
Instead of creating separate collections for each user, we recommend creating a single collection and separate access using payloads. Each Qdrant point can have a payload as metadata. For multitenancy, you can include a `user_id` or `tenant_id` for each point. To optimize storage further, you can enable tenant indexing for payload fields.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 81
Retrieved by: sparse 3, hybrid 8
Section: Quick Start with Qdrant Cloud — 5. Populate the collection
--------------------------------------------------------------------------------

Quick Start with Qdrant Cloud — 5. Populate the collection

Next, we will populate the collection with menu items. Each item will be represented as a point in the collection, with its vector embedding and associated metadata.
```python_code_1```
```rust_code_2```
```typescript_code_3```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 475
Retrieved by: sparse 4, hybrid 9, colbert 3
Section: Payload — Update payload
--------------------------------------------------------------------------------

Payload — Update payload

Updating payloads in Qdrant offers flexible methods to manage vector metadata. The set payload method updates specific fields while keeping others unchanged, while the overwrite method replaces the entire payload. Developers can also use clear payload to remove all metadata or delete fields to remove specific keys without affecting the rest. These options provide precise control for adapting to dynamic datasets.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1394
Retrieved by: sparse 5
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet is used to create a collection with a specific vector configuration and additional metadata. The metadata is provided as a JSON object, allowing you to store custom information about the collection. In this example, we add two metadata fields.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 369
Retrieved by: sparse 7
Section: Collections — Collection info — Collection metadata
--------------------------------------------------------------------------------

Collections — Collection info — Collection metadata

Available as of v1.16.0
For convenience and better data organization, Qdrant allows attaching custom metadata to collections in the form of key-value pairs.
Adding metadata is treated as a part of collection configuration and synchronized across all nodes in a cluster with consensus protocol.
Collection metadata can be specified during collection creation:
{{}}
as well as updated later:
{{}}
Note, that update operation only modifies the specified metadata fields, leaving other fields unchanged.
When specified, metadata is returned as part of collection info:
``` json
{
    "result": {
        "config": {
            "metadata": {
                "my-metadata-field": {
                    "key-a": "value-a",
                    "key-b": 42
                },
                "another-field": 123
            }
        }
    }
}
```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 984
Retrieved by: sparse 8, colbert 8
Section: Using FastEmbed with Qdrant for Vector Search — Add data
--------------------------------------------------------------------------------

Using FastEmbed with Qdrant for Vector Search — Add data

Now you can add two sample documents, their associated metadata, and a point `id` for each.
```python_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 634
Retrieved by: sparse 9, colbert 4
Section: Migrate to a New Embedding Model with Zero Downtime — Step 4: Change the Collection and Embedding Model for Searches
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — Step 4: Change the Collection and Embedding Model for Searches

Once the migration process is complete, and all the points from the old collection are re-embedded and stored in the new collection, you can roll out a configuration change of the backend application. There are two key changes you have to make:
1. The collection name. Switch this from the old collection to the new collection. If you're using a collection alias, switch the alias to point to the new collection.
2. The embedding model. Switch this from the old embedding model to the new embedding model.
If these values are hardcoded in your application, you will need to change them directly in the code and deploy a new version of your application. For example, if your current search code looks like this:
```python_code_1```
You need to change it in the following way:
```python_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 515
Retrieved by: colbert 5
Section: Similarity search — Grouping API — Lookup in groups
--------------------------------------------------------------------------------

Similarity search — Grouping API — Lookup in groups

Having multiple points for parts of the same item often introduces redundancy in the stored data. Which may be fine if the information shared by the points is small, but it can become a problem if the payload is large, because it multiplies the storage space needed to store the points by a factor of the amount of points we have per group.
One way of optimizing storage when using groups is to store the information shared by the points with the same group id in a single point in another collection. Then, when using the groups API, add the `with_lookup` parameter to bring the information from those points into each group.
Store only document-level metadata (e.g., titles, abstracts) in the lookup collection, not chunks or duplicated data.
This has the extra benefit of having a single point to update when the information shared by the points in a group changes.
For example, if you have a collection of documents, you may want to chunk them and store the points for the chunks in a separate collection, making sure that you store the point id from the document it belongs in the payload of the chunk point.
In this case, to bring the information from the documents into the chunks grouped by the document id, you can use the `with_lookup` parameter:
{{}}
For the `with_lookup` parameter, you can also use the shorthand `with_lookup="documents"` to bring the whole payload and vector(s) without explicitly specifying it.
The looked up result will show up under `lookup` in each group.
```json_code_1```
Since the lookup is done by matching directly with the point id, the lookup collection must be pre-populated with points where the `id` matches the `group_by` value (e.g., document_id) from your primary collection.
Any group id that is not an existing (and valid) point id in the lookup collection will be ignored, and the `lookup` field will be empty.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 488
Retrieved by: colbert 7
Section: Points — Upload points — Named vectors
--------------------------------------------------------------------------------

Points — Upload points — Named vectors

_Available as of v0.10.0_
If the collection was created with multiple vectors, each vector data can be provided using the vector's name:
{{}}
_Available as of v1.2.0_
Named vectors are optional. When uploading points, some vectors may be omitted.
For example, you can upload one point with only the `image` vector and a second
one with only the `text` vector.
When uploading a point with an existing ID, the existing point is deleted first,
then it is inserted with just the specified vectors. In other words, the entire
point is replaced, and any unspecified vectors are set to null. To keep existing
vectors unchanged and only update specified vectors, see update vectors.

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
What is the difference between set_payload and overwrite_payload?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 477
Retrieved by: dense 1, sparse 2, hybrid 1, colbert 2
Section: Payload — Update payload — Overwrite payload
--------------------------------------------------------------------------------

Payload — Update payload — Overwrite payload

Fully replace any existing payload with the given one.
REST API (Schema):
{{}}
Like set payload, you don't need to know the ids of the points
you want to modify. The alternative is to use filters.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1710
Retrieved by: dense 2, sparse 4, hybrid 3, colbert 3
Section: N8N — Operations — Payload
--------------------------------------------------------------------------------

N8N — Operations — Payload

Set Payload Set payload for points
 Overwrite Payload Replace entire payload for points
 Delete Payload Remove payload from points
 Clear Payload Clear all payload fields
 Payload Facets Get payload field statistics
 Create Payload Index Create an index for payload fields
 Delete Payload Index Remove a payload field index

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 475
Retrieved by: dense 3, sparse 1, hybrid 2, colbert 1
Section: Payload — Update payload
--------------------------------------------------------------------------------

Payload — Update payload

Updating payloads in Qdrant offers flexible methods to manage vector metadata. The set payload method updates specific fields while keeping others unchanged, while the overwrite method replaces the entire payload. Developers can also use clear payload to remove all metadata or delete fields to remove specific keys without affecting the rest. These options provide precise control for adapting to dynamic datasets.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 476
Retrieved by: dense 4, hybrid 6, colbert 6
Section: Payload — Update payload — Set payload
--------------------------------------------------------------------------------

Payload — Update payload — Set payload

Set only the given payload values on a point.
REST API (Schema):
{{}}
You don't need to know the ids of the points you want to modify. The alternative
is to use filters.
{{}}
_Available as of v1.8.0_
It is possible to modify only a specific key of the payload by using the `key` parameter.
For instance, given the following payload JSON object on a point:
```json_code_1```
You can modify the `nested_property` of `property1` with the following request:
{{}}
Resulting in the following payload:
```json_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1474
Retrieved by: dense 5, sparse 3, hybrid 4, colbert 4
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet represents a functionality to overwrite the payload for specified points within a collection. It allows you to replace the current payload of the specified points with a new set of properties and values provided in the request body. The points that will have their payloads overwritten are identified by their respective IDs within the collection.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 474
Retrieved by: dense 6, hybrid 8
Section: Payload — Create point with payload
--------------------------------------------------------------------------------

Payload — Create point with payload

REST API (Schema)
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1357
Retrieved by: dense 7, sparse 5, hybrid 5, colbert 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

With this code snippet, you can perform batch operations on points like upserting, updating vectors, deleting vectors, setting, overwriting, deleting, and clearing payload data associated with points. The operations include inserting, updating, and deleting points along with their vectors and payload. Each operation is executed in order specified in the request payload.

```http_code_1```


```java_code_2```


```python_code_3```


```rust_code_4```


```typescript_code_5```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 468
Retrieved by: dense 8
Section: Payload — Payload types — Float
--------------------------------------------------------------------------------

Payload — Payload types — Float

`float` 64-bit floating point number.
Example of single and multiple `float` values:
```json_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 496
Retrieved by: dense 9, colbert 9
Section: Points — Conditional updates
--------------------------------------------------------------------------------

Points — Conditional updates

_Available as of v1.16.0_
All update operations (including point insertion, vector updates, payload updates, and deletions) support configurable pre-conditions based on filters.
{{}}
While conditional payload modification and deletion covers the use-case of mass data modification, conditional point insertion and vector updates are particularly useful for implementing optimistic concurrency control in distributed systems.
A common scenario for such mechanism is when multiple clients try to update the same point independently.
Consider the following sequence of events:
 Client A reads point P.
 Client B reads point P.
 Client A modifies point P and writes it back to Qdrant.
 Client B modifies point P (based on the stale data) and writes it back to Qdrant, unintentionally overwriting changes made by Client A.
To prevent such situations, Client B can use conditional updates.
For this, we would need to introduce an additional field in the payload, e.g. `version`, which would be incremented on each update.
When Client A writes back the modified point P, it would set the condition that the `version` field must be equal to the value it read initially.
If Client B tries to write back its changes later, the condition would fail (as the `version` has been incremented by Client A), and Qdrant would reject the update, preventing accidental overwrites.
Instead of `version`, applications can use timestamps (assuming synchronized clocks) or any other monotonically increasing value that fits their data model.
This mechanism is especially useful in the scenarios of embedding model migration, where we need to resolve conflicts between regular application updates and background re-embedding tasks.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 479
Retrieved by: dense 10
Section: Payload — Update payload — Delete payload keys
--------------------------------------------------------------------------------

Payload — Update payload — Delete payload keys

Delete specific payload keys from points.
REST API (Schema):
{{}}
Alternatively, you can use filters to delete payload keys from the points.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1531
Retrieved by: sparse 6, hybrid 7
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Set the payload for points in a collection by applying a filter based on the specified properties. In this case, the code will set the payload with "property1" and "property2" values for points where the value of the "color" property is "red" within the specified collection. This approach allows for targeted modifications without needing to know the specific point ids.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1402
Retrieved by: sparse 7, hybrid 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates how to create a payload index for a timestamp field with an integer type. The "is_principal" property is set to true, indicating that this field will be used as the principal index for faster search performance. This feature is particularly useful for optimizing storage and speeding up search requests, especially when filtering data primarily based on the principal field, such as a timestamp in time-related data scenarios.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 433
Retrieved by: sparse 8, hybrid 10
Section: Indexing — Payload Index — Parameterized index
--------------------------------------------------------------------------------

Indexing — Payload Index — Parameterized index

Available as of v1.8.0
We've added a parameterized variant to the `integer` index, which allows
you to fine-tune indexing and search performance.
Both the regular and parameterized `integer` indexes use the following flags:
 `lookup`: enables support for direct lookup using
 Match filters.
 `range`: enables support for
 Range filters.
The regular `integer` index assumes both `lookup` and `range` are `true`. In
contrast, to configure a parameterized index, you would set only one of these
filters to `true`:
`true` — `true` — Regular integer index
`true` — `false` — Parameterized integer index
`false` — `true` — Parameterized integer index
`false` — `false` — No integer index
The parameterized index can enhance performance in collections with millions
of points. We encourage you to try it out. If it does not enhance performance
in your use case, you can always restore the regular `integer` index.
Note: If you set `"lookup": true` with a range filter, that may lead to
significant performance issues.
For example, the following code sets up a parameterized integer index which
supports only range filters:
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 481
Retrieved by: sparse 9
Section: Payload — Facet counts
--------------------------------------------------------------------------------

Payload — Facet counts

Available as of v1.12.0
Faceting is a special counting technique that can be used for various purposes:
 Know which unique values exist for a payload key.
 Know the number of points that contain each unique value.
 Know how restrictive a filter would become by matching a specific value.
Specifically, it is a counting aggregation for the values in a field, akin to a `GROUP BY` with `COUNT(*)` commands in SQL.
These results for a specific field is called a "facet". For example, when you look at an e-commerce search results page, you might see a list of brands on the sidebar, showing the number of products for each brand. This would be a facet for a `"brand"` field.
In Qdrant you can facet on a field only if you have created a field index that supports MatchValue conditions for it, like a keyword index.
To get the facet counts for a field, you can use the following:
By default, the number of hits returned is limited to 10. To change this, use the limit parameter. Keep this in mind when checking the number of unique values a payload field contains.
REST API (Facet)
{{}}
The response will contain the counts for each unique value in the field:
```json_code_1```
The results are sorted by the count in descending order, then by the value in ascending order.
Only values with non-zero counts will be returned.
By default, the way Qdrant the counts for each value is approximate to achieve fast results. This should accurate enough for most cases, but if you need to debug your storage, you can use the `exact` parameter to get exact counts.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1207
Retrieved by: sparse 10
Section: Capacity Planning — Choosing disk over RAM
--------------------------------------------------------------------------------

Capacity Planning — Choosing disk over RAM

For optimal performance, you should store only frequently accessed data in RAM. The rest should be offloaded to the disk. For example, extra payload fields that you don't use for filtering can be stored on disk.
Only indexed fields should be stored in RAM. You can read more about payload storage in the Storage section.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 501
Retrieved by: colbert 5
Section: Points — Batch update
--------------------------------------------------------------------------------

Points — Batch update

_Available as of v1.5.0_
You can batch multiple point update operations. This includes inserting,
updating and deleting points, vectors and payload.
A batch update request consists of a list of operations. These are executed in
order. These operations can be batched:
 Upsert points: `upsert` or `UpsertOperation`
 Delete points: `delete_points` or `DeleteOperation`
 Update vectors: `update_vectors` or `UpdateVectorsOperation`
 Delete vectors: `delete_vectors` or `DeleteVectorsOperation`
 Set payload: `set_payload` or `SetPayloadOperation`
 Overwrite payload: `overwrite_payload` or `OverwritePayload`
 Delete payload: `delete_payload` or `DeletePayloadOperation`
 Clear payload: `clear_payload` or `ClearPayloadOperation`
The following example snippet makes use of all operations.
REST API (Schema):
{{}}
To batch many points with a single operation type, please use batching
functionality in that operation directly.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 632
Retrieved by: colbert 7
Section: Migrate to a New Embedding Model with Zero Downtime — Step 2: Enable Dual Writes
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — Step 2: Enable Dual Writes

To ensure that both collections are kept up-to-date during the migration, you need to write any changes to both collections simultaneously. This way, any new data or updates to existing data are reflected in both collections.
Ideally, the data in Qdrant is updated by an update service reading from an update queue. This service is responsible for embedding the documents and writing them to Qdrant. It uses code similar to this:
```python_code_1```
To update the new collection, deploy a second service that updates the new collection in parallel with the existing one. This service uses the new embedding model to encode the documents and writes them to the new collection:
```python_code_2```
A good practice is to always ensure that both operations succeed. Any errors need to be handled on the client side. You could store errors in a log or "dead letter queue" for later processing. Transient errors can be retried at a later time. Other errors need to be analyzed and addressed accordingly.
If instead of update services, you have a monolithic application, you need to modify your application code to write to both collections simultaneously during the transition period. In your code, where you handle the embedding of the documents, you should add the logic to write to both collections.
Note that the method outlined in this tutorial only works for `upsert` operations. For example, a `delete` operation would fail on the new collection if a point does not exist yet, and that point would later be erroneously added by the migration process. If you use one of the following methods to modify points in your collection, you will need to pause those operations during the migration or implement additional logic to handle them:
 `.delete` removing specified points from the collection
 `.update_vectors` updating specified vectors on points
 `.delete_vectors` deleting specified vectors from points
 `.set_payload` setting payload values for specified points
 `.overwrite_payload` overwriting the entire payload of a specified point with a new payload
 `.delete_payload` deleting a specified key payload for points
 `.clear_payload` removing the entire payload for specified points
 `.batch_update_points` making batch updates to points, including their respective vectors and payloads
Please refer to the documentation of the SDK you are using, or the
HTTP/gRPC definitions, for the exact method names, as they may vary between languages.
After making these changes, you will be in a dual-write mode, where any change is written to both the old and new collection. This allows you to keep both collections up-to-date during the migration process.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 427
Retrieved by: colbert 8
Section: Hybrid and Multi-Stage Queries — Score boosting
--------------------------------------------------------------------------------

Hybrid and Multi-Stage Queries — Score boosting

If a score or variable is not available, and there is no default value, it will return an error.
 If a value is not a number (or the expected type), it will return an error.
 To leverage payload indices, single-value arrays are considered the same as the inner value. For example: `[0.2]` is the same as `0.2`, but `[0.2, 0.7]` will be interpreted as `[0.2, 0.7]`
 Multiplication and division are lazily evaluated, meaning that if a 0 is encountered, the rest of operations don't execute (e.g. `0.0 * condition` won't check the condition).
 Payload variables used within the formula also benefit from having payload indices. Please try to always have a payload index set up for the variables used in the formula for better performance.

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
When should I use clear_payload instead of delete_payload?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 478
Retrieved by: dense 1, sparse 1, hybrid 1, colbert 1
Section: Payload — Update payload — Clear payload
--------------------------------------------------------------------------------

Payload — Update payload — Clear payload

This method removes all payload keys from specified points
REST API (Schema):
{{}}
You can also use models.FilterSelector to remove the points matching given filter criteria, instead of providing the ids.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1710
Retrieved by: dense 2, sparse 3, hybrid 2, colbert 4
Section: N8N — Operations — Payload
--------------------------------------------------------------------------------

N8N — Operations — Payload

Set Payload Set payload for points
 Overwrite Payload Replace entire payload for points
 Delete Payload Remove payload from points
 Clear Payload Clear all payload fields
 Payload Facets Get payload field statistics
 Create Payload Index Create an index for payload fields
 Delete Payload Index Remove a payload field index

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 479
Retrieved by: dense 3, sparse 4, hybrid 4, colbert 6
Section: Payload — Update payload — Delete payload keys
--------------------------------------------------------------------------------

Payload — Update payload — Delete payload keys

Delete specific payload keys from points.
REST API (Schema):
{{}}
Alternatively, you can use filters to delete payload keys from the points.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 475
Retrieved by: dense 4, sparse 2, hybrid 3, colbert 2
Section: Payload — Update payload
--------------------------------------------------------------------------------

Payload — Update payload

Updating payloads in Qdrant offers flexible methods to manage vector metadata. The set payload method updates specific fields while keeping others unchanged, while the overwrite method replaces the entire payload. Developers can also use clear payload to remove all metadata or delete fields to remove specific keys without affecting the rest. These options provide precise control for adapting to dynamic datasets.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 477
Retrieved by: dense 5, sparse 10, hybrid 5, colbert 7
Section: Payload — Update payload — Overwrite payload
--------------------------------------------------------------------------------

Payload — Update payload — Overwrite payload

Fully replace any existing payload with the given one.
REST API (Schema):
{{}}
Like set payload, you don't need to know the ids of the points
you want to modify. The alternative is to use filters.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1113
Retrieved by: dense 6
Section: Mastra — Methods — `deleteIndex()`
--------------------------------------------------------------------------------

Mastra — Methods — `deleteIndex()`

`indexName` — `string` — Name of the index to delete

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1207
Retrieved by: dense 7, hybrid 9
Section: Capacity Planning — Choosing disk over RAM
--------------------------------------------------------------------------------

Capacity Planning — Choosing disk over RAM

For optimal performance, you should store only frequently accessed data in RAM. The rest should be offloaded to the disk. For example, extra payload fields that you don't use for filtering can be stored on disk.
Only indexed fields should be stored in RAM. You can read more about payload storage in the Storage section.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 476
Retrieved by: dense 8, hybrid 10, colbert 10
Section: Payload — Update payload — Set payload
--------------------------------------------------------------------------------

Payload — Update payload — Set payload

Set only the given payload values on a point.
REST API (Schema):
{{}}
You don't need to know the ids of the points you want to modify. The alternative
is to use filters.
{{}}
_Available as of v1.8.0_
It is possible to modify only a specific key of the payload by using the `key` parameter.
For instance, given the following payload JSON object on a point:
```json_code_1```
You can modify the `nested_property` of `property1` with the following request:
{{}}
Resulting in the following payload:
```json_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 946
Retrieved by: dense 9
Section: Frequently Asked Questions: General Topics — Compatibility — Should I create payload indexes before or after uploading?
--------------------------------------------------------------------------------

Frequently Asked Questions: General Topics — Compatibility — Should I create payload indexes before or after uploading?

Create payload indexes before uploading to avoid index rebuilding. However, there are scenarios where defining idexes after uploading is okay. For example, you can configure a new filter logic after launch.
You should always index first if you know your filters upfront. If you need to index another payload later, you can still do it, but be aware of the performance hit.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 434
Retrieved by: dense 10
Section: Indexing — Payload Index — On-disk payload index
--------------------------------------------------------------------------------

Indexing — Payload Index — On-disk payload index

Available as of v1.11.0
By default all payload-related structures are stored in memory. In this way, the vector index can quickly access payload values during search.
As latency in this case is critical, it is recommended to keep hot payload indexes in memory.
There are, however, cases when payload indexes are too large or rarely used. In those cases, it is possible to store payload indexes on disk.
 On-disk payload index might affect cold requests latency, as it requires additional disk I/O operations.
To configure on-disk payload index, you can use the following index parameters:
{{}}
Payload index on-disk is supported for the following types:
* `keyword`
* `integer`
* `float`
* `datetime`
* `uuid`
* `text`
* `geo`
The list will be extended in future versions.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1417
Retrieved by: sparse 5, hybrid 6
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet shows an example of using filters to delete specific keys from a payload based on defined criteria. In this example, it showcases how to delete keys "color" and "price" where the "color" key matches the value "red".

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1359
Retrieved by: sparse 6, hybrid 7
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates a functionality to clear payload keys from specific points by providing a list of point identifiers.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1357
Retrieved by: sparse 7, hybrid 8, colbert 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

With this code snippet, you can perform batch operations on points like upserting, updating vectors, deleting vectors, setting, overwriting, deleting, and clearing payload data associated with points. The operations include inserting, updating, and deleting points along with their vectors and payload. Each operation is executed in order specified in the request payload.

```http_code_1```


```java_code_2```


```python_code_3```


```rust_code_4```


```typescript_code_5```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 508
Retrieved by: sparse 8
Section: Similarity search — Search API — Payload and vector in the result
--------------------------------------------------------------------------------

Similarity search — Search API — Payload and vector in the result

By default, retrieval methods do not return any stored information such as
payload and vectors. Additional parameters `with_vectors` and `with_payload`
alter this behavior.
Example:
{{}}
You can use `with_payload` to scope to or filter a specific payload subset.
You can even specify an array of items to include, such as `city`,
`village`, and `town`:
{{}}
Or use `include` or `exclude` explicitly. For example, to exclude `city`:
{{}}
It is possible to target nested fields using a dot notation:
* `payload.nested_field` for a nested field
* `payload.nested_array[].sub_field` for projecting nested fields within an array
Accessing array elements by index is currently not supported.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 507
Retrieved by: sparse 9
Section: Similarity search — Search API — Filtering results by score
--------------------------------------------------------------------------------

Similarity search — Search API — Filtering results by score

In addition to payload filtering, it might be useful to filter out results with a low similarity score.
For example, if you know the minimal acceptance score for your model and do not want any results which are less similar than the threshold.
In this case, you can use `score_threshold` parameter of the search query.
It will exclude all results with a score worse than the given.
This parameter may exclude lower or higher scores depending on the used metric. For example, higher scores of Euclidean metric are considered more distant and, therefore, will be excluded.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 632
Retrieved by: colbert 3
Section: Migrate to a New Embedding Model with Zero Downtime — Step 2: Enable Dual Writes
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — Step 2: Enable Dual Writes

To ensure that both collections are kept up-to-date during the migration, you need to write any changes to both collections simultaneously. This way, any new data or updates to existing data are reflected in both collections.
Ideally, the data in Qdrant is updated by an update service reading from an update queue. This service is responsible for embedding the documents and writing them to Qdrant. It uses code similar to this:
```python_code_1```
To update the new collection, deploy a second service that updates the new collection in parallel with the existing one. This service uses the new embedding model to encode the documents and writes them to the new collection:
```python_code_2```
A good practice is to always ensure that both operations succeed. Any errors need to be handled on the client side. You could store errors in a log or "dead letter queue" for later processing. Transient errors can be retried at a later time. Other errors need to be analyzed and addressed accordingly.
If instead of update services, you have a monolithic application, you need to modify your application code to write to both collections simultaneously during the transition period. In your code, where you handle the embedding of the documents, you should add the logic to write to both collections.
Note that the method outlined in this tutorial only works for `upsert` operations. For example, a `delete` operation would fail on the new collection if a point does not exist yet, and that point would later be erroneously added by the migration process. If you use one of the following methods to modify points in your collection, you will need to pause those operations during the migration or implement additional logic to handle them:
 `.delete` removing specified points from the collection
 `.update_vectors` updating specified vectors on points
 `.delete_vectors` deleting specified vectors from points
 `.set_payload` setting payload values for specified points
 `.overwrite_payload` overwriting the entire payload of a specified point with a new payload
 `.delete_payload` deleting a specified key payload for points
 `.clear_payload` removing the entire payload for specified points
 `.batch_update_points` making batch updates to points, including their respective vectors and payloads
Please refer to the documentation of the SDK you are using, or the
HTTP/gRPC definitions, for the exact method names, as they may vary between languages.
After making these changes, you will be in a dual-write mode, where any change is written to both the old and new collection. This allows you to keep both collections up-to-date during the migration process.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 501
Retrieved by: colbert 5
Section: Points — Batch update
--------------------------------------------------------------------------------

Points — Batch update

_Available as of v1.5.0_
You can batch multiple point update operations. This includes inserting,
updating and deleting points, vectors and payload.
A batch update request consists of a list of operations. These are executed in
order. These operations can be batched:
 Upsert points: `upsert` or `UpsertOperation`
 Delete points: `delete_points` or `DeleteOperation`
 Update vectors: `update_vectors` or `UpdateVectorsOperation`
 Delete vectors: `delete_vectors` or `DeleteVectorsOperation`
 Set payload: `set_payload` or `SetPayloadOperation`
 Overwrite payload: `overwrite_payload` or `OverwritePayload`
 Delete payload: `delete_payload` or `DeletePayloadOperation`
 Clear payload: `clear_payload` or `ClearPayloadOperation`
The following example snippet makes use of all operations.
REST API (Schema):
{{}}
To batch many points with a single operation type, please use batching
functionality in that operation directly.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 496
Retrieved by: colbert 8
Section: Points — Conditional updates
--------------------------------------------------------------------------------

Points — Conditional updates

_Available as of v1.16.0_
All update operations (including point insertion, vector updates, payload updates, and deletions) support configurable pre-conditions based on filters.
{{}}
While conditional payload modification and deletion covers the use-case of mass data modification, conditional point insertion and vector updates are particularly useful for implementing optimistic concurrency control in distributed systems.
A common scenario for such mechanism is when multiple clients try to update the same point independently.
Consider the following sequence of events:
 Client A reads point P.
 Client B reads point P.
 Client A modifies point P and writes it back to Qdrant.
 Client B modifies point P (based on the stale data) and writes it back to Qdrant, unintentionally overwriting changes made by Client A.
To prevent such situations, Client B can use conditional updates.
For this, we would need to introduce an additional field in the payload, e.g. `version`, which would be incremented on each update.
When Client A writes back the modified point P, it would set the condition that the `version` field must be equal to the value it read initially.
If Client B tries to write back its changes later, the condition would fail (as the `version` has been incremented by Client A), and Qdrant would reject the update, preventing accidental overwrites.
Instead of `version`, applications can use timestamps (assuming synchronized clocks) or any other monotonically increasing value that fits their data model.
This mechanism is especially useful in the scenarios of embedding model migration, where we need to resolve conflicts between regular application updates and background re-embedding tasks.
{{}}

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How to migrate to a new embedding model without downtime?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 634
Retrieved by: dense 1, sparse 4, hybrid 2, colbert 5
Section: Migrate to a New Embedding Model with Zero Downtime — Step 4: Change the Collection and Embedding Model for Searches
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — Step 4: Change the Collection and Embedding Model for Searches

Once the migration process is complete, and all the points from the old collection are re-embedded and stored in the new collection, you can roll out a configuration change of the backend application. There are two key changes you have to make:
1. The collection name. Switch this from the old collection to the new collection. If you're using a collection alias, switch the alias to point to the new collection.
2. The embedding model. Switch this from the old embedding model to the new embedding model.
If these values are hardcoded in your application, you will need to change them directly in the code and deploy a new version of your application. For example, if your current search code looks like this:
```python_code_1```
You need to change it in the following way:
```python_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 630
Retrieved by: dense 2, sparse 1, hybrid 1, colbert 1
Section: Migrate to a New Embedding Model with Zero Downtime — The Solution
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — The Solution

Switching the embedding model with zero downtime is possible by using a blue-green deployment with two collections. The first collection contains the old embeddings, and the second one is used to store the new embeddings. A migration process copies the data from the old collection to the new one, re-embedding vectors using the new model. During the migration, you keep searching the old collection while writing any data updates to both collections. Once all vectors are re-embedded, switch the search to use the new collection.
{{}}
Re-embedding requires access to the original data used to create the embeddings. This data can come from a primary database, or it may be stored in the payloads of the points in Qdrant. This tutorial assumes that the necessary data is stored in the payloads. This is usually the case, as the payload often contains the text or other data that was used to generate the embeddings.
The solution outlined in this tutorial only works for upsert operations. If you use deletes or partial updates, it is necessary to pause those operations during the migration or implement additional logic to handle them.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 629
Retrieved by: dense 3, sparse 3, hybrid 3, colbert 3
Section: Migrate to a New Embedding Model with Zero Downtime
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime

When building a semantic search application, you need to choose an embedding
model. Over time, you may want to switch to a different model for better
quality or cost-effectiveness. If your application is in production, this must be done with zero downtime to avoid
disrupting users. Switching models requires re-embedding all vectors in your collection, which can take time. If your
data doesn't change, you can re-embed everything and switch to the new embeddings. However, in systems with frequent
updates, stopping the search service to re-embed is not an option.
This tutorial will guide you step-by-step through the process of migrating to a new model, including the changes you have to make in your project. The examples all use the Python SDK, but the same principles apply to other languages as well.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 631
Retrieved by: dense 4, sparse 5, hybrid 5, colbert 4
Section: Migrate to a New Embedding Model with Zero Downtime — Step 1: Create a New Collection
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — Step 1: Create a New Collection

The first step is to create a new collection in Qdrant that will be used to store the new
embeddings, compatible with the new model in terms of vector size and similarity function.
```python_code_1```
Now is also a good moment to consider changing any other settings for the collection, like custom sharding, replication factor, etc. Switching the model may be a good opportunity to improve the performance of your search.
The newly created collection is empty and ready to be used for storing the new embeddings.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 635
Retrieved by: dense 5, sparse 6, hybrid 6, colbert 2
Section: Migrate to a New Embedding Model with Zero Downtime — Step 5: Wrapping Up
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — Step 5: Wrapping Up

Once your application has switched to the new collection, disable the dual-write mode you implemented in Step 2. From now on, the application should only write to the new collection.
All searches are now performed using the new embeddings. If the old collection is no longer needed, you can safely delete it. To ensure you can roll back if necessary, keep a snapshot of the old collection.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 633
Retrieved by: dense 6, sparse 2, hybrid 4, colbert 6
Section: Migrate to a New Embedding Model with Zero Downtime — Step 3: Migrate the Existing Points into the New Collection
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — Step 3: Migrate the Existing Points into the New Collection

Now that you're in dual-write mode, it is time to migrate the existing points from the old collection to the new one. This can be done in a separate process that runs
in parallel with the regular upsert services.
The migration process reads the points from the old collection, re-embeds them using the new model, and writes them to the new collection, making sure not to overwrite existing points inserted by the update service. Here's an example of what the code for such a migration process could look like:
```python_code_1```
Breaking down this code step by step:
 Data is read from the old collection in batches of 100 points using a scroll. The `last_offset` variable keeps track of the scroll position in the collection.
 For each batch of points, the process re-embeds the vectors using the new embedding model. It assumes that the original text used for embedding is stored in the payload under the key `text`.
 With the re-embedded vectors, it prepares conditional upsert operations for the new collection, keeping the original IDs and payloads. The conditional upserts use a filter condition to ensure that a point is only inserted if it does not already exist in the new collection. The filter checks whether a point with the given ID already exists. A point is only upserted if the ID does not exist in the new collection. This prevents overwriting newer updates from the regular update service.
 Finally, the process uses a batch update to upsert the re-embedded points into the new collection. Note that it uses `batch_update_points` instead of `upsert`, because `batch_update_points` allows you to specify an update condition per upsert operation.
This kind of migration process can take some time, and the offset can be stored in a persistent way, so you can resume the migration process in case of a failure. You can use a database, a file, or any other persistent storage to keep track of the last offset. Having said that, because the conditional upserts would not overwrite any points in the new collection, you could safely restart the migration process from the beginning if needed.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 632
Retrieved by: dense 7, sparse 7, hybrid 7, colbert 7
Section: Migrate to a New Embedding Model with Zero Downtime — Step 2: Enable Dual Writes
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — Step 2: Enable Dual Writes

To ensure that both collections are kept up-to-date during the migration, you need to write any changes to both collections simultaneously. This way, any new data or updates to existing data are reflected in both collections.
Ideally, the data in Qdrant is updated by an update service reading from an update queue. This service is responsible for embedding the documents and writing them to Qdrant. It uses code similar to this:
```python_code_1```
To update the new collection, deploy a second service that updates the new collection in parallel with the existing one. This service uses the new embedding model to encode the documents and writes them to the new collection:
```python_code_2```
A good practice is to always ensure that both operations succeed. Any errors need to be handled on the client side. You could store errors in a log or "dead letter queue" for later processing. Transient errors can be retried at a later time. Other errors need to be analyzed and addressed accordingly.
If instead of update services, you have a monolithic application, you need to modify your application code to write to both collections simultaneously during the transition period. In your code, where you handle the embedding of the documents, you should add the logic to write to both collections.
Note that the method outlined in this tutorial only works for `upsert` operations. For example, a `delete` operation would fail on the new collection if a point does not exist yet, and that point would later be erroneously added by the migration process. If you use one of the following methods to modify points in your collection, you will need to pause those operations during the migration or implement additional logic to handle them:
 `.delete` removing specified points from the collection
 `.update_vectors` updating specified vectors on points
 `.delete_vectors` deleting specified vectors from points
 `.set_payload` setting payload values for specified points
 `.overwrite_payload` overwriting the entire payload of a specified point with a new payload
 `.delete_payload` deleting a specified key payload for points
 `.clear_payload` removing the entire payload for specified points
 `.batch_update_points` making batch updates to points, including their respective vectors and payloads
Please refer to the documentation of the SDK you are using, or the
HTTP/gRPC definitions, for the exact method names, as they may vary between languages.
After making these changes, you will be in a dual-write mode, where any change is written to both the old and new collection. This allows you to keep both collections up-to-date during the migration process.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 717
Retrieved by: dense 8, hybrid 10
Section: Nomic — Upsert using FastEmbed
--------------------------------------------------------------------------------

Nomic — Upsert using FastEmbed

```python_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 931
Retrieved by: dense 9, sparse 9, hybrid 8, colbert 8
Section: Frequently Asked Questions: General Topics — Vectors — Can I migrate my embeddings from another vector store to Qdrant?
--------------------------------------------------------------------------------

Frequently Asked Questions: General Topics — Vectors — Can I migrate my embeddings from another vector store to Qdrant?

Yes, Qdrant supports migration of embeddings from other vector stores, facilitating easy transitions and adoption of Qdrant’s features.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 748
Retrieved by: dense 10
Section: Snowflake — Embedding documents
--------------------------------------------------------------------------------

Snowflake — Embedding documents

```python_code_1```
```typescript_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 682
Retrieved by: sparse 8, hybrid 9
Section: Cohere — Embed v3
--------------------------------------------------------------------------------

Cohere — Embed v3

Embed v3 is a new family of Cohere models, released in November 2023. The new models require passing an additional
parameter to the API call: `input_type`. It determines the type of task you want to use the embeddings for.
 `input_type="search_document"` for documents to store in Qdrant
 `input_type="search_query"` for search queries to find the most relevant documents
 `input_type="classification"` for classification tasks
 `input_type="clustering"` for text clustering
While implementing semantic search applications, such as RAG, you should use `input_type="search_document"` for the
indexed documents and `input_type="search_query"` for the search queries. The following example shows how to index
documents with the Embed v3 model:
```python_code_1```
Once the documents are indexed, you can search for the most relevant documents using the Embed v3 model:
```python_code_2```
According to Cohere's documentation, all v3 models can use dot product, cosine similarity,
and Euclidean distance as the similarity metric, as all metrics return identical rankings.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 456
Retrieved by: sparse 10
Section: Inference — External Embedding Model Providers — OpenAI
--------------------------------------------------------------------------------

Inference — External Embedding Model Providers — OpenAI

When you prepend a model name with `openai/`, the embedding request is automatically routed to the OpenAI Embeddings API.
For example, to use OpenAI's `text-embedding-3-large` model when ingesting data, prepend the model name with `openai/` and provide your OpenAI API key in the `options` object. Any OpenAI-specific API parameters can be passed using the `options` object. This example uses the OpenAI-specific API `dimensions` parameter to reduce the dimensionality to 512:
{{}}
At query time, you can use the same model by prepending the model name with `openai/` and providing your OpenAI API key in the `options` object. This example again uses the OpenAI-specific API `dimensions` parameter to reduce the dimensionality to 512:
{{}}
Note that, because Qdrant does not store or cache your OpenAI API key, you need to provide it with each inference request.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 556
Retrieved by: colbert 9
Section: Airbyte — Setting up Qdrant as a destination — Embeddings
--------------------------------------------------------------------------------

Airbyte — Setting up Qdrant as a destination — Embeddings

You can choose the model that will be used to calculate the embeddings. Currently, Airbyte supports multiple
models, including OpenAI and Cohere.
Using some precomputed embeddings from your data source is also possible. In this case, you can pass the field
name containing the embeddings and their dimensionality.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 457
Retrieved by: colbert 10
Section: Inference — External Embedding Model Providers — Cohere
--------------------------------------------------------------------------------

Inference — External Embedding Model Providers — Cohere

Qdrant only supports version 2 of the Cohere Embed API.
When you prepend a model name with `cohere/`, the embedding request is automatically routed to the Cohere Embed API.
For example, to use Cohere's multimodal `embed-v4.0` model when ingesting data, prepend the model name with `cohere/` and provide your Cohere API key in the `options` object. This example uses the Cohere-specific API `output_dimension` parameter to reduce the dimensionality to 512:
{{}}
Note that the Cohere `embed-v4.0` model does not support passing an image as a URL. You need to provide a base64-encoded image as a Data URL.
At query time, you can use the same model by prepending the model name with `cohere/` and providing your Cohere API key in the `options` object. This example again uses the Cohere-specific API `output_dimension` parameter to reduce the dimensionality to 512:
{{}}
Note that, because Qdrant does not store or cache your Cohere API key, you need to provide it with each inference request.

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How to perform bulk operations on points?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 1357
Retrieved by: dense 1, sparse 1, hybrid 1, colbert 1
Section: Introduction
--------------------------------------------------------------------------------

Introduction

With this code snippet, you can perform batch operations on points like upserting, updating vectors, deleting vectors, setting, overwriting, deleting, and clearing payload data associated with points. The operations include inserting, updating, and deleting points along with their vectors and payload. Each operation is executed in order specified in the request payload.

```http_code_1```


```java_code_2```


```python_code_3```


```rust_code_4```


```typescript_code_5```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1707
Retrieved by: dense 2, sparse 2, hybrid 2, colbert 5
Section: N8N — Operations — Point
--------------------------------------------------------------------------------

N8N — Operations — Point

Upsert Points Insert or update points in a collection
 Retrieve Point Get a single point by ID
 Retrieve Points Get multiple points by their IDs
 Delete Points Remove points from a collection
 Count Points Count points in a collection with optional filtering
 Scroll Points Scroll through all points in a collection
 Batch Update Points Perform multiple point operations in a single request

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1459
Retrieved by: dense 3, sparse 9, hybrid 4, colbert 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

You can efficiently upload multiple points into Qdrant with a single API call using batching. This snippet demonstrates the process of creating new points with a batch operation. The batch contains IDs, payloads (such as color information), and vectors for each point. By grouping points together, you can reduce network connection overhead and improve performance.

```http_code_1```


```python_code_2```


```typescript_code_3```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 501
Retrieved by: dense 4, sparse 3, hybrid 3, colbert 3
Section: Points — Batch update
--------------------------------------------------------------------------------

Points — Batch update

_Available as of v1.5.0_
You can batch multiple point update operations. This includes inserting,
updating and deleting points, vectors and payload.
A batch update request consists of a list of operations. These are executed in
order. These operations can be batched:
 Upsert points: `upsert` or `UpsertOperation`
 Delete points: `delete_points` or `DeleteOperation`
 Update vectors: `update_vectors` or `UpdateVectorsOperation`
 Delete vectors: `delete_vectors` or `DeleteVectorsOperation`
 Set payload: `set_payload` or `SetPayloadOperation`
 Overwrite payload: `overwrite_payload` or `OverwritePayload`
 Delete payload: `delete_payload` or `DeletePayloadOperation`
 Clear payload: `clear_payload` or `ClearPayloadOperation`
The following example snippet makes use of all operations.
REST API (Schema):
{{}}
To batch many points with a single operation type, please use batching
functionality in that operation directly.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1709
Retrieved by: dense 5, hybrid 6, colbert 6
Section: N8N — Operations — Search
--------------------------------------------------------------------------------

N8N — Operations — Search

Query Points Search for similar vectors
 Query Points In Batch Perform multiple vector searches in batch
 Query Points Groups Group search results by payload field
 Matrix Pairs Calculate distance matrix between pairs of points
 Matrix Offsets Calculate distance matrix using offsets

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1708
Retrieved by: dense 6, hybrid 9
Section: N8N — Operations — Vector
--------------------------------------------------------------------------------

N8N — Operations — Vector

Update Vectors Update vectors for existing points
 Delete Vectors Remove vectors from points

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 497
Retrieved by: dense 7, hybrid 8
Section: Points — Retrieve points
--------------------------------------------------------------------------------

Points — Retrieve points

There is a method for retrieving points by their ids.
REST API (Schema):
{{}}
This method has additional parameters `with_vectors` and `with_payload`.
Using these parameters, you can select parts of the point you want as a result.
Excluding helps you not to waste traffic transmitting useless data.
The single point can also be retrieved via the API:
REST API (Schema):
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1461
Retrieved by: dense 8
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Inserts a list of points along with their IDs, payload data (such as color), and vector coordinates into a collection for storage or processing. The points are structured as objects with different attributes like ID, payload, and vector to represent properties of each point.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1470
Retrieved by: dense 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates how to insert multiple points with additional payload data into a collection. Each point is defined by an ID, a vector, and a payload containing information such as city names and prices. The `PUT` request is used to send this data to the server for storage or further processing.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 485
Retrieved by: dense 10
Section: Points — Upload points
--------------------------------------------------------------------------------

Points — Upload points

To optimize performance, Qdrant supports batch loading of points. I.e., you can load several points into the service in one API call.
Batching allows you to minimize the overhead of creating a network connection.
The Qdrant API supports two ways of creating batches record-oriented and column-oriented.
Internally, these options do not differ and are made only for the convenience of interaction.
Create points with batch:
{{}}
or record-oriented equivalent:
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 482
Retrieved by: sparse 4, hybrid 5
Section: Points
--------------------------------------------------------------------------------

Points

The points are the central entity that Qdrant operates with.
A point is a record consisting of a vector and an optional payload.
It looks like this:
```json_code_1```
You can search among the points grouped in one collection based on vector similarity.
This procedure is described in more detail in the search and filtering sections.
This section explains how to create and manage vectors.
Any point modification operation is asynchronous and takes place in 2 steps.
At the first stage, the operation is written to the Write-ahead-log.
After this moment, the service will not lose the data, even if the machine loses power supply.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1519
Retrieved by: sparse 5, hybrid 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet allows you to perform a search operation on a collection by specifying a filter condition based on a nested field. In this case, the search is filtering points where the `country.name` field matches the value "Germany". This enables you to retrieve scroll points that meet the specified criteria.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1592
Retrieved by: sparse 6, hybrid 7
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet represents an operation to update vectors associated with points in a collection. The operation uses a PUT request to update vectors for specific points by providing their IDs along with the new vector data. This method ensures that only the specified vectors are updated, while leaving any unspecified vectors unchanged. It is important to note that all the provided points must already exist in the collection for the update to be successful.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 496
Retrieved by: sparse 7
Section: Points — Conditional updates
--------------------------------------------------------------------------------

Points — Conditional updates

_Available as of v1.16.0_
All update operations (including point insertion, vector updates, payload updates, and deletions) support configurable pre-conditions based on filters.
{{}}
While conditional payload modification and deletion covers the use-case of mass data modification, conditional point insertion and vector updates are particularly useful for implementing optimistic concurrency control in distributed systems.
A common scenario for such mechanism is when multiple clients try to update the same point independently.
Consider the following sequence of events:
 Client A reads point P.
 Client B reads point P.
 Client A modifies point P and writes it back to Qdrant.
 Client B modifies point P (based on the stale data) and writes it back to Qdrant, unintentionally overwriting changes made by Client A.
To prevent such situations, Client B can use conditional updates.
For this, we would need to introduce an additional field in the payload, e.g. `version`, which would be incremented on each update.
When Client A writes back the modified point P, it would set the condition that the `version` field must be equal to the value it read initially.
If Client B tries to write back its changes later, the condition would fail (as the `version` has been incremented by Client A), and Qdrant would reject the update, preventing accidental overwrites.
Instead of `version`, applications can use timestamps (assuming synchronized clocks) or any other monotonically increasing value that fits their data model.
This mechanism is especially useful in the scenarios of embedding model migration, where we need to resolve conflicts between regular application updates and background re-embedding tasks.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1508
Retrieved by: sparse 8, colbert 8
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet showcases a context-based approach for performing a search operation on a collection of points. The search involves specifying positive and negative context points along with a limit on the number of results to be returned. By using a context score derived from the triplet-loss concept, the search is guided towards areas with fewer negative examples. This method allows for a more diverse and constrained result set, rather than only focusing on a single point. The approach can be utilized not just for general searching but also for recommendation systems by adapting it to specific use cases.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 620
Retrieved by: sparse 10, colbert 2
Section: Bulk Upload Vectors to a Qdrant Collection — Parallel upload into multiple shards
--------------------------------------------------------------------------------

Bulk Upload Vectors to a Qdrant Collection — Parallel upload into multiple shards

In Qdrant, each collection is split into shards. Each shard has a separate Write-Ahead-Log (WAL), which is responsible for ordering operations.
By creating multiple shards, you can parallelize upload of a large dataset. From 2 to 4 shards per one machine is a reasonable number.
```http_code_1```
```python_code_2```
```typescript_code_3```
```rust_code_4```
```java_code_5```
```csharp_code_6```
```go_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1228
Retrieved by: colbert 4
Section: Distributed deployment — Raft
--------------------------------------------------------------------------------

Distributed deployment — Raft

Qdrant uses the Raft consensus protocol to maintain consistency regarding the cluster topology and the collections structure.
Operations on points, on the other hand, do not go through the consensus infrastructure.
Qdrant is not intended to have strong transaction guarantees, which allows it to perform point operations with low overhead.
In practice, it means that Qdrant does not guarantee atomic distributed updates but allows you to wait until the operation is complete to see the results of your writes.
Operations on collections, on the contrary, are part of the consensus which guarantees that all operations are durable and eventually executed by all nodes.
In practice it means that a majority of nodes agree on what operations should be applied before the service will perform them.
Practically, it means that if the cluster is in a transition state either electing a new leader after a failure or starting up, the collection update operations will be denied.
You may use the cluster REST API to check the state of the consensus.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1229
Retrieved by: colbert 7
Section: Distributed deployment — Sharding
--------------------------------------------------------------------------------

Distributed deployment — Sharding

A Collection in Qdrant is made of one or more shards.
A shard is an independent store of points which is able to perform all operations provided by collections.
There are two methods of distributing points across shards:
 Automatic sharding: Points are distributed among shards by using a consistent hashing algorithm, so that shards are managing non-intersecting subsets of points. This is the default behavior.
 User-defined sharding: _Available as of v1.7.0_ Each point is uploaded to a specific shard, so that operations can hit only the shard or shards they need. Even with this distribution, shards still ensure having non-intersecting subsets of points. See more...
Each node knows where all parts of the collection are stored through the consensus protocol, so when you send a search request to one Qdrant node, it automatically queries all other nodes to obtain the full search result.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 618
Retrieved by: colbert 10
Section: Bulk Upload Vectors to a Qdrant Collection — Choose an Indexing Strategy — Disable indexing completely (`indexing_threshold: 0`)
--------------------------------------------------------------------------------

Bulk Upload Vectors to a Qdrant Collection — Choose an Indexing Strategy — Disable indexing completely (`indexing_threshold: 0`)

In case you are doing an initial upload of a large dataset, you might want to disable indexing during upload. It will enable to avoid unnecessary indexing of vectors, which will be overwritten by the next batch.
Setting `indexing_threshold` to `0` disables indexing altogether:
```http_code_1```
```python_code_2```
```typescript_code_3```
```rust_code_4```
```java_code_5```
```csharp_code_6```
```go_code_7```
With indexing_threshold set to 0, storage won't be optimized properly, which can lead to high RAM usage as segments accumulate in memory.
After upload is done, you can enable indexing by setting `indexing_threshold` to a desired value (default is 20000):
```http_code_8```
```python_code_9```
```typescript_code_10```
```rust_code_11```
```java_code_12```
```csharp_code_13```
```go_code_14```
At this point, Qdrant will begin indexing new and previously unindexed segments in the background.

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How does Qdrant handles versioning of data updates?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 1833
Retrieved by: dense 1, sparse 8, hybrid 2, colbert 4
Section: Managing a Qdrant Cluster — Upgrading the Qdrant version
--------------------------------------------------------------------------------

Managing a Qdrant Cluster — Upgrading the Qdrant version

To upgrade the Qdrant version of a database cluster, update the `version` field in the QdrantCluster spec. The Qdrant operator will automatically upgrade the cluster to the new version. The upgrade process is highly available on a multi-node cluster with replicated collections.
Note, that you should not skip minor versions when upgrading. For example, if you are running version `v1.11.3`, you can upgrade to `v1.11.5` or `v1.12.6`, but not directly to `v1.13.0`.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 297
Retrieved by: dense 2, sparse 3, hybrid 3, colbert 5
Section: Updating Qdrant Cloud Clusters
--------------------------------------------------------------------------------

Updating Qdrant Cloud Clusters

As soon as a new Qdrant version is available. Qdrant Cloud will show you an update notification in the Cluster list and on the Cluster details page.
To update to a new version, go to the Cluster Details page, choose the new version from the version dropdown and click Update.
If you are several versions behind, multiple updates might be required to reach the latest version. In this case, Qdrant Cloud will automatically perform the required intermediate updates to ensure a supported update path. You should still ensure that your client applications and used SKDs are compatible with the target version.
If you have a multi-node cluster and if your collections have a replication factor of at least 2, the update process will be zero-downtime and done in a rolling fashion. You will be able to use your database cluster normally.
If you have a single-node cluster or a collection with a replication factor of 1, the update process will require a short downtime period to restart your cluster with the new version.
See also Restart Mode for more details.
We advise taking a backup before updating to allow for rollbacks.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 541
Retrieved by: dense 3, sparse 1, hybrid 1, colbert 1
Section: Storage — Versioning
--------------------------------------------------------------------------------

Storage — Versioning

To ensure data integrity, Qdrant performs all data changes in 2 stages.
In the first step, the data is written to the Write-ahead-log(WAL), which orders all operations and assigns them a sequential number.
Once a change has been added to the WAL, it will not be lost even if a power loss occurs.
Then the changes go into the segments.
Each segment stores the last version of the change applied to it as well as the version of each individual point.
If the new change has a sequential number less than the current version of the point, the updater will ignore the change.
This mechanism allows Qdrant to safely and efficiently restore the storage from the WAL in case of an abnormal shutdown.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 475
Retrieved by: dense 4, sparse 4, hybrid 5, colbert 8
Section: Payload — Update payload
--------------------------------------------------------------------------------

Payload — Update payload

Updating payloads in Qdrant offers flexible methods to manage vector metadata. The set payload method updates specific fields while keeping others unchanged, while the overwrite method replaces the entire payload. Developers can also use clear payload to remove all metadata or delete fields to remove specific keys without affecting the rest. These options provide precise control for adapting to dynamic datasets.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1589
Retrieved by: dense 5, sparse 5, hybrid 6
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Update the collection with patch requests to put vector data on disk. This functionality allows you to specify vector parameters, such as setting vectors to be stored on disk, for a specific collection. In cases where the collection does not have named vectors, an empty name (`""`) should be used to perform this update. This feature provided by Qdrant version 1.4 enables modifications to collection parameters, including HNSW index, quantization, and disk configurations dynamically, without the need to recreate the collection. Additionally, segments containing index and quantized data will be automatically rebuilt in the background to align with the new parameters.

```bash_code_1```


```http_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 935
Retrieved by: dense 6, sparse 2, hybrid 4, colbert 2
Section: Frequently Asked Questions: General Topics — Search — How does Qdrant handle real-time data updates and search?
--------------------------------------------------------------------------------

Frequently Asked Questions: General Topics — Search — How does Qdrant handle real-time data updates and search?

Qdrant supports live updates for vector data, with newly inserted, updated and deleted vectors available for immediate search. The system uses full-scan search on unindexed segments during background index updates.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 632
Retrieved by: dense 7, sparse 6, hybrid 7
Section: Migrate to a New Embedding Model with Zero Downtime — Step 2: Enable Dual Writes
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — Step 2: Enable Dual Writes

To ensure that both collections are kept up-to-date during the migration, you need to write any changes to both collections simultaneously. This way, any new data or updates to existing data are reflected in both collections.
Ideally, the data in Qdrant is updated by an update service reading from an update queue. This service is responsible for embedding the documents and writing them to Qdrant. It uses code similar to this:
```python_code_1```
To update the new collection, deploy a second service that updates the new collection in parallel with the existing one. This service uses the new embedding model to encode the documents and writes them to the new collection:
```python_code_2```
A good practice is to always ensure that both operations succeed. Any errors need to be handled on the client side. You could store errors in a log or "dead letter queue" for later processing. Transient errors can be retried at a later time. Other errors need to be analyzed and addressed accordingly.
If instead of update services, you have a monolithic application, you need to modify your application code to write to both collections simultaneously during the transition period. In your code, where you handle the embedding of the documents, you should add the logic to write to both collections.
Note that the method outlined in this tutorial only works for `upsert` operations. For example, a `delete` operation would fail on the new collection if a point does not exist yet, and that point would later be erroneously added by the migration process. If you use one of the following methods to modify points in your collection, you will need to pause those operations during the migration or implement additional logic to handle them:
 `.delete` removing specified points from the collection
 `.update_vectors` updating specified vectors on points
 `.delete_vectors` deleting specified vectors from points
 `.set_payload` setting payload values for specified points
 `.overwrite_payload` overwriting the entire payload of a specified point with a new payload
 `.delete_payload` deleting a specified key payload for points
 `.clear_payload` removing the entire payload for specified points
 `.batch_update_points` making batch updates to points, including their respective vectors and payloads
Please refer to the documentation of the SDK you are using, or the
HTTP/gRPC definitions, for the exact method names, as they may vary between languages.
After making these changes, you will be in a dual-write mode, where any change is written to both the old and new collection. This allows you to keep both collections up-to-date during the migration process.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 656
Retrieved by: dense 8, hybrid 10
Section: Migration — Why use this instead of Qdrant’s Native Snapshotting?
--------------------------------------------------------------------------------

Migration — Why use this instead of Qdrant’s Native Snapshotting?

Qdrant supports snapshot-based backups, low-level disk operations built for same cluster recovery or local backups. These snapshots:
* Require snapshot consistency across nodes.
* Can be hard to port across machines or cloud zones.
On the other hand, the Qdrant Migration Tool:
* Streams data in live batches.
* Can resume interrupted migrations.
* Works even when data is being inserted.
* Supports collection reconfiguration (e.g., change replication, and quantization)
* Supports migrating from other vector DBs (Pinecone, Chroma, Weaviate, etc.)

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1597
Retrieved by: dense 9, hybrid 9
Section: Configure, Scale & Update Qdrant Hybrid Cloud Clusters — Update Clusters
--------------------------------------------------------------------------------

Configure, Scale & Update Qdrant Hybrid Cloud Clusters — Update Clusters

You can update the version of your cluster at any time. For more details see Update Clusters.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1652
Retrieved by: dense 10
Section: Further Reading
--------------------------------------------------------------------------------

Further Reading

Getting started with Datadog
 Qdrant integration source

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1242
Retrieved by: sparse 7, hybrid 8, colbert 7
Section: Distributed deployment — Consistency guarantees
--------------------------------------------------------------------------------

Distributed deployment — Consistency guarantees

By default, Qdrant focuses on availability and maximum throughput of search operations.
For the majority of use cases, this is a preferable trade-off.
During the normal state of operation, it is possible to search and modify data from any peers in the cluster.
Before responding to the client, the peer handling the request dispatches all operations according to the current topology in order to keep the data synchronized across the cluster.
 reads are using a partial fan-out strategy to optimize latency and availability
 writes are executed in parallel on all active sharded replicas
By default, concurrent updates on one point can result in an inconsistent state. For example, if two clients simultaneously update the same point in a collection with three replicas per shard. On some replicas, the point may reflect the update from one client, while on other replicas, the point may reflect the update from the other client.
In some cases, it is necessary to ensure additional guarantees during possible hardware instabilities, mass concurrent updates of same documents, etc.
Qdrant provides a few options to control consistency guarantees:
 `write_consistency_factor` defines the number of replicas that must acknowledge a write operation before responding to the client. Increasing this value will make write operations tolerant to network partitions in the cluster, but will require a higher number of replicas to be active to perform write operations.
 Read `consistency` param, can be used with search and retrieve operations to ensure that the results obtained from all replicas are the same. If this option is used, Qdrant will perform the read operation on multiple replicas and resolve the result according to the selected strategy. This option is useful to avoid data inconsistency in case of concurrent updates of the same documents. This options is preferred if the update operations are frequent and the number of replicas is low.
 Write `ordering` param, can be used with update and delete operations to ensure that the operations are executed in the same order on all replicas. If this option is used, Qdrant will route the operation to the leader replica of the shard and wait for the response before responding to the client. This option is useful to avoid data inconsistency in case of concurrent updates of the same documents. This options is preferred if read operations are more frequent than update and if search performance is critical.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1881
Retrieved by: sparse 9
Section: Qdrant on Databricks
--------------------------------------------------------------------------------

Qdrant on Databricks

Databricks is a unified analytics platform for working with big data and AI. It's built around Apache Spark, a powerful open-source distributed computing system well-suited for processing large-scale datasets and performing complex analytics tasks.
Apache Spark is designed to scale horizontally, meaning it can handle expensive operations like generating vector embeddings by distributing computation across a cluster of machines. This scalability is crucial when dealing with large datasets.
In this example, we will demonstrate how to vectorize a dataset with dense and sparse embeddings using Qdrant's FastEmbed library. We will then load this vectorized data into a Qdrant cluster using the Qdrant Spark connector on Databricks.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 235
Retrieved by: sparse 10, colbert 10
Section: Build a Hybrid Search Service with FastEmbed and Qdrant — Run Qdrant in Docker
--------------------------------------------------------------------------------

Build a Hybrid Search Service with FastEmbed and Qdrant — Run Qdrant in Docker

Next, you need to manage all of your data using a vector engine. Qdrant lets you store, update or delete created vectors. Most importantly, it lets you search for the nearest vectors via a convenient API.
> Note: Before you begin, create a project directory and a virtual python environment in it.
1. Download the Qdrant image from DockerHub.
```bash_code_1```
2. Start Qdrant inside of Docker.
```bash_code_2```
You should see output like this
```text_code_3```
Test the service by going to the local Qdrant dashboard. You should see the Qdrant version info in your browser.
All data uploaded to Qdrant is saved inside the `./qdrant_storage` directory and will be persisted even if you recreate the container.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 461
Retrieved by: colbert 3
Section: Optimizer
--------------------------------------------------------------------------------

Optimizer

It is much more efficient to apply changes in batches than perform each change individually, as many other databases do. Qdrant here is no exception. Since Qdrant operates with data structures that are not always easy to change, it is sometimes necessary to rebuild those structures completely.
Storage optimization in Qdrant occurs at the segment level (see storage).
In this case, the segment to be optimized remains readable for the time of the rebuild.
The availability is achieved by wrapping the segment into a proxy that transparently handles data changes.
Changed data is placed in the copy-on-write segment, which has priority for retrieval and subsequent updates.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 496
Retrieved by: colbert 6
Section: Points — Conditional updates
--------------------------------------------------------------------------------

Points — Conditional updates

_Available as of v1.16.0_
All update operations (including point insertion, vector updates, payload updates, and deletions) support configurable pre-conditions based on filters.
{{}}
While conditional payload modification and deletion covers the use-case of mass data modification, conditional point insertion and vector updates are particularly useful for implementing optimistic concurrency control in distributed systems.
A common scenario for such mechanism is when multiple clients try to update the same point independently.
Consider the following sequence of events:
 Client A reads point P.
 Client B reads point P.
 Client A modifies point P and writes it back to Qdrant.
 Client B modifies point P (based on the stale data) and writes it back to Qdrant, unintentionally overwriting changes made by Client A.
To prevent such situations, Client B can use conditional updates.
For this, we would need to introduce an additional field in the payload, e.g. `version`, which would be incremented on each update.
When Client A writes back the modified point P, it would set the condition that the `version` field must be equal to the value it read initially.
If Client B tries to write back its changes later, the condition would fail (as the `version` has been incremented by Client A), and Qdrant would reject the update, preventing accidental overwrites.
Instead of `version`, applications can use timestamps (assuming synchronized clocks) or any other monotonically increasing value that fits their data model.
This mechanism is especially useful in the scenarios of embedding model migration, where we need to resolve conflicts between regular application updates and background re-embedding tasks.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 243
Retrieved by: colbert 9
Section: Build a Neural Search Service with Sentence Transformers and Qdrant — Run Qdrant in Docker
--------------------------------------------------------------------------------

Build a Neural Search Service with Sentence Transformers and Qdrant — Run Qdrant in Docker

Next, you need to manage all of your data using a vector engine. Qdrant lets you store, update or delete created vectors. Most importantly, it lets you search for the nearest vectors via a convenient API.
> Note: Before you begin, create a project directory and a virtual python environment in it.
1. Download the Qdrant image from DockerHub.
```bash_code_1```
2. Start Qdrant inside of Docker.
```bash_code_2```
You should see output like this
```text_code_3```
Test the service by going to the local Qdrant dashboard. You should see the Qdrant version info in your browser.
All data uploaded to Qdrant is saved inside the `./qdrant_storage` directory and will be persisted even if you recreate the container.

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How to change existing data in Qdrant?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 1589
Retrieved by: dense 1, hybrid 2
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Update the collection with patch requests to put vector data on disk. This functionality allows you to specify vector parameters, such as setting vectors to be stored on disk, for a specific collection. In cases where the collection does not have named vectors, an empty name (`""`) should be used to perform this update. This feature provided by Qdrant version 1.4 enables modifications to collection parameters, including HNSW index, quantization, and disk configurations dynamically, without the need to recreate the collection. Additionally, segments containing index and quantized data will be automatically rebuilt in the background to align with the new parameters.

```bash_code_1```


```http_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 598
Retrieved by: dense 2, hybrid 4
Section: Further Reading
--------------------------------------------------------------------------------

Further Reading

Getting started with Connect
 Qdrant Output Reference

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1137
Retrieved by: dense 3, hybrid 6
Section: NLWeb — Usage — Configuring Qdrant
--------------------------------------------------------------------------------

NLWeb — Usage — Configuring Qdrant

To use Qdrant, update your configuration.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 475
Retrieved by: dense 4, hybrid 7
Section: Payload — Update payload
--------------------------------------------------------------------------------

Payload — Update payload

Updating payloads in Qdrant offers flexible methods to manage vector metadata. The set payload method updates specific fields while keeping others unchanged, while the overwrite method replaces the entire payload. Developers can also use clear payload to remove all metadata or delete fields to remove specific keys without affecting the rest. These options provide precise control for adapting to dynamic datasets.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 592
Retrieved by: dense 5, hybrid 9
Section: Usage with Qdrant — Running
--------------------------------------------------------------------------------

Usage with Qdrant — Running

```console_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 632
Retrieved by: dense 6, sparse 1, hybrid 1, colbert 3
Section: Migrate to a New Embedding Model with Zero Downtime — Step 2: Enable Dual Writes
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — Step 2: Enable Dual Writes

To ensure that both collections are kept up-to-date during the migration, you need to write any changes to both collections simultaneously. This way, any new data or updates to existing data are reflected in both collections.
Ideally, the data in Qdrant is updated by an update service reading from an update queue. This service is responsible for embedding the documents and writing them to Qdrant. It uses code similar to this:
```python_code_1```
To update the new collection, deploy a second service that updates the new collection in parallel with the existing one. This service uses the new embedding model to encode the documents and writes them to the new collection:
```python_code_2```
A good practice is to always ensure that both operations succeed. Any errors need to be handled on the client side. You could store errors in a log or "dead letter queue" for later processing. Transient errors can be retried at a later time. Other errors need to be analyzed and addressed accordingly.
If instead of update services, you have a monolithic application, you need to modify your application code to write to both collections simultaneously during the transition period. In your code, where you handle the embedding of the documents, you should add the logic to write to both collections.
Note that the method outlined in this tutorial only works for `upsert` operations. For example, a `delete` operation would fail on the new collection if a point does not exist yet, and that point would later be erroneously added by the migration process. If you use one of the following methods to modify points in your collection, you will need to pause those operations during the migration or implement additional logic to handle them:
 `.delete` removing specified points from the collection
 `.update_vectors` updating specified vectors on points
 `.delete_vectors` deleting specified vectors from points
 `.set_payload` setting payload values for specified points
 `.overwrite_payload` overwriting the entire payload of a specified point with a new payload
 `.delete_payload` deleting a specified key payload for points
 `.clear_payload` removing the entire payload for specified points
 `.batch_update_points` making batch updates to points, including their respective vectors and payloads
Please refer to the documentation of the SDK you are using, or the
HTTP/gRPC definitions, for the exact method names, as they may vary between languages.
After making these changes, you will be in a dual-write mode, where any change is written to both the old and new collection. This allows you to keep both collections up-to-date during the migration process.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1138
Retrieved by: dense 7
Section: NLWeb — Usage — Configuring Qdrant — 1. Copy and edit the environment variables file
--------------------------------------------------------------------------------

NLWeb — Usage — Configuring Qdrant — 1. Copy and edit the environment variables file

```bash_code_1```
Ensure the following values are set in your `.env` file:
```text_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1841
Retrieved by: dense 8, colbert 5
Section: Managing a Qdrant Cluster — Resharding
--------------------------------------------------------------------------------

Managing a Qdrant Cluster — Resharding

In Qdrant Cloud, you can change the number of shards in your existing collections without having to recreate the collection from scratch. This feature is called resharding and allows you to scale your collections up or down as needed. For more details see Resharding.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1216
Retrieved by: dense 9
Section: Configuration
--------------------------------------------------------------------------------

Configuration

Qdrant ships with sensible defaults for collection and network settings that are suitable for most use cases. You can view these defaults in the Qdrant source. If you need to customize the settings, you can do so using configuration files and environment variables.
 Qdrant Cloud does not allow modifying the Qdrant configuration.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1652
Retrieved by: dense 10
Section: Further Reading
--------------------------------------------------------------------------------

Further Reading

Getting started with Datadog
 Qdrant integration source

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 541
Retrieved by: sparse 2, hybrid 3, colbert 1
Section: Storage — Versioning
--------------------------------------------------------------------------------

Storage — Versioning

To ensure data integrity, Qdrant performs all data changes in 2 stages.
In the first step, the data is written to the Write-ahead-log(WAL), which orders all operations and assigns them a sequential number.
Once a change has been added to the WAL, it will not be lost even if a power loss occurs.
Then the changes go into the segments.
Each segment stores the last version of the change applied to it as well as the version of each individual point.
If the new change has a sequential number less than the current version of the point, the updater will ignore the change.
This mechanism allows Qdrant to safely and efficiently restore the storage from the WAL in case of an abnormal shutdown.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 461
Retrieved by: sparse 3, hybrid 5, colbert 2
Section: Optimizer
--------------------------------------------------------------------------------

Optimizer

It is much more efficient to apply changes in batches than perform each change individually, as many other databases do. Qdrant here is no exception. Since Qdrant operates with data structures that are not always easy to change, it is sometimes necessary to rebuild those structures completely.
Storage optimization in Qdrant occurs at the segment level (see storage).
In this case, the segment to be optimized remains readable for the time of the rebuild.
The availability is achieved by wrapping the segment into a proxy that transparently handles data changes.
Changed data is placed in the copy-on-write segment, which has priority for retrieval and subsequent updates.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1882
Retrieved by: sparse 4, hybrid 8
Section: Qdrant on Databricks — Setting up a Databricks project
--------------------------------------------------------------------------------

Qdrant on Databricks — Setting up a Databricks project

Set up a Databricks cluster following the official documentation guidelines.
 Install the Qdrant Spark connector as a library:
 Navigate to the `Libraries` section in your cluster dashboard.
 Click on `Install New` at the top-right to open the library installation modal.
 Search for `io.qdrant:spark:VERSION` in the Maven packages and click on `Install`.
 Create a new Databricks notebook on your cluster to begin working with your data and libraries.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1356
Retrieved by: sparse 5, hybrid 10
Section: Usage statistics — Request information deletion
--------------------------------------------------------------------------------

Usage statistics — Request information deletion

We provide an email address so that users can request the complete removal of their data from all of our tools.
To do so, send an email to privacy@qdrant.com containing the unique identifier generated for your Qdrant installation.
You can find this identifier in the telemetry API response (`"id"` field), or in the logs of your Qdrant instance.
Any questions regarding the management of the data we collect can also be sent to this email address.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 105
Retrieved by: sparse 6
Section: Send S3 Data to Qdrant Vector Store with LangChain — Step 4: Visualizing Data in Qdrant WebUI
--------------------------------------------------------------------------------

Send S3 Data to Qdrant Vector Store with LangChain — Step 4: Visualizing Data in Qdrant WebUI

To start visualizing your data in the Qdrant WebUI, head to the Overview section and select Access the database.
Figure 2: Accessing the Database from the Qdrant UI
When prompted, enter your API key. Once inside, you’ll be able to view your collections and the corresponding data points. You should see your collection displayed like this:
Figure 3: The product-data Collection in Qdrant
Here’s a look at the most recent point ingested into Qdrant:
Figure 4: The Latest Point Added to the product-data Collection
The Qdrant WebUI’s search functionality allows you to perform vector searches across your collections. With options to apply filters and parameters, retrieving relevant embeddings and exploring relationships within your data becomes easy. To start, head over to the Console in the left panel, where you can create queries:
Figure 5: Overview of Console in Qdrant
The first query retrieves all collections, the second fetches points from the product-data collection, and the third performs a sample query. This demonstrates how straightforward it is to interact with your data in the Qdrant UI.
Now, let’s retrieve some documents from the database using a query!.
Figure 6: Querying the Qdrant Client to Retrieve Relevant Documents
In this example, we queried Phones with improved design. Then, we converted the text to vectors using OpenAI and retrieved a relevant phone review highlighting design improvements.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 673
Retrieved by: sparse 7, colbert 7
Section: Qdrant Edge Quickstart — Load Existing Edge Shard from Disk
--------------------------------------------------------------------------------

Qdrant Edge Quickstart — Load Existing Edge Shard from Disk

After closing an Edge Shard, you can reopen it by loading its data and configuration from disk. Create a new `EdgeShard` instance with the storage directory and provide `None` for the configuration:
```python_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1881
Retrieved by: sparse 8
Section: Qdrant on Databricks
--------------------------------------------------------------------------------

Qdrant on Databricks

Databricks is a unified analytics platform for working with big data and AI. It's built around Apache Spark, a powerful open-source distributed computing system well-suited for processing large-scale datasets and performing complex analytics tasks.
Apache Spark is designed to scale horizontally, meaning it can handle expensive operations like generating vector embeddings by distributing computation across a cluster of machines. This scalability is crucial when dealing with large datasets.
In this example, we will demonstrate how to vectorize a dataset with dense and sparse embeddings using Qdrant's FastEmbed library. We will then load this vectorized data into a Qdrant cluster using the Qdrant Spark connector on Databricks.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1879
Retrieved by: sparse 9
Section: Setup Data Streaming with Kafka via Confluent — Playground Application
--------------------------------------------------------------------------------

Setup Data Streaming with Kafka via Confluent — Playground Application

As the infrastructure set is completely done, now it's time for us to create a simple application and check our setup. the objective of our application is the data is inserted to Mongodb and eventually it will get ingested into Qdrant also using Change Data Capture (CDC).
`requirements.txt`
```bash_code_1```
`project_root_folder/main.py`
This is just sample code. Nevertheless it can be extended to millions of operations based on your use case.
```python_code_2```
`project_root_folder/utils/app_utils.py`
```python_code_3```
Before we run the application, below is the state of MongoDB and Qdrant databases.
Figure 3: Initial state: no collection named `test` & `no data` in the `docs` collection of MongodDB.
Once you run the code the data goes into Mongodb and the CDC gets triggered and eventually Qdrant will receive this data.
Figure 4: The test Qdrant collection is created automatically.
Figure 5: Data is inserted into both MongoDB and Qdrant.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1227
Retrieved by: sparse 10, colbert 6
Section: Distributed deployment — Making use of a new distributed Qdrant cluster
--------------------------------------------------------------------------------

Distributed deployment — Making use of a new distributed Qdrant cluster

When you enable distributed mode and scale up to two or more nodes, your data does not move to the new node automatically; it starts out empty. To make use of your new empty node, do one of the following:
* Create a new replicated collection by setting the replication_factor to 2 or more and setting the number of shards to a multiple of your number of nodes.
* If you have an existing collection which does not contain enough shards for each node, you must create a new collection as described in the previous bullet point.
* If you already have enough shards for each node, and you merely need to replicate your data, follow the directions for creating new shard replicas.
* If you already have enough shards for each node, and your data is already replicated, you can move data (without replicating it) onto the new node(s) by moving shards.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1596
Retrieved by: colbert 4
Section: Configure, Scale & Update Qdrant Hybrid Cloud Clusters — Scale Clusters — Resharding
--------------------------------------------------------------------------------

Configure, Scale & Update Qdrant Hybrid Cloud Clusters — Scale Clusters — Resharding

In Qdrant Cloud, you can change the number of shards in your existing collections without having to recreate the collection from scratch. This feature is called resharding and allows you to scale your collections up or down as needed. For more details see Resharding.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 527
Retrieved by: colbert 8
Section: Snapshots — Restore snapshot — Snapshot priority
--------------------------------------------------------------------------------

Snapshots — Restore snapshot — Snapshot priority

When recovering a snapshot to a non-empty node, there may be conflicts between the snapshot data and the existing data. The "priority" setting controls how Qdrant handles these conflicts. The priority setting is important because different priorities can give very
different end results. The default priority may not be best for all situations.
The available snapshot recovery priorities are:
 `replica`: _(default)_ prefer existing data over the snapshot.
 `snapshot`: prefer snapshot data over existing data.
 `no_sync`: restore snapshot without any additional synchronization.
To recover a new collection from a snapshot, you need to set
the priority to `snapshot`. With `snapshot` priority, all data from the snapshot
will be recovered onto the cluster. With `replica` priority _(default)_, you'd
end up with an empty collection because the collection on the cluster did not
contain any points and that source was preferred.
`no_sync` is for specialized use cases and is not commonly used. It allows
managing shards and transferring shards between clusters manually without any
additional synchronization. Using it incorrectly will leave your cluster in a
broken state.
To recover from a URL, you specify an additional parameter in the request body:
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 550
Retrieved by: colbert 9
Section: Vectors — Quantization
--------------------------------------------------------------------------------

Vectors — Quantization

Apart from changing the datatype of the original vectors, Qdrant can create quantized representations of vectors alongside the original ones.
This quantized representation can be used to quickly select candidates for rescoring with the original vectors or even used directly for search.
Quantization is applied in the background, during the optimization process.
More information about the quantization process can be found in the Quantization section.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 631
Retrieved by: colbert 10
Section: Migrate to a New Embedding Model with Zero Downtime — Step 1: Create a New Collection
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — Step 1: Create a New Collection

The first step is to create a new collection in Qdrant that will be used to store the new
embeddings, compatible with the new model in terms of vector size and similarity function.
```python_code_1```
Now is also a good moment to consider changing any other settings for the collection, like custom sharding, replication factor, etc. Switching the model may be a good opportunity to improve the performance of your search.
The newly created collection is empty and ready to be used for storing the new embeddings.

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How are vector updates precessed internally?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 1708
Retrieved by: dense 1, hybrid 3
Section: N8N — Operations — Vector
--------------------------------------------------------------------------------

N8N — Operations — Vector

Update Vectors Update vectors for existing points
 Delete Vectors Remove vectors from points

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 496
Retrieved by: dense 2, sparse 1, hybrid 1, colbert 1
Section: Points — Conditional updates
--------------------------------------------------------------------------------

Points — Conditional updates

_Available as of v1.16.0_
All update operations (including point insertion, vector updates, payload updates, and deletions) support configurable pre-conditions based on filters.
{{}}
While conditional payload modification and deletion covers the use-case of mass data modification, conditional point insertion and vector updates are particularly useful for implementing optimistic concurrency control in distributed systems.
A common scenario for such mechanism is when multiple clients try to update the same point independently.
Consider the following sequence of events:
 Client A reads point P.
 Client B reads point P.
 Client A modifies point P and writes it back to Qdrant.
 Client B modifies point P (based on the stale data) and writes it back to Qdrant, unintentionally overwriting changes made by Client A.
To prevent such situations, Client B can use conditional updates.
For this, we would need to introduce an additional field in the payload, e.g. `version`, which would be incremented on each update.
When Client A writes back the modified point P, it would set the condition that the `version` field must be equal to the value it read initially.
If Client B tries to write back its changes later, the condition would fail (as the `version` has been incremented by Client A), and Qdrant would reject the update, preventing accidental overwrites.
Instead of `version`, applications can use timestamps (assuming synchronized clocks) or any other monotonically increasing value that fits their data model.
This mechanism is especially useful in the scenarios of embedding model migration, where we need to resolve conflicts between regular application updates and background re-embedding tasks.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1592
Retrieved by: dense 3, sparse 2, hybrid 2, colbert 4
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet represents an operation to update vectors associated with points in a collection. The operation uses a PUT request to update vectors for specific points by providing their IDs along with the new vector data. This method ensures that only the specified vectors are updated, while leaving any unspecified vectors unchanged. It is important to note that all the provided points must already exist in the collection for the update to be successful.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1357
Retrieved by: dense 4, hybrid 8
Section: Introduction
--------------------------------------------------------------------------------

Introduction

With this code snippet, you can perform batch operations on points like upserting, updating vectors, deleting vectors, setting, overwriting, deleting, and clearing payload data associated with points. The operations include inserting, updating, and deleting points along with their vectors and payload. Each operation is executed in order specified in the request payload.

```http_code_1```


```java_code_2```


```python_code_3```


```rust_code_4```


```typescript_code_5```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 935
Retrieved by: dense 5, hybrid 9
Section: Frequently Asked Questions: General Topics — Search — How does Qdrant handle real-time data updates and search?
--------------------------------------------------------------------------------

Frequently Asked Questions: General Topics — Search — How does Qdrant handle real-time data updates and search?

Qdrant supports live updates for vector data, with newly inserted, updated and deleted vectors available for immediate search. The system uses full-scan search on unindexed segments during background index updates.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1586
Retrieved by: dense 6
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates updating HNSW index and quantization parameters for a collection, as well as for a specific vector within the collection called `my_vector`. The values like `m`, `ef_construct`, compression type, and quantization settings are adjusted for optimization.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1589
Retrieved by: dense 7, sparse 4, hybrid 5, colbert 7
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Update the collection with patch requests to put vector data on disk. This functionality allows you to specify vector parameters, such as setting vectors to be stored on disk, for a specific collection. In cases where the collection does not have named vectors, an empty name (`""`) should be used to perform this update. This feature provided by Qdrant version 1.4 enables modifications to collection parameters, including HNSW index, quantization, and disk configurations dynamically, without the need to recreate the collection. Additionally, segments containing index and quantized data will be automatically rebuilt in the background to align with the new parameters.

```bash_code_1```


```http_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 364
Retrieved by: dense 8, sparse 7, hybrid 6, colbert 3
Section: Collections — Update collection parameters — Update vector parameters
--------------------------------------------------------------------------------

Collections — Update collection parameters — Update vector parameters

Available as of v1.4.0
To update vector parameters using the collection update API, you must always specify a vector name. If your collection does not have named vectors, use an empty ("") name.
Qdrant 1.4 adds support for updating more collection parameters at runtime. HNSW
index, quantization and disk configurations can now be changed without
recreating a collection. Segments (with index and quantized data) will
automatically be rebuilt in the background to match updated parameters.
To put vector data on disk for a collection that does not have named vectors,
use `""` as name:
{{}}
To put vector data on disk for a collection that does have named vectors:
Note: To create a vector name, follow the procedure from our Points.
{{}}
In the following example the HNSW index and quantization parameters are updated,
both for the whole collection, and for `my_vector` specifically:
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1730
Retrieved by: dense 9
Section: Vectorize.io — Further Reading
--------------------------------------------------------------------------------

Vectorize.io — Further Reading

Vectorize Documentation
 Vectorize Tutorials.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 363
Retrieved by: dense 10, sparse 3, hybrid 4, colbert 6
Section: Collections — Update collection parameters
--------------------------------------------------------------------------------

Collections — Update collection parameters

Dynamic parameter updates may be helpful, for example, for more efficient initial loading of vectors.
For example, you can disable indexing during the upload process, and enable it immediately after the upload is finished.
As a result, you will not waste extra computation resources on rebuilding the index.
The following command enables indexing for segments that have more than 10000 kB of vectors stored:
{{}}
The following parameters can be updated:
* `optimizers_config` see optimizer for details.
* `hnsw_config` see indexing for details.
* `quantization_config` see quantization for details.
* `vectors_config` vector-specific configuration, including individual `hnsw_config`, `quantization_config` and `on_disk` settings.
* `params` other collection parameters, including `write_consistency_factor` and `on_disk_payload`.
* `strict_mode_config` see strict mode for details.
Full API specification is available in schema definitions.
Calls to this endpoint may be blocking as it waits for existing optimizers to
finish. We recommended against using this in a production database as it may
introduce huge overhead due to the rebuilding of the index.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1590
Retrieved by: sparse 5, hybrid 7, colbert 5
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Update the collection by setting the vectors to be saved on disk for a specific vector named 'my_vector'. This code snippet demonstrates the configuration to ensure that the vector data is saved on disk within the collection.

```bash_code_1```


```http_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 475
Retrieved by: sparse 6, colbert 8
Section: Payload — Update payload
--------------------------------------------------------------------------------

Payload — Update payload

Updating payloads in Qdrant offers flexible methods to manage vector metadata. The set payload method updates specific fields while keeping others unchanged, while the overwrite method replaces the entire payload. Developers can also use clear payload to remove all metadata or delete fields to remove specific keys without affecting the rest. These options provide precise control for adapting to dynamic datasets.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1587
Retrieved by: sparse 8, hybrid 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Update collection parameters to adjust the optimizer's configuration. In this case, the code snippet demonstrates how to patch the collection by setting an indexing threshold of 10000 for more efficient initial loading of vectors. This allows you to optimize resource usage by enabling indexing selectively based on the number of vectors stored in each segment.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 492
Retrieved by: sparse 9, colbert 10
Section: Points — Modify points — Update vectors
--------------------------------------------------------------------------------

Points — Modify points — Update vectors

_Available as of v1.2.0_
This method updates the specified vectors on the given points. Unspecified
vectors are kept unchanged. All given points must exist.
REST API (Schema):
{{}}
To update points and replace all of its vectors, see uploading
points.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1460
Retrieved by: sparse 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet represents a functionality to update points in a collection. In this instance, it updates a point with id 1 by changing its payload to have a color of "red" and its vector coordinates to [0.9, 0.1, 0.1].

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 367
Retrieved by: colbert 2
Section: Collections — Collection info — Approximate point and vector counts
--------------------------------------------------------------------------------

Collections — Collection info — Approximate point and vector counts

You may be interested in the count attributes:
 `points_count` total number of objects (vectors and their payloads) stored in the collection
 `indexed_vectors_count` total number of vectors stored in the HNSW or sparse index. Qdrant does not store all the vectors in the index, but only if an index segment might be created for a given configuration.
The above counts are not exact, but should be considered approximate. Depending
on how you use Qdrant these may give very different numbers than what you may
expect. It's therefore important not to rely on them.
More specifically, these numbers represent the count of points and vectors in
Qdrant's internal storage. Internally, Qdrant may temporarily duplicate points
as part of automatic optimizations. It may keep changed or deleted points for a
bit. And it may delay indexing of new points. All of that is for optimization
reasons.
Updates you do are therefore not directly reflected in these numbers. If you see
a wildly different count of points, it will likely resolve itself once a new
round of automatic optimizations is completed.
To clarify: these numbers don't represent the exact amount of points or vectors
you have inserted, nor does it represent the exact number of distinguishable
points or vectors you can query. If you want to know exact counts, refer to the
count API.
_Note: these numbers may be removed in a future version of Qdrant._

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 501
Retrieved by: colbert 9
Section: Points — Batch update
--------------------------------------------------------------------------------

Points — Batch update

_Available as of v1.5.0_
You can batch multiple point update operations. This includes inserting,
updating and deleting points, vectors and payload.
A batch update request consists of a list of operations. These are executed in
order. These operations can be batched:
 Upsert points: `upsert` or `UpsertOperation`
 Delete points: `delete_points` or `DeleteOperation`
 Update vectors: `update_vectors` or `UpdateVectorsOperation`
 Delete vectors: `delete_vectors` or `DeleteVectorsOperation`
 Set payload: `set_payload` or `SetPayloadOperation`
 Overwrite payload: `overwrite_payload` or `OverwritePayload`
 Delete payload: `delete_payload` or `DeletePayloadOperation`
 Clear payload: `clear_payload` or `ClearPayloadOperation`
The following example snippet makes use of all operations.
REST API (Schema):
{{}}
To batch many points with a single operation type, please use batching
functionality in that operation directly.

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How does Qdrant manage metadata?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 369
Retrieved by: dense 1, sparse 2, hybrid 2, colbert 2
Section: Collections — Collection info — Collection metadata
--------------------------------------------------------------------------------

Collections — Collection info — Collection metadata

Available as of v1.16.0
For convenience and better data organization, Qdrant allows attaching custom metadata to collections in the form of key-value pairs.
Adding metadata is treated as a part of collection configuration and synchronized across all nodes in a cluster with consensus protocol.
Collection metadata can be specified during collection creation:
{{}}
as well as updated later:
{{}}
Note, that update operation only modifies the specified metadata fields, leaving other fields unchanged.
When specified, metadata is returned as part of collection info:
``` json
{
    "result": {
        "config": {
            "metadata": {
                "my-metadata-field": {
                    "key-a": "value-a",
                    "key-b": 42
                },
                "another-field": 123
            }
        }
    }
}
```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 475
Retrieved by: dense 2, sparse 1, hybrid 1, colbert 1
Section: Payload — Update payload
--------------------------------------------------------------------------------

Payload — Update payload

Updating payloads in Qdrant offers flexible methods to manage vector metadata. The set payload method updates specific fields while keeping others unchanged, while the overwrite method replaces the entire payload. Developers can also use clear payload to remove all metadata or delete fields to remove specific keys without affecting the rest. These options provide precise control for adapting to dynamic datasets.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1044
Retrieved by: dense 3, hybrid 3
Section: Additional Tutorials
--------------------------------------------------------------------------------

Additional Tutorials

Discover additional examples and use cases of Qdrant with Dynamiq:
 Using Qdrant with Dynamiq – A Hands-on Tutorial
 End-to-End Application with Qdrant and Dynamiq

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 898
Retrieved by: dense 4, hybrid 6, colbert 3
Section: Region-Specific Contract Management System — Implementation — Qdrant collection
--------------------------------------------------------------------------------

Region-Specific Contract Management System — Implementation — Qdrant collection

Aleph Alpha embeddings are high dimensional vectors by default, with a dimensionality of `5120`. However, a pretty
unique feature of that model is that they might be compressed to a size of `128`, with a small drop in accuracy
performance (4-6%, according to the docs). Qdrant can store even the original vectors easily, and this sounds like a
good idea to enable Binary Quantization to save space and
make the retrieval faster. Let's create a collection with such settings:
```python_code_1```
We are going to use the `contracts` collection to store the vectors of the documents. The `always_ram` flag is set to
`True` to keep the quantized vectors in RAM, which will speed up the search process. We also wanted to restrict access
to the individual documents, so only users with the proper permissions can see them. In Qdrant that should be solved by
adding a payload field that defines who can access the document. We'll call this field `roles` and set it to an array
of strings with the roles that can access the document.
```python_code_2```
Since we use Langchain, the `roles` field is a nested field of the `metadata`, so we have to define it as
`metadata.roles`. The schema says that the field is a keyword, which means it is a string or an array of strings. We are
going to use the name of the customers as the roles, so the access control will be based on the customer name.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 885
Retrieved by: dense 5, hybrid 8
Section: Private RAG Information Extraction Engine — Deploying Qdrant Hybrid Cloud on Vultr — Qdrant Hybrid Cloud
--------------------------------------------------------------------------------

Private RAG Information Extraction Engine — Deploying Qdrant Hybrid Cloud on Vultr — Qdrant Hybrid Cloud

Our documentation contains a comprehensive guide on how to set up Qdrant in the Hybrid Cloud mode on Vultr. Please follow it carefully to get your Qdrant instance up and running. Once it's done, we need to store the Qdrant URL and the API key in the environment variables. You can do it by running the following commands:
```shell_code_1```
```python_code_2```
DSPy is framework we are going to use. It's integrated with Qdrant already, but it assumes you use
FastEmbed to create the embeddings. DSPy does not provide a way to index the
data, but leaves this task to the user. We are going to create a collection on our own, and fill it with the embeddings
of our document chunks.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1736
Retrieved by: dense 6, hybrid 9
Section: API Reference — qdrant.io/v1
--------------------------------------------------------------------------------

API Reference — qdrant.io/v1

Package v1 contains API Schema definitions for the qdrant.io v1 API group

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 598
Retrieved by: dense 7
Section: Further Reading
--------------------------------------------------------------------------------

Further Reading

Getting started with Connect
 Qdrant Output Reference

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1589
Retrieved by: dense 8
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Update the collection with patch requests to put vector data on disk. This functionality allows you to specify vector parameters, such as setting vectors to be stored on disk, for a specific collection. In cases where the collection does not have named vectors, an empty name (`""`) should be used to perform this update. This feature provided by Qdrant version 1.4 enables modifications to collection parameters, including HNSW index, quantization, and disk configurations dynamically, without the need to recreate the collection. Additionally, segments containing index and quantized data will be automatically rebuilt in the background to align with the new parameters.

```bash_code_1```


```http_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1787
Retrieved by: dense 9
Section: API Reference — qdrant.io/v1 — Resource Types — QdrantEntity
--------------------------------------------------------------------------------

API Reference — qdrant.io/v1 — Resource Types — QdrantEntity

QdrantEntity is the Schema for the qdrantentities API
_Appears in:_
 QdrantEntityList
`apiVersion` _string_ — `qdrant.io/v1`
`kind` _string_ — `QdrantEntity`
`metadata` _ObjectMeta_ — Refer to Kubernetes API documentation for fields of `metadata`.
`spec` _QdrantEntitySpec_

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1652
Retrieved by: dense 10
Section: Further Reading
--------------------------------------------------------------------------------

Further Reading

Getting started with Datadog
 Qdrant integration source

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1900
Retrieved by: sparse 3, hybrid 4, colbert 5
Section: Using Cloud Inference with Qdrant for Vector Search — Create a Collection
--------------------------------------------------------------------------------

Using Cloud Inference with Qdrant for Vector Search — Create a Collection

Qdrant stores vectors and associated metadata in collections. A collection requires vector parameters to be set during creation. In this case, let's set up a collection using `BM25` for sparse vectors and `all-minilm-l6-v2` for dense vectors. BM25 uses the Inverse Document Frequency to reduce the weight of common terms that appear in many documents while boosting the importance of rare terms that are more discriminative for retrieval. Qdrant will handle the calculations of the IDF term if we enable that in the configuration of the `bm25_sparse_vector` named sparse vector.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1191
Retrieved by: sparse 4, hybrid 5, colbert 4
Section: Administration — Recovery mode
--------------------------------------------------------------------------------

Administration — Recovery mode

Available as of v1.2.0
Recovery mode can help in situations where Qdrant fails to start repeatedly.
When starting in recovery mode, Qdrant only loads collection metadata to prevent
going out of memory. This allows you to resolve out of memory situations, for
example, by deleting a collection. After resolving Qdrant can be restarted
normally to continue operation.
In recovery mode, collection operations are limited to
deleting a
collection. That is because only collection metadata is loaded during recovery.
To enable recovery mode with the Qdrant Docker image you must set the
environment variable `QDRANT_ALLOW_RECOVERY_MODE=true`. The container will try
to start normally first, and restarts in recovery mode if initialisation fails
due to an out of memory error. This behavior is disabled by default.
If using a Qdrant binary, recovery mode can be enabled by setting a recovery
message in an environment variable, such as
`QDRANT__STORAGE__RECOVERY_MODE="My recovery message"`.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 985
Retrieved by: sparse 5, hybrid 7, colbert 6
Section: Using FastEmbed with Qdrant for Vector Search — Create a collection
--------------------------------------------------------------------------------

Using FastEmbed with Qdrant for Vector Search — Create a collection

Qdrant stores vectors and associated metadata in collections.
Collection requires vector parameters to be set during creation.
In this tutorial, we'll be using `BAAI/bge-small-en` to compute embeddings.
```python_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1873
Retrieved by: sparse 6, hybrid 10
Section: Setup Data Streaming with Kafka via Confluent — Qdrant
--------------------------------------------------------------------------------

Setup Data Streaming with Kafka via Confluent — Qdrant

The processed data is then routed to Qdrant, a highly scalable vector search engine designed for similarity searches. Qdrant excels at managing and searching through high-dimensional vector data, which is essential for applications involving machine learning and AI, such as recommendation systems, image recognition, and natural language processing. The Qdrant Sink Connector for Kafka plays a pivotal role here, enabling seamless integration between Kafka and Qdrant. This connector allows for the real-time ingestion of vector data into Qdrant, ensuring that the data is always up-to-date and ready for high-performance similarity searches.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1840
Retrieved by: sparse 7
Section: Managing a Qdrant Cluster — Automatic Shard Rebalancing
--------------------------------------------------------------------------------

Managing a Qdrant Cluster — Automatic Shard Rebalancing

Qdrant Private Cloud supports automatic shard rebalancing. This means that when you scale up or down the number of nodes in a cluster, the operator will automatically redistribute the shards across the available nodes to ensure an even distribution of data.
To enable automatic shard rebalancing, you can set the `rebalancestrategy` field in the QdrantCluster spec:
```yaml_code_1```
For a list of all available rebalancing strategies, see the Qdrant Private Cloud API Reference.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1881
Retrieved by: sparse 8
Section: Qdrant on Databricks
--------------------------------------------------------------------------------

Qdrant on Databricks

Databricks is a unified analytics platform for working with big data and AI. It's built around Apache Spark, a powerful open-source distributed computing system well-suited for processing large-scale datasets and performing complex analytics tasks.
Apache Spark is designed to scale horizontally, meaning it can handle expensive operations like generating vector embeddings by distributing computation across a cluster of machines. This scalability is crucial when dealing with large datasets.
In this example, we will demonstrate how to vectorize a dataset with dense and sparse embeddings using Qdrant's FastEmbed library. We will then load this vectorized data into a Qdrant cluster using the Qdrant Spark connector on Databricks.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1683
Retrieved by: sparse 9
Section: Keboola — Using Qdrant in Keboola
--------------------------------------------------------------------------------

Keboola — Using Qdrant in Keboola

With Keboola's Qdrant integration, you can:
 Data Pipeline Integration: Extract data from any source in Keboola, transform it, and load vector embeddings into Qdrant for semantic search capabilities.
 Vector Database Management: Create, manage, and update collections in Qdrant directly from your Keboola workflows.
 Orchestration: Schedule and automate your vector database operations as part of your data pipeline.
 ML Operations: Combine your machine learning models with vector search capabilities for advanced AI applications.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 235
Retrieved by: sparse 10
Section: Build a Hybrid Search Service with FastEmbed and Qdrant — Run Qdrant in Docker
--------------------------------------------------------------------------------

Build a Hybrid Search Service with FastEmbed and Qdrant — Run Qdrant in Docker

Next, you need to manage all of your data using a vector engine. Qdrant lets you store, update or delete created vectors. Most importantly, it lets you search for the nearest vectors via a convenient API.
> Note: Before you begin, create a project directory and a virtual python environment in it.
1. Download the Qdrant image from DockerHub.
```bash_code_1```
2. Start Qdrant inside of Docker.
```bash_code_2```
You should see output like this
```text_code_3```
Test the service by going to the local Qdrant dashboard. You should see the Qdrant version info in your browser.
All data uploaded to Qdrant is saved inside the `./qdrant_storage` directory and will be persisted even if you recreate the container.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 103
Retrieved by: colbert 7
Section: Send S3 Data to Qdrant Vector Store with LangChain — Step 3: Loading Embeddings into Qdrant — Creating a Collection in Qdrant
--------------------------------------------------------------------------------

Send S3 Data to Qdrant Vector Store with LangChain — Step 3: Loading Embeddings into Qdrant — Creating a Collection in Qdrant

In Qdrant, data is organized in collections, each representing a set of embeddings (or points) and their associated metadata (payload). To store the embeddings generated earlier, you’ll first need to create a collection.
Here’s how to create a collection in Qdrant to store both text and image embeddings:
```python_code_1```
This function creates a collection for storing text (384 dimensions) and image (512 dimensions) embeddings, using cosine similarity to compare embeddings within the collection.
Once the collection is set up, you can load the embeddings into Qdrant. This involves inserting (or updating) the embeddings and their associated metadata (payload) into the specified collection.
Here’s the code for loading embeddings into Qdrant:
```python_code_2```
Explanation of Ingestion
1. Upserting the Data Point: The upsert method on the `qdrant_client` inserts each PointStruct into the specified collection. If a point with the same ID already exists, it will be updated with the new values.
2. Operation Info: The function returns `operation_info`, which contains details about the upsert operation, such as success status or any potential errors.
Running the Ingestion Code
Here’s how to call the function and ingest data:
```python_code_3```
The `PointStruct` is instantiated with these key parameters:
 id: A unique identifier for each embedding, typically an incremental index.
 vector: A dictionary holding the text and image inputs to be embedded. `qdrant-client` uses FastEmbed under the hood to automatically generate vector representations from these inputs locally.
 payload: A dictionary storing additional metadata, like product reviews and image references, which is invaluable for retrieval and context during searches.
The code dynamically loads folders from an S3 bucket, processes text and image files separately, and stores their embeddings and associated data in dedicated lists. It then creates a `PointStruct` for each data entry and calls the ingestion function to load it into Qdrant.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 947
Retrieved by: colbert 8
Section: Frequently Asked Questions: General Topics — Should I create one Qdrant collection per user?
--------------------------------------------------------------------------------

Frequently Asked Questions: General Topics — Should I create one Qdrant collection per user?

No. Creating one collection per user is more resource intensive.
Instead of creating separate collections for each user, we recommend creating a single collection and separate access using payloads. Each Qdrant point can have a payload as metadata. For multitenancy, you can include a `user_id` or `tenant_id` for each point. To optimize storage further, you can enable tenant indexing for payload fields.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 104
Retrieved by: colbert 9
Section: Send S3 Data to Qdrant Vector Store with LangChain — Step 3: Loading Embeddings into Qdrant — Exploring the Qdrant WebUI Dashboard
--------------------------------------------------------------------------------

Send S3 Data to Qdrant Vector Store with LangChain — Step 3: Loading Embeddings into Qdrant — Exploring the Qdrant WebUI Dashboard

Once the embeddings are loaded into Qdrant, you can use the WebUI dashboard to visualize and manage your collections. The dashboard provides a clear, structured interface for viewing collections and their data. Let’s take a closer look in the next section.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1832
Retrieved by: colbert 10
Section: Managing a Qdrant Cluster — Scaling a Cluster
--------------------------------------------------------------------------------

Managing a Qdrant Cluster — Scaling a Cluster

To scale a cluster, update the CPU, memory and storage resources in the QdrantCluster spec. The Qdrant operator will automatically adjust the cluster configuration. This operation is highly available on a multi-node cluster with replicated collections.
Vertical scaling is only possible if your CSI driver and StorageClass allows volume expansion. Disk storage can not be downscaled.

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How to filter points by a payload field?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 478
Retrieved by: dense 1, hybrid 2
Section: Payload — Update payload — Clear payload
--------------------------------------------------------------------------------

Payload — Update payload — Clear payload

This method removes all payload keys from specified points
REST API (Schema):
{{}}
You can also use models.FilterSelector to remove the points matching given filter criteria, instead of providing the ids.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 474
Retrieved by: dense 2, hybrid 5
Section: Payload — Create point with payload
--------------------------------------------------------------------------------

Payload — Create point with payload

REST API (Schema)
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1531
Retrieved by: dense 3, sparse 3, hybrid 3, colbert 4
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Set the payload for points in a collection by applying a filter based on the specified properties. In this case, the code will set the payload with "property1" and "property2" values for points where the value of the "color" property is "red" within the specified collection. This approach allows for targeted modifications without needing to know the specific point ids.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 479
Retrieved by: dense 4, hybrid 7
Section: Payload — Update payload — Delete payload keys
--------------------------------------------------------------------------------

Payload — Update payload — Delete payload keys

Delete specific payload keys from points.
REST API (Schema):
{{}}
Alternatively, you can use filters to delete payload keys from the points.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1487
Retrieved by: dense 5, sparse 7, hybrid 6
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet showcases a scenario where a collection of points can be queried with a focus on the contents of the payload data associated with each point. The example demonstrates the use of dense vectors as queries along with filters based on payload fields such as 'color' with values like "red" or "green". Additionally, the results can be limited and ordered based on a specific payload field such as "price". This functionality allows for more refined and customized querying based on both vector similarity and payload content.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1515
Retrieved by: dense 6, hybrid 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Retrieve a single point based on a specified filter condition from a collection of points without being aware of the specific identifiers. It allows for fetching points based on a defined filter criterion. The request includes criteria for filtering points by properties like color, where only points with a color value of "red" will be returned. The response will contain one point with additional payload information, and the vector information will not be included. This functionality enables efficient iteration through points that match the specified filter.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 416
Retrieved by: dense 7
Section: Filtering — Filtering conditions — Has id
--------------------------------------------------------------------------------

Filtering — Filtering conditions — Has id

This type of query is not related to payload, but can be very useful in some situations.
For example, the user could mark some specific search results as irrelevant, or we want to search only among the specified points.
{{}}
Filtered points would be:
```json_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1710
Retrieved by: dense 8
Section: N8N — Operations — Payload
--------------------------------------------------------------------------------

N8N — Operations — Payload

Set Payload Set payload for points
 Overwrite Payload Replace entire payload for points
 Delete Payload Remove payload from points
 Clear Payload Clear all payload fields
 Payload Facets Get payload field statistics
 Create Payload Index Create an index for payload fields
 Delete Payload Index Remove a payload field index

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 402
Retrieved by: dense 9, sparse 1, hybrid 1, colbert 3
Section: Filtering — Filtering conditions — Nested key
--------------------------------------------------------------------------------

Filtering — Filtering conditions — Nested key

Available as of v1.1.0
Payloads being arbitrary JSON object, it is likely that you will need to filter on a nested field.
For convenience, we use a syntax similar to what can be found in the Jq project.
Suppose we have a set of points with the following payload:
```json_code_1```
You can search on a nested field using a dot notation.
{{}}
You can also search through arrays by projecting inner values using the `[]` syntax.
{{}}
This query would only output the point with id 2 as only Japan has a city with population greater than 9.0.
And the leaf nested field can also be an array.
{{}}
This query would only output the point with id 2 as only Japan has a city with the "Osaka castke" as part of the sightseeing.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 476
Retrieved by: dense 10
Section: Payload — Update payload — Set payload
--------------------------------------------------------------------------------

Payload — Update payload — Set payload

Set only the given payload values on a point.
REST API (Schema):
{{}}
You don't need to know the ids of the points you want to modify. The alternative
is to use filters.
{{}}
_Available as of v1.8.0_
It is possible to modify only a specific key of the payload by using the `key` parameter.
For instance, given the following payload JSON object on a point:
```json_code_1```
You can modify the `nested_property` of `property1` with the following request:
{{}}
Resulting in the following payload:
```json_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 499
Retrieved by: sparse 2, hybrid 4, colbert 6
Section: Points — Scroll points — Order points by payload key
--------------------------------------------------------------------------------

Points — Scroll points — Order points by payload key

_Available as of v1.8.0_
When using the `scroll` API, you can sort the results by payload key. For example, you can retrieve points in chronological order if your payloads have a `"timestamp"` field, as is shown from the example below:
Without an appropriate index, payload-based ordering would create too much load on the system for each request. Qdrant therefore requires a payload index which supports Range filtering conditions on the field used for order_by
{{}}
You need to use the `order_by` `key` parameter to specify the payload key. Then you can add other fields to control the ordering, such as `direction` and `start_from`:
{{}}
When you use the order_by parameter, pagination is disabled.
When sorting is based on a non-unique value, it is not possible to rely on an ID offset. Thus, next_page_offset is not returned within the response. However, you can still do pagination by combining `"order_by": { "start_from": ... }` with a `{ "must_not": [{ "has_id": [...] }] }` filter.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1336
Retrieved by: sparse 4, hybrid 8, colbert 1
Section: Filtering — Filtering on an Exact String
--------------------------------------------------------------------------------

Filtering — Filtering on an Exact String

To filter on exact strings, first create a payload index of type `keyword`for the field you want to filter on. A payload index makes filtering faster and reduces the load on the system.
Filtering on a field without an index is not possible on collections that run in strict mode. Strict mode is enabled by default on Qdrant Cloud.
For example, to filter books by author name, create a keyword index on the "author" field:
{{}}
Next, when querying the data, you also add a filter clause to the request. The following example searches for books related to "time travel" but only returns books written by H.G. Wells:
{{}}
The ranking of the results of this request is based on the vector similarity of the query. The filter only narrows down the results to those points where the `author` field exactly matches `H.G. Wells`. Furthermore, the filter is case-sensitive. Filtering for the lowercase value `h.g. wells` would not return any results.
The previous example only returns points that match the filter value. If you want the opposite: exclude points with a specific value, use a `must_not` clause instead of `must`. The following example only returns books not written by H.G. Wells:
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1529
Retrieved by: sparse 5, hybrid 9, colbert 2
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Sort your collection points by a custom payload key when using the scroll API. This feature enables you to order and retrieve the points based on a specific payload key, in this case, the `"timestamp"` field. Just keep in mind that for this to work efficiently, Qdrant needs a payload index supporting range filtering conditions.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1505
Retrieved by: sparse 6
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates how to send a POST request to query points from a collection. It includes a query array and specifies certain payload fields to be included in the response, such as 'city', 'village', and 'town'. The `with_payload` parameter helps to filter the payload and retrieve only the specified fields.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1340
Retrieved by: sparse 8
Section: Filtering — Filter on Text Strings
--------------------------------------------------------------------------------

Filtering — Filter on Text Strings

To filter on text values in a payload field, first create a full-text index for that field. Next, you can use a `text` condition to query the collection with a filter for titles that contain the word "space":
{{}}
When filtering on more than one term, a `text` filter only matches fields that contain all the specified terms (logical `AND`). To match fields that contain any of the specified terms (logical `OR`), use the `text_any` condition:
{{}}
Qdrant also supports phrase filtering, enabling you to search for multiple words in the exact order they appear in the original text, with no other words in between. For example, a phrase filter for "time machine" matches against the title "The Time Machine" but would not match "The Time Travel Machine" (there's a word between "time" and "machine") nor "Machine Time" (the word order is incorrect).
The difference between phrase filtering and keyword filtering is that phrase filtering applies text processing and, as a result, is case-insensitive, while keyword filtering is case-sensitive and only matches the exact string. Additionally, keyword filtering has to match the entire string, whereas phrase filtering can match part of a larger string. So a keyword filter for "Space War" would not match "The Space War" because it doesn't match "The," but a phrase filter for "Space War" would.
Summarizing the differences between the four filtering methods for a multi-term filter on "Space War":
text_any — `space` OR `war` — Yes — Yes — Yes — Yes
text — `space` AND `war` — Yes — Yes — Yes — No
phrase — `"space war"` — Yes — Yes — No — No
keyword — `"Space War"` — Yes — No — No — No
To filter on phrases, use a `phrase` condition. This requires enabling phrase searching when creating the full-text index:
{{}}
Next, you can use a `phrase` condition to filter for titles that contain the exact phrase "time machine":
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 481
Retrieved by: sparse 9, colbert 5
Section: Payload — Facet counts
--------------------------------------------------------------------------------

Payload — Facet counts

Available as of v1.12.0
Faceting is a special counting technique that can be used for various purposes:
 Know which unique values exist for a payload key.
 Know the number of points that contain each unique value.
 Know how restrictive a filter would become by matching a specific value.
Specifically, it is a counting aggregation for the values in a field, akin to a `GROUP BY` with `COUNT(*)` commands in SQL.
These results for a specific field is called a "facet". For example, when you look at an e-commerce search results page, you might see a list of brands on the sidebar, showing the number of products for each brand. This would be a facet for a `"brand"` field.
In Qdrant you can facet on a field only if you have created a field index that supports MatchValue conditions for it, like a keyword index.
To get the facet counts for a field, you can use the following:
By default, the number of hits returned is limited to 10. To change this, use the limit parameter. Keep this in mind when checking the number of unique values a payload field contains.
REST API (Facet)
{{}}
The response will contain the counts for each unique value in the field:
```json_code_1```
The results are sorted by the count in descending order, then by the value in ascending order.
Only values with non-zero counts will be returned.
By default, the way Qdrant the counts for each value is approximate to achieve fast results. This should accurate enough for most cases, but if you need to debug your storage, you can use the `exact` parameter to get exact counts.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1494
Retrieved by: sparse 10, colbert 8
Section: Introduction
--------------------------------------------------------------------------------

Introduction

The snippet demonstrates how to boost the score of points based on their tag field. If the tag field is one of the headers, it will be more relevant to the query. Tags are located in the payload and included in the boost formula as a filtering condition.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 509
Retrieved by: colbert 7
Section: Similarity search — Search API — ACORN Search Algorithm
--------------------------------------------------------------------------------

Similarity search — Search API — ACORN Search Algorithm

Available as of v1.16.0
For filtered vector search, you are recommended to create a payload index for the fields you want to filter by.
During the search, Qdrant will use a combined filterable index.
However, when combining multiple strict payload filters, this mechanism might not provide sufficient accuracy.
In such cases, you can use the ACORN search algorithm.
It is an extension to the regular HNSW search algorithm, based on the ACORN-1 algorithm described in the paper ACORN: Performant and Predicate-Agnostic Search Over Vector Embeddings and Structured Data.
During graph traversal, it explores not just direct neighbors (first hop), but also neighbors of neighbors (second hop) when direct neighbors are filtered out.
This improves search accuracy at the cost of performance.
Enable it as follows:
{{}}
ACORN is disabled by default.
Once enabled via the `enable` flag, it activates conditionally when estimated filter selectivity is below the threshold.
The optional `max_selectivity` value controls this threshold;
`0.0` means ACORN will never be used, `1.0` means it will always be used. The default value is `0.4`.
Selectivity is estimated as:
$$ \text{Estimated filter selectivity} =
 \frac{\text{Estimated number of points satisfying the filters}}
 {\text{Total number of points}}
$$
Since ACORN is significantly slower (approximately 2-10x in typical scenarios) but improves recall for restrictive filters, tuning this parameter is about deciding when the accuracy improvement justifies the performance cost.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 437
Retrieved by: colbert 9
Section: Indexing — Full-text index
--------------------------------------------------------------------------------

Indexing — Full-text index

Qdrant supports full-text search for string payload.
Full-text index allows you to filter points by the presence of a word or a phrase in the payload field.
Full-text index configuration is a bit more complex than other indexes, as you can specify the tokenization parameters.
Tokenization is the process of splitting a string into tokens, which are then indexed in the inverted index.
See Full Text match for examples of querying with a full-text index.
To create a full-text index, you can use the following:
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 432
Retrieved by: colbert 10
Section: Indexing — Payload Index
--------------------------------------------------------------------------------

Indexing — Payload Index

Payload index in Qdrant is similar to the index in conventional document-oriented databases.
This index is built for a specific field and type, and is used for quick point requests by the corresponding filtering condition.
The index is also used to accurately estimate the filter cardinality, which helps the query planning choose a search strategy.
Creating an index requires additional computational resources and memory, so choosing fields to be indexed is essential. Qdrant does not make this choice but grants it to the user.
To mark a field as indexable, you can use the following:
{{}}
You can use dot notation to specify a nested field for indexing. Similar to specifying nested filters.
Available field types are:
* `keyword` for keyword payload, affects Match filtering conditions.
* `integer` for integer payload, affects Match and Range filtering conditions.
* `float` for float payload, affects Range filtering conditions.
* `bool` for bool payload, affects Match filtering conditions (available as of v1.4.0).
* `geo` for geo payload, affects Geo Bounding Box and Geo Radius filtering conditions.
* `datetime` for datetime payload, affects Range filtering conditions (available as of v1.8.0).
* `text` a special kind of index, available for keyword / string payloads, affects Full Text search filtering conditions. Read more about text index configuration
* `uuid` a special type of index, similar to `keyword`, but optimized for UUID values.
Affects Match filtering conditions. (available as of v1.11.0)
Payload index may occupy some additional memory, so it is recommended to only use the index for those fields that are used in filtering conditions.
If you need to filter by many fields and the memory limits do not allow for indexing all of them, it is recommended to choose the field that limits the search result the most.
As a rule, the more different values a payload value has, the more efficiently the index will be used.

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How to search vectors with a metadata condition?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 1512
Retrieved by: dense 1, hybrid 2
Section: Introduction
--------------------------------------------------------------------------------

Introduction

The code snippet demonstrates how to make a query to explore points in a collection based on named vectors. In this case, the query is configured to recommend vectors specified as 'positive' and 'negative'. By setting the 'using' parameter to "image" and limiting the results to 10, you can retrieve relevant data for the specified vectors in the collection. This feature is available starting from version 0.10.0 and allows for more granular recommendation requests when dealing with multiple vectors in a collection.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 506
Retrieved by: dense 2, hybrid 4
Section: Similarity search — Search API
--------------------------------------------------------------------------------

Similarity search — Search API

Let's look at an example of a search query.
REST API API Schema definition is available here
{{}}
In this example, we are looking for vectors similar to vector `[0.2, 0.1, 0.9, 0.7]`.
Parameter `limit` (or its alias `top`) specifies the amount of most similar results we would like to retrieve.
Values under the key `params` specify custom parameters for the search.
Currently, it could be:
* `hnsw_ef` value that specifies `ef` parameter of the HNSW algorithm.
* `exact` option to not use the approximate search (ANN). If set to true, the search may run for a long as it performs a full scan to retrieve exact results.
* `indexed_only` With this option you can disable the search in those segments where vector index is not built yet. This may be useful if you want to minimize the impact to the search performance whilst the collection is also being updated. Using this option may lead to a partial result if the collection is not fully indexed yet, consider using it only if eventual consistency is acceptable for your use case.
* `quantization` parameters related to quantization. See Searching with Quantization guide.
* `acorn` parameters related to the ACORN search algorithm.
Since the `filter` parameter is specified, the search is performed only among those points that satisfy the filter condition.
See details of possible filters and their work in the filtering section.
Example result of this API would be
```json_code_1```
The `result` contains ordered by `score` list of found point ids.
Note that payload and vector data is missing in these results by default.
See payload and vector in the result on how
to include it.
If the collection was created with multiple vectors, the name of the vector to use for searching should be provided:
{{}}
Search is processing only among vectors with the same name.
If the collection was created with sparse vectors, the name of the sparse vector to use for searching should be provided:
You can still use payload filtering and other features of the search API with sparse vectors.
There are however important differences between dense and sparse vector search:
Scoring Metric — Default is `Dot product`, no need to specify it — `Distance` has supported metrics e.g. Dot, Cosine
Search Type — Always exact in Qdrant — HNSW is an approximate NN
Return Behaviour — Returns only vectors with non-zero values in the same indices as the query vector — Returns `limit` vectors
In general, the speed of the search is proportional to the number of non-zero values in the query vector.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1090
Retrieved by: dense 3, hybrid 7
Section: LangChain — Similarity search — Dense Vector Search
--------------------------------------------------------------------------------

LangChain — Similarity search — Dense Vector Search

To search with only dense vectors,
 The `retrieval_mode` parameter should be set to `RetrievalMode.DENSE`(default).
 A dense embeddings value should be provided for the `embedding` parameter.
```py_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1374
Retrieved by: dense 4, hybrid 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code sets up a collection with vectors containing 128 dimensions and a cosine distance metric. It configures the datatype for dense vectors to be Float16, which consumes less memory than Float32 without significant impact on search quality. Additionally, it specifies Float16 as the datatype for sparse text vectors in the collection.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1383
Retrieved by: dense 5, hybrid 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates creating a collection in Qdrant with support for sparse vectors. Sparse vectors are useful for text search, representing each word as a separate dimension. This feature allows collections to contain both sparse vectors and regular dense vectors in one point. Sparse vectors need to be named uniquely within a collection, separate from the names of dense vectors.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 417
Retrieved by: dense 6, sparse 5, hybrid 5, colbert 6
Section: Filtering — Filtering conditions — Has vector
--------------------------------------------------------------------------------

Filtering — Filtering conditions — Has vector

Available as of v1.13.0
This condition enables filtering by the presence of a given named vector on a point.
For example, if we have two named vector in our collection.
```http_code_1```
Some points in the collection might have all vectors, some might have only a subset of them.
If your collection does not have named vectors, use an empty ("") name.
This is how you can search for points which have the dense `image` vector defined:
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 359
Retrieved by: dense 7
Section: Collections — Create a collection — Collection with sparse vectors
--------------------------------------------------------------------------------

Collections — Create a collection — Collection with sparse vectors

Available as of v1.7.0
Qdrant supports sparse vectors as a first-class citizen.
Sparse vectors are useful for text search, where each word is represented as a separate dimension.
Collections can contain sparse vectors as additional named vectors along side regular dense vectors in a single point.
Unlike dense vectors, sparse vectors must be named.
And additionally, sparse vectors and dense vectors must have different names within a collection.
{{}}
Outside of a unique name, there are no required configuration parameters for sparse vectors.
The distance function for sparse vectors is always `Dot` and does not need to be specified.
However, there are optional parameters to tune the underlying sparse vector index.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1092
Retrieved by: dense 8
Section: LangChain — Similarity search — Hybrid Vector Search
--------------------------------------------------------------------------------

LangChain — Similarity search — Hybrid Vector Search

To perform a hybrid search using dense and sparse vectors with score fusion,
 The `retrieval_mode` parameter should be set to `RetrievalMode.HYBRID`.
 A dense embeddings value should be provided for the `embedding` parameter.
 An implementation of the SparseEmbeddings interface using any sparse embeddings provider has to be provided as value to the `sparse_embedding` parameter.
```python_code_1```
Note that if you've added documents with HYBRID mode, you can switch to any retrieval mode when searching. Since both the dense and sparse vectors are available in the collection.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1487
Retrieved by: dense 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet showcases a scenario where a collection of points can be queried with a focus on the contents of the payload data associated with each point. The example demonstrates the use of dense vectors as queries along with filters based on payload fields such as 'color' with values like "red" or "green". Additionally, the results can be limited and ordered based on a specific payload field such as "price". This functionality allows for more refined and customized querying based on both vector similarity and payload content.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1497
Retrieved by: dense 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet allows you to perform a search using sparse vectors. The query includes indices and corresponding values to search within the specified collection using a text-based search approach.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 985
Retrieved by: sparse 1, hybrid 1, colbert 1
Section: Using FastEmbed with Qdrant for Vector Search — Create a collection
--------------------------------------------------------------------------------

Using FastEmbed with Qdrant for Vector Search — Create a collection

Qdrant stores vectors and associated metadata in collections.
Collection requires vector parameters to be set during creation.
In this tutorial, we'll be using `BAAI/bge-small-en` to compute embeddings.
```python_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 984
Retrieved by: sparse 2, hybrid 3, colbert 3
Section: Using FastEmbed with Qdrant for Vector Search — Add data
--------------------------------------------------------------------------------

Using FastEmbed with Qdrant for Vector Search — Add data

Now you can add two sample documents, their associated metadata, and a point `id` for each.
```python_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1900
Retrieved by: sparse 3, hybrid 6, colbert 2
Section: Using Cloud Inference with Qdrant for Vector Search — Create a Collection
--------------------------------------------------------------------------------

Using Cloud Inference with Qdrant for Vector Search — Create a Collection

Qdrant stores vectors and associated metadata in collections. A collection requires vector parameters to be set during creation. In this case, let's set up a collection using `BM25` for sparse vectors and `all-minilm-l6-v2` for dense vectors. BM25 uses the Inverse Document Frequency to reduce the weight of common terms that appear in many documents while boosting the importance of rare terms that are more discriminative for retrieval. Qdrant will handle the calculations of the IDF term if we enable that in the configuration of the `bm25_sparse_vector` named sparse vector.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1858
Retrieved by: sparse 4, hybrid 8
Section: Implementing Vector Search with Reranking — Overview — Retrieval Stage
--------------------------------------------------------------------------------

Implementing Vector Search with Reranking — Overview — Retrieval Stage

User's Query: Now we enter the retrieval phase. The user submits a query, and it’s time to match that query against the stored documents.
 Embeddings: Just like with the documents, the user’s query is converted into a sparse or dense embedding. This enables the system to compare the query's meaning with the meanings of the stored documents.
 Vector Search: The system searches for the most relevant documents by comparing the query’s embedding to those in the vector database, and it pulls up the closest matches.
 Rerank: Once the initial results are in, the reranking process kicks in to ensure you get the best results on top. We’ll be using Cohere’s rerank-english-v3.0 model, which excels at reordering English language documents to prioritize relevance. It can handle up to 4096 tokens, giving it plenty of context to work with. And if you’re dealing with multi-lingual data, don’t worry—Cohere’s got reranking models for other languages too.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 641
Retrieved by: sparse 6, colbert 4
Section: Upload and Search Large collections cost-efficiently — Dataset
--------------------------------------------------------------------------------

Upload and Search Large collections cost-efficiently — Dataset

The dataset we will use is LAION-400M, a collection of approximately 400 million vectors obtained from
images extracted from a Common Crawl dataset. Each vector is 512-dimensional and generated using a CLIP model.
Vectors are associated with a number of metadata fields, such as `url`, `caption`, `LICENSE`, etc.
The overall payload size is approximately 200 GB, and the vectors are 400 GB.
Dataset doesn't store images themselves, and only contain URLs to the image origin. By the time of writing, some of the URLs are already unavailable.
The dataset is available in the form of 409 chunks, each containing approximately 1M vectors.
We will use the following python script to upload dataset chunks one by one.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 508
Retrieved by: sparse 7
Section: Similarity search — Search API — Payload and vector in the result
--------------------------------------------------------------------------------

Similarity search — Search API — Payload and vector in the result

By default, retrieval methods do not return any stored information such as
payload and vectors. Additional parameters `with_vectors` and `with_payload`
alter this behavior.
Example:
{{}}
You can use `with_payload` to scope to or filter a specific payload subset.
You can even specify an array of items to include, such as `city`,
`village`, and `town`:
{{}}
Or use `include` or `exclude` explicitly. For example, to exclude `city`:
{{}}
It is possible to target nested fields using a dot notation:
* `payload.nested_field` for a nested field
* `payload.nested_array[].sub_field` for projecting nested fields within an array
Accessing array elements by index is currently not supported.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1867
Retrieved by: sparse 8
Section: Implementing Vector Search with Reranking — Implementation — Rerank
--------------------------------------------------------------------------------

Implementing Vector Search with Reranking — Implementation — Rerank

This code takes the documents from the search results and reranks them based on your query, making sure you get the most relevant ones right at the top.
First, we pull out the documents from the search results. Then we use Cohere’s rerank model to refine these results:
```python_code_1```
What’s happening here? In the first line, we’re building a list of documents by grabbing the 'document' field from each search result point. Then, we pass this list, along with the original query, to Cohere’s rerank method. Using the rerank-english-v3.0 model, it reshuffles the documents and gives you back the top 5, ranked by their relevance to the query.
Here’s the reranked result table, with the new order and their relevance scores:
0 — In machine learning, feature scaling is the process of normalizing the range of independent variables or features. — 0.99995166
1 — Feature scaling is commonly used in data preprocessing to ensure that features are on the same scale. — 0.99929035
10 — In deep learning, feature scaling helps stabilize the learning process, allowing for better performance and faster convergence. — 0.998675
23 — Data augmentation techniques in machine learning may also include scaling to ensure consistency across training datasets. — 0.998043
3 — Unsupervised learning algorithms, such as clustering methods, may benefit from feature scaling. — 0.9979967
As you can see, the reranking did its job. Positions for documents 10 and 1 got swapped, showing that the reranker has fine-tuned the results to give you the most relevant content at the top.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1865
Retrieved by: sparse 9
Section: Implementing Vector Search with Reranking — Implementation — Retrieval
--------------------------------------------------------------------------------

Implementing Vector Search with Reranking — Implementation — Retrieval

The first few steps here mirror what we did during ingestion—just like before, we need to convert the query into an embedding:
```python_code_1```
After that, we'll move on to retrieve results using vector search and apply reranking on the results. This two-stage process is super efficient because we’re grabbing a small set of the most relevant documents first, which is much faster than reranking a huge dataset.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1856
Retrieved by: sparse 10
Section: Implementing Vector Search with Reranking — Overview
--------------------------------------------------------------------------------

Implementing Vector Search with Reranking — Overview

A typical search system works in two main stages: Ingestion and Retrieval. Think of ingestion as the process where your data gets prepped and loaded into the system, and retrieval as the part where the magic happens—where your queries pull out the most relevant documents.
Check out the architectural diagram below to visualize how these stages work together.
The two essential stages of a search system: Ingestion and Retrieval Process

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1109
Retrieved by: colbert 5
Section: Mastra — Methods — `query()`
--------------------------------------------------------------------------------

Mastra — Methods — `query()`

`vector` — `number[]` — Query vector to find similar vectors
`topK` — `number` — Number of results to return (optional) — `10`
`filter` — `Record` — Metadata filters for the query (optional)

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 833
Retrieved by: colbert 7
Section: Multitenancy with LlamaIndex — Querying documents with constraints
--------------------------------------------------------------------------------

Multitenancy with LlamaIndex — Querying documents with constraints

Let's assume we are searching for some information about large language models, but are only allowed to
use Qdrant documentation. LlamaIndex has a concept of retrievers, responsible for finding the most
relevant nodes for a given query. Our `VectorStoreIndex` can be used as a retriever, with some additional
constraints in our case value of the `library` metadata attribute.
```python_code_1```
The description of Qdrant was the best match, even though it didn't mention large language models
at all. However, it was the only document that belonged to the `qdrant` library, so there was no
other choice. Let's try to search for something that is not present in the collection.
Let's define another retrieve, this time for the `llama-index` library:
```python_code_2```
The results returned by both retrievers are different, due to the different constraints, so we implemented
a real multitenant search application!

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 426
Retrieved by: colbert 8
Section: Hybrid and Multi-Stage Queries — Score boosting
--------------------------------------------------------------------------------

Hybrid and Multi-Stage Queries — Score boosting

_Available as of v1.14.0_
When introducing vector search to specific applications, sometimes business logic needs to be considered for ranking the final list of results.
A quick example is our own documentation search bar.
It has vectors for every part of the documentation site. If one were to perform a search by "just" using the vectors, all kinds of elements would be equally considered good results.
However, when searching for documentation, we can establish a hierarchy of importance:
`title > content > snippets`
One way to solve this is to weight the results based on the kind of element.
For example, we can assign a higher weight to titles and content, and keep snippets unboosted.
Pseudocode would be something like:
`score = score + (is_title 0.5) + (is_content 0.25)`
Query API can rescore points with custom formulas. They can be based on:
 Dynamic payload values
 Conditions
 Scores of prefetches
To express the formula, the syntax uses objects to identify each element.
Taking the documentation example, the request would look like this:
{{}}
There are multiple expressions available, check the API docs for specific details.
 constant A floating point number. e.g. `0.5`.
 `"$score"` Reference to the score of the point in the prefetch. This is the same as `"$score[0]"`.
 `"$score[0]"`, `"$score[1]"`, `"$score[2]"`, ... When using multiple prefetches, you can reference specific prefetch with the index within the array of prefetches.
 payload key Any plain string will refer to a payload key. This uses the jsonpath format used in every other place, e.g. `key` or `key.subkey`. It will try to extract a number from the given key.
 condition A filtering condition. If the condition is met, it becomes `1.0`, otherwise `0.0`.
 mult Multiply an array of expressions.
 sum Sum an array of expressions.
 div Divide an expression by another expression.
 abs Absolute value of an expression.
 pow Raise an expression to the power of another expression.
 sqrt Square root of an expression.
 log10 Base 10 logarithm of an expression.
 ln Natural logarithm of an expression.
 exp Exponential function of an expression (`e^x`).
 geo distance Haversine distance between two geographic points. Values need to be `{ "lat": 0.0, "lon": 0.0 }` objects.
 decay Apply a decay function to an expression, which clamps the output between 0 and 1. Available decay functions are linear, exponential, and gaussian. See more.
 datetime Parse a datetime string (see formats here), and use it as a POSIX timestamp, in seconds.
 datetime key Specify that a payload key contains a datetime string to be parsed into POSIX seconds.
It is possible to define a default for when the variable (either from payload or prefetch score) is not found. This is given in the form of a mapping from variable to value.
If there is no variable, and no defined default, a default value of `0.0` is used.
Considerations when using formula queries:
 Formula queries can only be used as a rescoring step.
 Formula results are always sorted in descending order (bigger is better). For euclidean scores, make sure to negate them to sort closest to farthest.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 927
Retrieved by: colbert 9
Section: Frequently Asked Questions: General Topics — Vectors — What is the maximum size of vector metadata that can be stored?
--------------------------------------------------------------------------------

Frequently Asked Questions: General Topics — Vectors — What is the maximum size of vector metadata that can be stored?

There is no inherent limitation on metadata size, but it should be optimized for performance and resource usage. Users can set upper limits in the configuration.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1394
Retrieved by: colbert 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet is used to create a collection with a specific vector configuration and additional metadata. The metadata is provided as a JSON object, allowing you to store custom information about the collection. In this example, we add two metadata fields.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How to apply multiple filters in a query?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 1337
Retrieved by: dense 1, sparse 2, hybrid 1, colbert 3
Section: Filtering — Filtering on Multiple Exact Strings
--------------------------------------------------------------------------------

Filtering — Filtering on Multiple Exact Strings

You can provide multiple filter clauses. For example, to find all books co-authored by Larry Niven and Jerry Pournelle, use the following filter:
{{}}
Note that both filter clauses must be true for a point to be included in the results, because a `must` clause operates like a logical `AND`. If you want to find books written by either author (as well as both), use a `should` clause, which operates like a logical `OR`:
{{}}
Alternatively, when you want to filter on one or more values of a single key, you can use the `any` condition:
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1524
Retrieved by: dense 2, sparse 5, hybrid 3
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates a way to combine multiple clauses to filter data. In this example, the code shows how to filter data based on a specific city value (in this case, "London") while excluding another specific value (in this case, the color "red"). The specified clauses work together in the filter to refine the results accordingly.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 397
Retrieved by: dense 3, hybrid 6
Section: Filtering — Filtering clauses — Clauses combination
--------------------------------------------------------------------------------

Filtering — Filtering clauses — Clauses combination

It is also possible to use several clauses simultaneously:
{{}}
Filtered points would be:
```json_code_1```
In this case, the conditions are combined by `AND`.
Also, the conditions could be recursively nested. Example:
{{}}
Filtered points would be:
```json_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 398
Retrieved by: dense 4, hybrid 9
Section: Filtering — Filtering conditions
--------------------------------------------------------------------------------

Filtering — Filtering conditions

Different types of values in payload correspond to different kinds of queries that we can apply to them.
Let's look at the existing condition variants and what types of data they apply to.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 400
Retrieved by: dense 5, sparse 3, hybrid 4, colbert 2
Section: Filtering — Filtering conditions — Match Any
--------------------------------------------------------------------------------

Filtering — Filtering conditions — Match Any

Available as of v1.1.0
In case you want to check if the stored value is one of multiple values, you can use the Match Any condition.
Match Any works as a logical OR for the given values. It can also be described as a `IN` operator.
You can apply it to keyword and integer payloads.
Example:
{{}}
In this example, the condition will be satisfied if the stored value is either `black` or `yellow`.
If the stored value is an array, it should have at least one value matching any of the given values. E.g. if the stored value is `["black", "green"]`, the condition will be satisfied, because `"black"` is in `["black", "yellow"]`.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1523
Retrieved by: dense 6, hybrid 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates a query that filters data based on specific IDs. By providing a list of IDs, the query filters out results that do not match these specific IDs. This type of filtering can be beneficial when there is a need to exclude certain data points or focus the search on a predefined set of IDs.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1334
Retrieved by: dense 7
Section: Filtering
--------------------------------------------------------------------------------

Filtering

Qdrant supports filtering on a wide range of datatypes: numbers, dates, booleans, geolocations, and strings. In Qdrant, a filter is typically combined with a vector query. The vector query is used to score and rank the results, while the filter is used to narrow down the results based on specific criteria.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1530
Retrieved by: dense 8, sparse 8, hybrid 8, colbert 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet showcases how to use a filter with multiple conditions for scrolling through points in a collection. In this case, the conditions specified in the filter are that the "city" should be "London" and the "color" should be "red". The usage of "should" indicates that any point meeting at least one of these conditions will be included in the results.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 401
Retrieved by: dense 9, sparse 6, hybrid 7, colbert 8
Section: Filtering — Filtering conditions — Match Except
--------------------------------------------------------------------------------

Filtering — Filtering conditions — Match Except

Available as of v1.2.0
In case you want to check if the stored value is not one of multiple values, you can use the Match Except condition.
Match Except works as a logical NOR for the given values.
It can also be described as a `NOT IN` operator.
You can apply it to keyword and integer payloads.
Example:
{{}}
In this example, the condition will be satisfied if the stored value is neither `black` nor `yellow`.
If the stored value is an array, it should have at least one value not matching any of the given values. E.g. if the stored value is `["black", "green"]`, the condition will be satisfied, because `"green"` does not match `"black"` nor `"yellow"`.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 413
Retrieved by: dense 10
Section: Filtering — Filtering conditions — Values count
--------------------------------------------------------------------------------

Filtering — Filtering conditions — Values count

In addition to the direct value comparison, it is also possible to filter by the amount of values.
For example, given the data:
```json_code_1```
We can perform the search only among the items with more than two comments:
{{}}
The result would be:
```json_code_2```
If stored value is not an array it is assumed that the amount of values is equals to 1.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1478
Retrieved by: sparse 1, hybrid 2, colbert 4
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates the batch search feature of a system. The batch search API allows you to send multiple search queries in a single request. Each search query includes a set of criteria to filter results and a limit on the number of expected results. By batching search requests together, the system can optimize processing by sharing intermediary results when queries have the same filters. This approach helps reduce network connections and improve overall efficiency, especially for complex filters. To use the batch search API, package your search requests together with the desired criteria.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1341
Retrieved by: sparse 4, hybrid 5, colbert 1
Section: Filtering — Progressive Filtering with the Batch Search API
--------------------------------------------------------------------------------

Filtering — Progressive Filtering with the Batch Search API

Even though filters are not used to rank results, you can use the batch search API to progressively relax filters. This is useful when you have strict filtering criteria that may not return results. Batching multiple search requests with progressively relaxed filters enables you to get results even when the strictest filter returns no results.
For example, the following batch search request first tries to find books that match all search terms in the title. The second search request relaxes the filter to match any of the search terms. The third search request removes the filter altogether:
{{}}
The response contains three separate result sets. You can return the first non-empty result set to the user, or you can use the three sets to assemble a single ranked list.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 418
Retrieved by: sparse 7
Section: Hybrid and Multi-Stage Queries
--------------------------------------------------------------------------------

Hybrid and Multi-Stage Queries

_Available as of v1.10.0_
With the introduction of multiple named vectors per point, there are use-cases when the best search is obtained by combining multiple queries,
or by performing the search in more than one stage.
Qdrant has a flexible and universal interface to make this possible, called `Query API` (API reference).
The main component for making the combinations of queries possible is the `prefetch` parameter, which enables making sub-requests.
Specifically, whenever a query has at least one prefetch, Qdrant will:
1. Perform the prefetch query (or queries),
2. Apply the main query over the results of its prefetch(es).
Additionally, prefetches can have prefetches themselves, so you can have nested prefetches.
Using offset parameter only affects the main query. This means that the prefetches must have a limit of at least limit + offset of the main query, otherwise you can get an empty result.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1272
Retrieved by: sparse 9
Section: Configure Multitenancy — Partition by payload
--------------------------------------------------------------------------------

Configure Multitenancy — Partition by payload

When an instance is shared between multiple users, you may need to partition vectors by user. This is done so that each user can only access their own vectors and can't see the vectors of other users.
 Note: The key doesn't necessarily need to be named group_id. You can choose a name that best suits your data structure and naming conventions.
{{}}
2. Use a filter along with `group_id` to filter vectors for each user.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 188
Retrieved by: sparse 10
Section: Use Collaborative Filtering to Build a Movie Recommendation System with Qdrant — Implementation — Define query
--------------------------------------------------------------------------------

Use Collaborative Filtering to Build a Movie Recommendation System with Qdrant — Implementation — Define query

In order to get recommendations, we need to find users with similar tastes to ours.
Let's describe our preferences by providing ratings for some of our favorite movies.
`1` indicates that we like the movie, `-1` indicates that we dislike it.
```python_code_1```
Click to see the code for to_vector
```python_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1339
Retrieved by: colbert 5
Section: Filtering — Full-Text Filtering — Text Processing
--------------------------------------------------------------------------------

Filtering — Full-Text Filtering — Text Processing

To enable efficient full-text filtering, Qdrant processes text strings by breaking them down into individual tokens (words) and applying several normalization steps. This process ensures that searches are more flexible and can match variations of words. At query time, Qdrant applies the same processing steps to the filter string, ensuring that the filter matches the indexed tokens correctly.
The following text processing steps are applied to text strings:
 The string is broken down into individual tokens (words) using a process called tokenization. By default, Qdrant uses the `word` tokenizer, which splits the string using word boundaries, discarding spaces, punctuation marks, and special characters.
 By default, each word is then converted to lowercase. Lowercasing the tokens allows Qdrant to ignore capitalization, making full-text filters case-insensitive.
 Optionally, Qdrant can remove diacritics (accents) from characters using a process called ASCII folding. This ensures that diacritics are ignored. As a result, filtering for the word "cafe" matches "café".
 Optionally, tokens can be reduced to their root form using a stemmer. This ensures that filtering for "running" also matches "run" and "ran". Because stemming is language-specific, if enabled, it must be configured for a specific language.
 Certain words like "the", "is", and "and" are very common in text and do not contribute much to the meaning of text. These words are called stopwords and can optionally be removed during indexing. Like stemming, stopword removal is language-specific. You can configure specific languages for stopword removal and/or provide a custom list of stopwords to remove.
 Optionally, you can enable phrase matching to allow filtering for multiple words in the exact same order as they appear in the original text.
These text processing steps can be configured when creating a full-text index. For example, to create a text index on the `title` field with ASCII folding enabled:
{{}}
When querying using this index, Qdrant automatically applies the same text processing steps to the filter string before matching it against the indexed tokens.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 510
Retrieved by: colbert 6
Section: Similarity search — Batch search API
--------------------------------------------------------------------------------

Similarity search — Batch search API

The batch search API enables to perform multiple search requests via a single request.
Its semantic is straightforward, `n` batched search requests are equivalent to `n` singular search requests.
This approach has several advantages. Logically, fewer network connections are required which can be very beneficial on its own.
More importantly, batched requests will be efficiently processed via the query planner which can detect and optimize requests if they have the same `filter`.
This can have a great effect on latency for non trivial filters as the intermediary results can be shared among the request.
In order to use it, simply pack together your search requests. All the regular attributes of a search request are of course available.
{{}}
The result of this API contains one array per search requests.
```json_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 403
Retrieved by: colbert 7
Section: Filtering — Filtering conditions — Nested object filter
--------------------------------------------------------------------------------

Filtering — Filtering conditions — Nested object filter

Available as of v1.2.0
By default, the conditions are taking into account the entire payload of a point.
For instance, given two points with the following payload:
```json_code_1```
The following query would match both points:
{{}}
This happens because both points are matching the two conditions:
 the "t-rex" matches food=meat on `diet[1].food` and likes=true on `diet[1].likes`
 the "diplodocus" matches food=meat on `diet[1].food` and likes=true on `diet[0].likes`
To retrieve only the points which are matching the conditions on an array element basis, that is the point with id 1 in this example, you would need to use a nested object filter.
Nested object filters allow arrays of objects to be queried independently of each other.
It is achieved by using the `nested` condition type formed by a payload key to focus on and a filter to apply.
The key should point to an array of objects and can be used with or without the bracket notation ("data" or "data[]").
{{}}
The matching logic is modified to be applied at the level of an array element within the payload.
Nested filters work in the same way as if the nested filter was applied to a single element of the array at a time.
Parent document is considered to match the condition if at least one element of the array matches the nested filter.
Limitations
The `has_id` condition is not supported within the nested object filter. If you need it, place it in an adjacent `must` clause.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1340
Retrieved by: colbert 9
Section: Filtering — Filter on Text Strings
--------------------------------------------------------------------------------

Filtering — Filter on Text Strings

To filter on text values in a payload field, first create a full-text index for that field. Next, you can use a `text` condition to query the collection with a filter for titles that contain the word "space":
{{}}
When filtering on more than one term, a `text` filter only matches fields that contain all the specified terms (logical `AND`). To match fields that contain any of the specified terms (logical `OR`), use the `text_any` condition:
{{}}
Qdrant also supports phrase filtering, enabling you to search for multiple words in the exact order they appear in the original text, with no other words in between. For example, a phrase filter for "time machine" matches against the title "The Time Machine" but would not match "The Time Travel Machine" (there's a word between "time" and "machine") nor "Machine Time" (the word order is incorrect).
The difference between phrase filtering and keyword filtering is that phrase filtering applies text processing and, as a result, is case-insensitive, while keyword filtering is case-sensitive and only matches the exact string. Additionally, keyword filtering has to match the entire string, whereas phrase filtering can match part of a larger string. So a keyword filter for "Space War" would not match "The Space War" because it doesn't match "The," but a phrase filter for "Space War" would.
Summarizing the differences between the four filtering methods for a multi-term filter on "Space War":
text_any — `space` OR `war` — Yes — Yes — Yes — Yes
text — `space` AND `war` — Yes — Yes — Yes — No
phrase — `"space war"` — Yes — Yes — No — No
keyword — `"Space War"` — Yes — No — No — No
To filter on phrases, use a `phrase` condition. This requires enabling phrase searching when creating the full-text index:
{{}}
Next, you can use a `phrase` condition to filter for titles that contain the exact phrase "time machine":
{{}}

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How to create a collection with multiple vector fields?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 357
Retrieved by: dense 1, sparse 1, hybrid 1, colbert 2
Section: Collections — Create a collection — Collection with multiple vectors
--------------------------------------------------------------------------------

Collections — Create a collection — Collection with multiple vectors

Available as of v0.10.0
It is possible to have multiple vectors per record.
This feature allows for multiple vector storages per collection.
To distinguish vectors in one record, they should have a unique name defined when creating the collection.
Each named vector in this mode has its distance and size:
{{}}
For rare use cases, it is possible to create a collection without any vector storage.
Available as of v1.1.1
For each named vector you can optionally specify
`hnsw_config` or
`quantization_config` to
deviate from the collection configuration. This can be useful to fine-tune
search performance on a vector level.
Available as of v1.2.0
Vectors all live in RAM for very quick access. On a per-vector basis you can set
`on_disk` to true to store all vectors on disk at all times. This will enable
the use of
memmaps,
which is suitable for ingesting a large amount of data.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1377
Retrieved by: dense 2, hybrid 3
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code defines a collection with the ability to store multiple vectors per record. Each vector, such as 'image' and 'text', has a unique name and is associated with specific distance and size parameters. The 'image' vector has a size of 4 and a distance metric of 'Dot', while the 'text' vector has a size of 8 and a distance metric of 'Cosine'. This feature enables the storage of different types of vectors within the same collection.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1378
Retrieved by: dense 3, sparse 2, hybrid 2, colbert 1
Section: Introduction
--------------------------------------------------------------------------------

Introduction

You can create a collection with named vectors in Qdrant by defining multiple vector spaces for different features or modalities like image and text. Each vector space can have a unique name along with specific size and distance calculation method. Additionally, you can include sparse vectors in the collection configuration for more efficient representation of data points.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 757
Retrieved by: dense 4, hybrid 6
Section: Twelve Labs — Creating a collection to insert the vectors
--------------------------------------------------------------------------------

Twelve Labs — Creating a collection to insert the vectors

```python_code_1```
```typescript_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1461
Retrieved by: dense 5
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Inserts a list of points along with their IDs, payload data (such as color), and vector coordinates into a collection for storage or processing. The points are structured as objects with different attributes like ID, payload, and vector to represent properties of each point.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1382
Retrieved by: dense 6, hybrid 8
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet is used to create a collection with a specific vector configuration. The collection is defined by its name, and the vectors within the collection are set to have a size of 300 dimensions and use the Cosine distance metric.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1394
Retrieved by: dense 7, hybrid 7, colbert 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet is used to create a collection with a specific vector configuration and additional metadata. The metadata is provided as a JSON object, allowing you to store custom information about the collection. In this example, we add two metadata fields.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1462
Retrieved by: dense 8
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet allows inserting a point with named vectors into a collection. The point has an ID and contains vectors labeled as "image," "text," and "text-sparse." The "image" vector has four values, the "text" vector has five values, and the "text-sparse" vector includes indices and corresponding values.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1862
Retrieved by: dense 9, colbert 8
Section: Implementing Vector Search with Reranking — Implementation — Creating a Collection
--------------------------------------------------------------------------------

Implementing Vector Search with Reranking — Implementation — Creating a Collection

A collection is basically a named group of points (vectors with data) that you can search through. All the vectors in a collection need to have the same size and be compared using one distance metric. Here’s how to create one:
```jsx_code_1```
Here, the vector size is set to 1024 to match our dense embeddings, and we’re using dot product as the distance metric—perfect for capturing the similarity between vectors, especially when they’re normalized.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1469
Retrieved by: dense 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet is for inserting a point with a multivector into a collection. It defines an operation to update a collection with a new point containing an ID and a vector represented by multiple arrays of values.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 383
Retrieved by: sparse 3, hybrid 5, colbert 7
Section: Explore the data — Recommendation API — Multiple vectors
--------------------------------------------------------------------------------

Explore the data — Recommendation API — Multiple vectors

Available as of v0.10.0
If the collection was created with multiple vectors, the name of the vector should be specified in the recommendation request:
{{}}
Parameter `using` specifies which stored vectors to use for the recommendation.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 547
Retrieved by: sparse 4, hybrid 4, colbert 3
Section: Vectors — Named Vectors
--------------------------------------------------------------------------------

Vectors — Named Vectors

In Qdrant, you can store multiple vectors of different sizes and types in the same data point. This is useful when you need to define your data with multiple embeddings to represent different features or modalities (e.g., image, text or video).
To store different vectors for each point, you need to create separate named vector spaces in the collection. You can define these vector spaces during collection creation and manage them independently.
Each vector should have a unique name. Vectors can represent different modalities and you can use different embedding models to generate them.
To create a collection with named vectors, you need to specify a configuration for each vector:
{{}}
To insert a point with named vectors:
{{}}
To search with named vectors (available in `query` API):
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 620
Retrieved by: sparse 5, hybrid 10
Section: Bulk Upload Vectors to a Qdrant Collection — Parallel upload into multiple shards
--------------------------------------------------------------------------------

Bulk Upload Vectors to a Qdrant Collection — Parallel upload into multiple shards

In Qdrant, each collection is split into shards. Each shard has a separate Write-Ahead-Log (WAL), which is responsible for ordering operations.
By creating multiple shards, you can parallelize upload of a large dataset. From 2 to 4 shards per one machine is a reasonable number.
```http_code_1```
```python_code_2```
```typescript_code_3```
```rust_code_4```
```java_code_5```
```csharp_code_6```
```go_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 580
Retrieved by: sparse 6, colbert 4
Section: Message Formats
--------------------------------------------------------------------------------

Message Formats

The connector supports messages in the following formats.
_Click each to expand._
 Unnamed/Default vector
Reference: Creating a collection with a default vector.
```json_code_1```
 Named multiple vectors
Reference: Creating a collection with multiple vectors.
```json_code_2```
 Sparse vectors
Reference: Creating a collection with sparse vectors.
```json_code_3```
 Multi-vectors
Reference:
 Multi-vectors
```json_code_4```
 Combination of named dense and sparse vectors
Reference:
 Creating a collection with multiple vectors.
 Creating a collection with sparse vectors.
```json_code_5```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 354
Retrieved by: sparse 7, hybrid 9
Section: Collections
--------------------------------------------------------------------------------

Collections

A collection is a named set of points (vectors with a payload) among which you can search. The vector of each point within the same collection must have the same dimensionality and be compared by a single metric. Named vectors can be used to have multiple vectors in a single point, each of which can have their own dimensionality and metric requirements.
Distance metrics are used to measure similarities among vectors.
The choice of metric depends on the way vectors obtaining and, in particular, on the method of neural network encoder training.
Qdrant supports these most popular types of metrics:
* Dot product: `Dot` [[wiki]](
* Cosine similarity: `Cosine` [[wiki]](
* Euclidean distance: `Euclid` [[wiki]](
* Manhattan distance: `Manhattan` [[wiki]](
For search efficiency, Cosine similarity is implemented as dot-product over normalized vectors. Vectors are automatically normalized during upload
In addition to metrics and vector size, each collection uses its own set of parameters that controls collection optimization, index construction, and vacuum.
These settings can be changed at any time by a corresponding request.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 594
Retrieved by: sparse 8, colbert 6
Section: Usage with Qdrant — Message Formats
--------------------------------------------------------------------------------

Usage with Qdrant — Message Formats

This sink connector supports messages with dense/sparse/multi vectors.
_Click each to expand._
 Unnamed/Default vector
Reference: Creating a collection with a default vector.
```json_code_1```
 Named multiple vectors
Reference: Creating a collection with multiple vectors.
```json_code_2```
 Sparse vectors
Reference: Creating a collection with sparse vectors.
```json_code_3```
 Multi-vector
```json_code_4```
 Combination of named dense and sparse vectors
Reference:
 Creating a collection with multiple vectors.
 Creating a collection with sparse vectors.
```json_code_5```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1395
Retrieved by: sparse 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

To utilize multivectors in Qdrant, you can create a collection with a specified configuration. This configuration includes defining the size of the vectors (128 in this case), setting the distance metric as cosine, and enabling the multivector feature with the comparator function as `max_sim`. The `max_sim` function calculates the similarity between matrices of vectors by summing the maximum similarities between each pair of vectors in the matrices. This allows for scenarios where you may have multiple representations of the same object or late interaction embeddings, such as text embedding models outputting multiple vectors for a single text sequence.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1512
Retrieved by: sparse 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

The code snippet demonstrates how to make a query to explore points in a collection based on named vectors. In this case, the query is configured to recommend vectors specified as 'positive' and 'negative'. By setting the 'using' parameter to "image" and limiting the results to 10, you can retrieve relevant data for the specified vectors in the collection. This feature is available starting from version 0.10.0 and allows for more granular recommendation requests when dealing with multiple vectors in a collection.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 602
Retrieved by: colbert 5
Section: Apache Spark — Usage — Loading data
--------------------------------------------------------------------------------

Apache Spark — Usage — Loading data

Before loading the data using this connector, a collection has to be created in advance with the appropriate vector dimensions and configurations.
The connector supports ingesting multiple named/unnamed, dense/sparse vectors.
_Click each to expand._
 Unnamed/Default vector
```python_code_1```
 Named vector
```python_code_2```
> #### NOTE
>
> The `embedding_field` and `vector_name` options are maintained for backward compatibility. It is recommended to use `vector_fields` and `vector_names` for named vectors as shown below.
 Multiple named vectors
```python_code_3```
 Sparse vectors
```python_code_4```
 Multiple sparse vectors
```python_code_5```
 Combination of named dense and sparse vectors
```python_code_6```
 Multi-vectors
```python_code_7```
 Multiple Multi-vectors
```python_code_8```
 No vectors Entire dataframe is stored as payload
```python_code_9```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 488
Retrieved by: colbert 9
Section: Points — Upload points — Named vectors
--------------------------------------------------------------------------------

Points — Upload points — Named vectors

_Available as of v0.10.0_
If the collection was created with multiple vectors, each vector data can be provided using the vector's name:
{{}}
_Available as of v1.2.0_
Named vectors are optional. When uploading points, some vectors may be omitted.
For example, you can upload one point with only the `image` vector and a second
one with only the `text` vector.
When uploading a point with an existing ID, the existing point is deleted first,
then it is inserted with just the specified vectors. In other words, the entire
point is replaced, and any unspecified vectors are set to null. To keep existing
vectors unchanged and only update specified vectors, see update vectors.

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How to configure vector size and distance metric?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 1393
Retrieved by: dense 1, sparse 2, hybrid 1, colbert 2
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet creates a collection with specific configurations for vectors and optimizers. It sets the vector size to 768 and the distance metric to Cosine. It also configures the optimizers with a default segment number of 2 and a maximum segment size of 5000000. These settings aim to optimize throughput by utilizing fewer segments to handle parallel requests and benefit from large segment sizes for optimized index performance.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1386
Retrieved by: dense 2, sparse 1, hybrid 2, colbert 3
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code configures a collection named `{collection_name}` with vectors of size 1536 and a distance metric of cosine. The collection is set up for binary quantization with the setting `always_ram` set to true. To enable binary quantization for an existing collection, a PATCH request or an `update_collection` method can be used, omitting the vector configuration as it is already defined.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 261
Retrieved by: dense 3, sparse 10, hybrid 5
Section: Build Your First Semantic Search Engine in 5 Minutes — 4. Create a collection
--------------------------------------------------------------------------------

Build Your First Semantic Search Engine in 5 Minutes — 4. Create a collection

All data in Qdrant is organized by collections. In this case, you are storing books, so we are calling it `my_books`.
```python_code_1```
 The `vector_size` parameter defines the size of the vectors for a specific collection. If their size is different, it is impossible to calculate the distance between them. 384 is the encoder output dimensionality. You can also use model.get_sentence_embedding_dimension() to get the dimensionality of the model you are using.
 The `distance` parameter lets you specify the function used to measure the distance between two points.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1397
Retrieved by: dense 4, sparse 4, hybrid 3, colbert 1
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet is configuring a collection with product quantization. It defines the vector size and distance metric for vectors in the collection, and specifies parameters for product quantization such as compression and storage settings. It highlights the process of setting up product quantization and mentions the specific details to include in the configuration. It also suggests using a PATCH request or the corresponding method for updating an existing collection without modifying the vector configuration.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1382
Retrieved by: dense 5, sparse 8, hybrid 6, colbert 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet is used to create a collection with a specific vector configuration. The collection is defined by its name, and the vectors within the collection are set to have a size of 300 dimensions and use the Cosine distance metric.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1377
Retrieved by: dense 6, sparse 9, hybrid 8, colbert 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code defines a collection with the ability to store multiple vectors per record. Each vector, such as 'image' and 'text', has a unique name and is associated with specific distance and size parameters. The 'image' vector has a size of 4 and a distance metric of 'Dot', while the 'text' vector has a size of 8 and a distance metric of 'Cosine'. This feature enables the storage of different types of vectors within the same collection.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1730
Retrieved by: dense 7
Section: Vectorize.io — Further Reading
--------------------------------------------------------------------------------

Vectorize.io — Further Reading

Vectorize Documentation
 Vectorize Tutorials.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1375
Retrieved by: dense 8, sparse 3, hybrid 4, colbert 5
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates how to configure Qdrant to create a collection with vectors stored as uint8 datatypes. This is useful when dealing with pre-quantized embeddings, such as uint8 embeddings provided by embedding providers like Cohere. The vectors in the collection will have a size of 1024 and will be using the Cosine distance metric for similarity comparison.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1374
Retrieved by: dense 9, sparse 5, hybrid 7, colbert 4
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code sets up a collection with vectors containing 128 dimensions and a cosine distance metric. It configures the datatype for dense vectors to be Float16, which consumes less memory than Float32 without significant impact on search quality. Additionally, it specifies Float16 as the datatype for sparse text vectors in the collection.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 934
Retrieved by: dense 10, colbert 8
Section: Frequently Asked Questions: General Topics — Vectors — Vectors in the collection don't match what I uploaded.
--------------------------------------------------------------------------------

Frequently Asked Questions: General Topics — Vectors — Vectors in the collection don't match what I uploaded.

There are two possible reasons for this:
 You used the `Cosine` distance metric in the collection settings. In this case, Qdrant pre-normalizes your vectors for faster distance computation. If you strictly need the original vectors to be preserved, consider using the `Dot` distance metric instead.
 You used the `uint8` datatype to store vectors. `uint8` requires a special format for input values, which might not be compatible with the typical output of embedding models.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1862
Retrieved by: sparse 6, hybrid 9, colbert 6
Section: Implementing Vector Search with Reranking — Implementation — Creating a Collection
--------------------------------------------------------------------------------

Implementing Vector Search with Reranking — Implementation — Creating a Collection

A collection is basically a named group of points (vectors with data) that you can search through. All the vectors in a collection need to have the same size and be compared using one distance metric. Here’s how to create one:
```jsx_code_1```
Here, the vector size is set to 1024 to match our dense embeddings, and we’re using dot product as the distance metric—perfect for capturing the similarity between vectors, especially when they’re normalized.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1395
Retrieved by: sparse 7, hybrid 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

To utilize multivectors in Qdrant, you can create a collection with a specified configuration. This configuration includes defining the size of the vectors (128 in this case), setting the distance metric as cosine, and enabling the multivector feature with the comparator function as `max_sim`. The `max_sim` function calculates the similarity between matrices of vectors by summing the maximum similarities between each pair of vectors in the matrices. This allows for scenarios where you may have multiple representations of the same object or late interaction embeddings, such as text embedding models outputting multiple vectors for a single text sequence.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1107
Retrieved by: colbert 7
Section: Mastra — Methods — `createIndex()`
--------------------------------------------------------------------------------

Mastra — Methods — `createIndex()`

`indexName` — `string` — Name of the index to create
`dimension` — `number` — Vector dimension size
`metric` — `string` — Distance metric for similarity search — `cosine`

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How to add a sparse vector to an existing collection?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 1463
Retrieved by: dense 1, sparse 4, hybrid 1, colbert 7
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet showcases a system for inserting points with sparse vectors into collections. Each point consists of an ID and a vector, where the vector data includes the indices and corresponding values. The `indices` and `values` arrays are required to have the same length, with unique `indices`. If the `indices` are not sorted, the system will internally sort them. Sparse vectors can be uploaded in a similar manner as dense vectors.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 359
Retrieved by: dense 2, sparse 2, hybrid 2, colbert 1
Section: Collections — Create a collection — Collection with sparse vectors
--------------------------------------------------------------------------------

Collections — Create a collection — Collection with sparse vectors

Available as of v1.7.0
Qdrant supports sparse vectors as a first-class citizen.
Sparse vectors are useful for text search, where each word is represented as a separate dimension.
Collections can contain sparse vectors as additional named vectors along side regular dense vectors in a single point.
Unlike dense vectors, sparse vectors must be named.
And additionally, sparse vectors and dense vectors must have different names within a collection.
{{}}
Outside of a unique name, there are no required configuration parameters for sparse vectors.
The distance function for sparse vectors is always `Dot` and does not need to be specified.
However, there are optional parameters to tune the underlying sparse vector index.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1464
Retrieved by: dense 3, hybrid 6
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Inserts a point with a sparse vector, identified by its ID and containing indices and corresponding values, into the specified collection.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1383
Retrieved by: dense 4, sparse 5, hybrid 4, colbert 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates creating a collection in Qdrant with support for sparse vectors. Sparse vectors are useful for text search, representing each word as a separate dimension. This feature allows collections to contain both sparse vectors and regular dense vectors in one point. Sparse vectors need to be named uniquely within a collection, separate from the names of dense vectors.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1462
Retrieved by: dense 5, hybrid 7
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet allows inserting a point with named vectors into a collection. The point has an ID and contains vectors labeled as "image," "text," and "text-sparse." The "image" vector has four values, the "text" vector has five values, and the "text-sparse" vector includes indices and corresponding values.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1385
Retrieved by: dense 6, sparse 1, hybrid 3, colbert 4
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Category: Create Collection - Sparse Vector Index on Disk

This code snippet demonstrates creating a collection in Qdrant with a configuration for indexing sparse vectors. When a sparse vector index is used with the "on_disk" option set to false, it indicates that the index will be stored in memory rather than on disk. Sparse vector indexing in Qdrant is exact and does not involve approximation algorithms. The indexing method employed is similar to inverted indexes commonly found in text search engines. By specifying the configuration for sparse vectors in a collection, you can take advantage of efficient indexing optimized for vectors with a high number of zero values. This can lead to more compact and streamlined index structures, especially when managing collections that store both dense and sparse vectors.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1374
Retrieved by: dense 7, hybrid 8
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code sets up a collection with vectors containing 128 dimensions and a cosine distance metric. It configures the datatype for dense vectors to be Float16, which consumes less memory than Float32 without significant impact on search quality. Additionally, it specifies Float16 as the datatype for sparse text vectors in the collection.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1378
Retrieved by: dense 8, sparse 3, hybrid 5, colbert 2
Section: Introduction
--------------------------------------------------------------------------------

Introduction

You can create a collection with named vectors in Qdrant by defining multiple vector spaces for different features or modalities like image and text. Each vector space can have a unique name along with specific size and distance calculation method. Additionally, you can include sparse vectors in the collection configuration for more efficient representation of data points.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1587
Retrieved by: dense 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Update collection parameters to adjust the optimizer's configuration. In this case, the code snippet demonstrates how to patch the collection by setting an indexing threshold of 10000 for more efficient initial loading of vectors. This allows you to optimize resource usage by enabling indexing selectively based on the number of vectors stored in each segment.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1377
Retrieved by: dense 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code defines a collection with the ability to store multiple vectors per record. Each vector, such as 'image' and 'text', has a unique name and is associated with specific distance and size parameters. The 'image' vector has a size of 4 and a distance metric of 'Dot', while the 'text' vector has a size of 8 and a distance metric of 'Cosine'. This feature enables the storage of different types of vectors within the same collection.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1900
Retrieved by: sparse 6, hybrid 9, colbert 5
Section: Using Cloud Inference with Qdrant for Vector Search — Create a Collection
--------------------------------------------------------------------------------

Using Cloud Inference with Qdrant for Vector Search — Create a Collection

Qdrant stores vectors and associated metadata in collections. A collection requires vector parameters to be set during creation. In this case, let's set up a collection using `BM25` for sparse vectors and `all-minilm-l6-v2` for dense vectors. BM25 uses the Inverse Document Frequency to reduce the weight of common terms that appear in many documents while boosting the importance of rare terms that are more discriminative for retrieval. Qdrant will handle the calculations of the IDF term if we enable that in the configuration of the `bm25_sparse_vector` named sparse vector.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 920
Retrieved by: sparse 7, hybrid 10
Section: Movie Recommendation System — Implementation — Data preparation
--------------------------------------------------------------------------------

Movie Recommendation System — Implementation — Data preparation

Now you will transform user ratings into sparse vectors, where each vector represents ratings for different movies. This step prepares the data for indexing in Qdrant.
First, create a collection with configured sparse vectors. For sparse vectors, you don't need to specify the dimension, because it's extracted from the data automatically.
```python_code_1```
Connect to Qdrant and create a collection called movielens:
```python_code_2```
Upload user ratings to the movielens collection in Qdrant as sparse vectors, along with user metadata. This step populates the database with the necessary data for recommendation generation.
```python_code_3```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1376
Retrieved by: sparse 8
Section: Introduction
--------------------------------------------------------------------------------

Introduction

When working with vectors in a collection, you can specify the datatype as Uint8 for both dense and sparse vectors. Uint8 represents integer numbers from 0 to 255, which is different from floating-point numbers. 

For dense vectors, make sure the values fall within the range of 0 to 255. If the embeddings generated by your model are not in this range, you will need to quantize the values to convert them. 

Some embedding providers may offer pre-quantized embeddings like Cohere int8 & binary embeddings. If not, you will have to perform quantization yourself.

It's important to note that while dense vectors must be in the 0 to 255 range, sparse vectors allow for in-flight quantization. This distinction should be considered when handling Uint8 vectors.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1888
Retrieved by: sparse 9
Section: Qdrant on Databricks — Uploading the data to Qdrant
--------------------------------------------------------------------------------

Qdrant on Databricks — Uploading the data to Qdrant

Create a Qdrant collection:
 Follow the documentation to create a collection with the appropriate configurations. Here's an example request to support both dense and sparse vectors:
```json_code_1```
 Upload the dataframe to Qdrant:
```python_code_2```
 You can find the list of the Spark connector configuration options here.
Ensure to replace the placeholder values (``, ``, ``) with your actual values. If the `id_field` option is not specified, Qdrant Spark connector generates random UUIDs for each point.
The command output you should see is similar to:
```console_code_3```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1428
Retrieved by: sparse 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet uses the Qdrant and FastEmbed integration to infer and upsert documents into a collection configured for BM25 sparse vectors. Each document is converted into a sparse BM25 vector, with the conversion incorporating the avg_len parameter of the BM25 scoring formula — the average document length in the corpus — which must be provided by the user. The resulting vector and the document’s text, stored as payload, are then upserted to the collection.

```python_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 445
Retrieved by: colbert 3
Section: Indexing — Sparse Vector Index
--------------------------------------------------------------------------------

Indexing — Sparse Vector Index

Available as of v1.7.0
Sparse vectors in Qdrant are indexed with a special data structure, which is optimized for vectors that have a high proportion of zeroes. In some ways, this indexing method is similar to the inverted index, which is used in text search engines.
 A sparse vector index in Qdrant is exact, meaning it does not use any approximation algorithms.
 All sparse vectors added to the collection are immediately indexed in the mutable version of a sparse index.
With Qdrant, you can benefit from a more compact and efficient immutable sparse index, which is constructed during the same optimization process as the dense vector index.
This approach is particularly useful for collections storing both dense and sparse vectors.
To configure a sparse vector index, create a collection with the following parameters:
{{}}`
The following parameters may affect performance:
 `on_disk: true` The index is stored on disk, which lets you save memory. This may slow down search performance.
 `on_disk: false` The index is still persisted on disk, but it is also loaded into memory for faster search.
Unlike a dense vector index, a sparse vector index does not require a predefined vector size. It automatically adjusts to the size of the vectors added to the collection.
Note: A sparse vector index only supports dot-product similarity searches. It does not support other distance metrics.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 545
Retrieved by: colbert 6
Section: Vectors — Vector Types — Sparse Vectors
--------------------------------------------------------------------------------

Vectors — Vector Types — Sparse Vectors

Sparse vectors are a special type of vectors.
Mathematically, they are the same as dense vectors, but they contain many zeros so they are stored in a special format.
Sparse vectors in Qdrant don't have a fixed length, as it is dynamically allocated during vector insertion.
The amount of non-zero values in sparse vectors is currently limited to u32 datatype range (4294967295).
In order to define a sparse vector, you need to provide a list of non-zero elements and their indexes.
```json_code_1```
Sparse vectors in Qdrant are kept in special storage and indexed in a separate index, so their configuration is different from dense vectors.
To create a collection with sparse vectors:
{{}}
Insert a point with a sparse vector into the created collection:
{{}}
Now you can run a search with sparse vectors:
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 594
Retrieved by: colbert 8
Section: Usage with Qdrant — Message Formats
--------------------------------------------------------------------------------

Usage with Qdrant — Message Formats

This sink connector supports messages with dense/sparse/multi vectors.
_Click each to expand._
 Unnamed/Default vector
Reference: Creating a collection with a default vector.
```json_code_1```
 Named multiple vectors
Reference: Creating a collection with multiple vectors.
```json_code_2```
 Sparse vectors
Reference: Creating a collection with sparse vectors.
```json_code_3```
 Multi-vector
```json_code_4```
 Combination of named dense and sparse vectors
Reference:
 Creating a collection with multiple vectors.
 Creating a collection with sparse vectors.
```json_code_5```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 580
Retrieved by: colbert 10
Section: Message Formats
--------------------------------------------------------------------------------

Message Formats

The connector supports messages in the following formats.
_Click each to expand._
 Unnamed/Default vector
Reference: Creating a collection with a default vector.
```json_code_1```
 Named multiple vectors
Reference: Creating a collection with multiple vectors.
```json_code_2```
 Sparse vectors
Reference: Creating a collection with sparse vectors.
```json_code_3```
 Multi-vectors
Reference:
 Multi-vectors
```json_code_4```
 Combination of named dense and sparse vectors
Reference:
 Creating a collection with multiple vectors.
 Creating a collection with sparse vectors.
```json_code_5```

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How to delete specific points by ID?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 495
Retrieved by: dense 1, sparse 4, hybrid 2, colbert 7
Section: Points — Delete points
--------------------------------------------------------------------------------

Points — Delete points

REST API (Schema):
{{}}
Alternative way to specify which points to remove is to use filter.
{{}}
This example removes all points with `{ "color": "red" }` from the collection.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 493
Retrieved by: dense 2, sparse 6, hybrid 4, colbert 9
Section: Points — Modify points — Delete vectors
--------------------------------------------------------------------------------

Points — Modify points — Delete vectors

_Available as of v1.2.0_
This method deletes just the specified vectors from the given points. Other
vectors are kept unchanged. Points are never deleted.
REST API (Schema):
{{}}
To delete entire points, see deleting points.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1418
Retrieved by: dense 3, sparse 3, hybrid 3, colbert 1
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet pertains to deleting specific keys from the payload of points. It specifies the keys to be deleted as 'color' and 'price' from the points with IDs 0, 3, and 100 within a collection.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1421
Retrieved by: dense 4, sparse 1, hybrid 1, colbert 3
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates a way to delete specific vectors from specified points in a collection. It allows users to remove selected vectors while retaining other vectors associated with the points. The points themselves are not deleted during this process, only certain vectors are removed. This method is available starting from version 1.2.0.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 479
Retrieved by: dense 5, sparse 8, hybrid 6, colbert 5
Section: Payload — Update payload — Delete payload keys
--------------------------------------------------------------------------------

Payload — Update payload — Delete payload keys

Delete specific payload keys from points.
REST API (Schema):
{{}}
Alternatively, you can use filters to delete payload keys from the points.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 478
Retrieved by: dense 6, hybrid 8, colbert 10
Section: Payload — Update payload — Clear payload
--------------------------------------------------------------------------------

Payload — Update payload — Clear payload

This method removes all payload keys from specified points
REST API (Schema):
{{}}
You can also use models.FilterSelector to remove the points matching given filter criteria, instead of providing the ids.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1420
Retrieved by: dense 7, sparse 2, hybrid 5, colbert 2
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code represents a task to delete specific points from a collection. The API endpoint allows you to send a POST request to delete points with the specified indexes (0, 3, and 100) from a collection specified by its name.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1708
Retrieved by: dense 8
Section: N8N — Operations — Vector
--------------------------------------------------------------------------------

N8N — Operations — Vector

Update Vectors Update vectors for existing points
 Delete Vectors Remove vectors from points

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 497
Retrieved by: dense 9
Section: Points — Retrieve points
--------------------------------------------------------------------------------

Points — Retrieve points

There is a method for retrieving points by their ids.
REST API (Schema):
{{}}
This method has additional parameters `with_vectors` and `with_payload`.
Using these parameters, you can select parts of the point you want as a result.
Excluding helps you not to waste traffic transmitting useless data.
The single point can also be retrieved via the API:
REST API (Schema):
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1419
Retrieved by: dense 10, sparse 10, hybrid 10, colbert 4
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates an alternative way to specify and remove certain points from a collection by filtering based on a specific key-value pair. In this case, the filter is set to remove points with the key "color" that match the value "red".

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1465
Retrieved by: sparse 5, hybrid 7
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet allows you to insert a point with a specific ID into a collection. The point contains a payload with color information and a vector represented by an array of three values. The ID of the point is a UUID, which can be used as a unique identifier for the point within the collection.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1707
Retrieved by: sparse 7, hybrid 9, colbert 8
Section: N8N — Operations — Point
--------------------------------------------------------------------------------

N8N — Operations — Point

Upsert Points Insert or update points in a collection
 Retrieve Point Get a single point by ID
 Retrieve Points Get multiple points by their IDs
 Delete Points Remove points from a collection
 Count Points Count points in a collection with optional filtering
 Scroll Points Scroll through all points in a collection
 Batch Update Points Perform multiple point operations in a single request

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1513
Retrieved by: sparse 9, colbert 6
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet represents a method for retrieving points by their ids from a collection. The function allows users to specify the ids of the points to be retrieved as part of a POST request to the specified endpoint. The provided ids are an array of integers, indicating the specific points to retrieve.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How to remove only vectors but keep payload?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 1708
Retrieved by: dense 1, hybrid 2
Section: N8N — Operations — Vector
--------------------------------------------------------------------------------

N8N — Operations — Vector

Update Vectors Update vectors for existing points
 Delete Vectors Remove vectors from points

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1421
Retrieved by: dense 2, hybrid 3, colbert 2
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates a way to delete specific vectors from specified points in a collection. It allows users to remove selected vectors while retaining other vectors associated with the points. The points themselves are not deleted during this process, only certain vectors are removed. This method is available starting from version 1.2.0.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 478
Retrieved by: dense 3, hybrid 6, colbert 10
Section: Payload — Update payload — Clear payload
--------------------------------------------------------------------------------

Payload — Update payload — Clear payload

This method removes all payload keys from specified points
REST API (Schema):
{{}}
You can also use models.FilterSelector to remove the points matching given filter criteria, instead of providing the ids.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 479
Retrieved by: dense 4, hybrid 7
Section: Payload — Update payload — Delete payload keys
--------------------------------------------------------------------------------

Payload — Update payload — Delete payload keys

Delete specific payload keys from points.
REST API (Schema):
{{}}
Alternatively, you can use filters to delete payload keys from the points.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 493
Retrieved by: dense 5, hybrid 10, colbert 6
Section: Points — Modify points — Delete vectors
--------------------------------------------------------------------------------

Points — Modify points — Delete vectors

_Available as of v1.2.0_
This method deletes just the specified vectors from the given points. Other
vectors are kept unchanged. Points are never deleted.
REST API (Schema):
{{}}
To delete entire points, see deleting points.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1710
Retrieved by: dense 6
Section: N8N — Operations — Payload
--------------------------------------------------------------------------------

N8N — Operations — Payload

Set Payload Set payload for points
 Overwrite Payload Replace entire payload for points
 Delete Payload Remove payload from points
 Clear Payload Clear all payload fields
 Payload Facets Get payload field statistics
 Create Payload Index Create an index for payload fields
 Delete Payload Index Remove a payload field index

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 617
Retrieved by: dense 7
Section: Bulk Upload Vectors to a Qdrant Collection — Choose an Indexing Strategy — Defer HNSW graph construction (`m: 0`)
--------------------------------------------------------------------------------

Bulk Upload Vectors to a Qdrant Collection — Choose an Indexing Strategy — Defer HNSW graph construction (`m: 0`)

For dense vectors, setting the HNSW `m` parameter to `0` disables index building entirely. Vectors will still be stored, but not indexed until you enable indexing later.
```http_code_1```
```python_code_2```
```typescript_code_3```
```rust_code_4```
```java_code_5```
```csharp_code_6```
```go_code_7```
Once ingestion is complete, re-enable HNSW by setting `m` to your production value (usually 16 or 32).
```http_code_8```
```python_code_9```
```typescript_code_10```
```rust_code_11```
```java_code_12```
```csharp_code_13```
```go_code_14```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 508
Retrieved by: dense 8, sparse 3, hybrid 4, colbert 3
Section: Similarity search — Search API — Payload and vector in the result
--------------------------------------------------------------------------------

Similarity search — Search API — Payload and vector in the result

By default, retrieval methods do not return any stored information such as
payload and vectors. Additional parameters `with_vectors` and `with_payload`
alter this behavior.
Example:
{{}}
You can use `with_payload` to scope to or filter a specific payload subset.
You can even specify an array of items to include, such as `city`,
`village`, and `town`:
{{}}
Or use `include` or `exclude` explicitly. For example, to exclude `city`:
{{}}
It is possible to target nested fields using a dot notation:
* `payload.nested_field` for a nested field
* `payload.nested_array[].sub_field` for projecting nested fields within an array
Accessing array elements by index is currently not supported.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 447
Retrieved by: dense 9
Section: Indexing — Filterable Index
--------------------------------------------------------------------------------

Indexing — Filterable Index

Separately, a payload index and a vector index cannot solve the problem of search using the filter completely.
In the case of high-selectivity (weak) filters, you can use the HNSW index as it is.
In the case of low-selectivity (strict) filters, you can use the payload index and complete rescore.
However, for cases in the middle, this approach does not work well.
On the one hand, we cannot apply a full scan on too many vectors.
On the other hand, the HNSW graph starts to fall apart when using too strict filters.
Qdrant solves this problem by extending the HNSW graph with additional edges based on the stored payload values.
Extra edges allow you to efficiently search for nearby vectors using the HNSW index and apply filters as you search in the graph.
You can find more information on this approach in our article.
However, in some cases, these additional edges might not be enough.
These extra edges are added per each payload index separately, but not per each possible combination of them.
So, a combination of two or more strict filters still might lead to disconnected graph components.
The same may happen when having a large number of soft-deleted points in the graph.
In such cases, the ACORN Search Algorithm can be used.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1374
Retrieved by: dense 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code sets up a collection with vectors containing 128 dimensions and a cosine distance metric. It configures the datatype for dense vectors to be Float16, which consumes less memory than Float32 without significant impact on search quality. Additionally, it specifies Float16 as the datatype for sparse text vectors in the collection.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 475
Retrieved by: sparse 1, hybrid 1, colbert 1
Section: Payload — Update payload
--------------------------------------------------------------------------------

Payload — Update payload

Updating payloads in Qdrant offers flexible methods to manage vector metadata. The set payload method updates specific fields while keeping others unchanged, while the overwrite method replaces the entire payload. Developers can also use clear payload to remove all metadata or delete fields to remove specific keys without affecting the rest. These options provide precise control for adapting to dynamic datasets.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 434
Retrieved by: sparse 2, hybrid 5
Section: Indexing — Payload Index — On-disk payload index
--------------------------------------------------------------------------------

Indexing — Payload Index — On-disk payload index

Available as of v1.11.0
By default all payload-related structures are stored in memory. In this way, the vector index can quickly access payload values during search.
As latency in this case is critical, it is recommended to keep hot payload indexes in memory.
There are, however, cases when payload indexes are too large or rarely used. In those cases, it is possible to store payload indexes on disk.
 On-disk payload index might affect cold requests latency, as it requires additional disk I/O operations.
To configure on-disk payload index, you can use the following index parameters:
{{}}
Payload index on-disk is supported for the following types:
* `keyword`
* `integer`
* `float`
* `datetime`
* `uuid`
* `text`
* `geo`
The list will be extended in future versions.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1409
Retrieved by: sparse 4, hybrid 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Create a payload index by specifying the field name and setting its schema to 'keyword'. This allows for more efficient searching with filters in Qdrant. Indexing fields can impact the vector index as well. It is recommended to index fields that might heavily influence search results. For example, indexing the object ID, which is unique for each record, will be more efficient than indexing by color with only a few possible values. Qdrant will prioritize using the most restrictive index in compound queries involving multiple fields.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 497
Retrieved by: sparse 5
Section: Points — Retrieve points
--------------------------------------------------------------------------------

Points — Retrieve points

There is a method for retrieving points by their ids.
REST API (Schema):
{{}}
This method has additional parameters `with_vectors` and `with_payload`.
Using these parameters, you can select parts of the point you want as a result.
Excluding helps you not to waste traffic transmitting useless data.
The single point can also be retrieved via the API:
REST API (Schema):
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1390
Retrieved by: sparse 6, hybrid 8
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Configure Qdrant to optimize performance by bypassing the creation of a global vector index for the entire collection. Instead, focus on indexing vectors for individual groups separately to enhance the speed of the process. Update the HNSW configuration by setting `payload_m` to a specific value, like 16, and ensuring `m` in the configuration is set to 0 to disable the global index construction.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 537
Retrieved by: sparse 7
Section: Storage
--------------------------------------------------------------------------------

Storage

All data within one collection is divided into segments.
Each segment has its independent vector and payload storage as well as indexes.
Data stored in segments usually do not overlap.
However, storing the same point in different segments will not cause problems since the search contains a deduplication mechanism.
The segments consist of vector and payload storages, vector and payload indexes, and id mapper, which stores the relationship between internal and external ids.
A segment can be `appendable` or `non-appendable` depending on the type of storage and index used.
You can freely add, delete and query data in the `appendable` segment.
With `non-appendable` segment can only read and delete data.
The configuration of the segments in the collection can be different and independent of one another, but at least one `appendable' segment must be present in a collection.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 540
Retrieved by: sparse 8, colbert 8
Section: Storage — Payload storage
--------------------------------------------------------------------------------

Storage — Payload storage

Qdrant supports two types of payload storages: InMemory and OnDisk.
InMemory payload storage is organized in the same way as in-memory vectors.
The payload data is loaded into RAM at service startup while disk and Gridstore are used for persistence only.
This type of storage works quite fast, but it may require a lot of space to keep all the data in RAM, especially if the payload has large values attached abstracts of text or even images.
In the case of large payload values, it might be better to use OnDisk payload storage.
This type of storage will read and write payload directly to RocksDB, so it won't require any significant amount of RAM to store.
The downside, however, is the access latency.
If you need to query vectors with some payload-based conditions checking values stored on disk might take too much time.
In this scenario, we recommend creating a payload index for each field used in filtering conditions to avoid disk access.
Once you create the field index, Qdrant will preserve all values of the indexed field in RAM regardless of the payload storage type.
You can specify the desired type of payload storage with configuration file or with collection parameter `on_disk_payload` during creation of the collection.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 480
Retrieved by: sparse 9
Section: Payload — Payload indexing
--------------------------------------------------------------------------------

Payload — Payload indexing

To search more efficiently with filters, Qdrant allows you to create indexes for payload fields by specifying the name and type of field it is intended to be.
The indexed fields also affect the vector index. See Indexing for details.
In practice, we recommend creating an index on those fields that could potentially constrain the results the most.
For example, using an index for the object ID will be much more efficient, being unique for each record, than an index by its color, which has only a few possible values.
In compound queries involving multiple fields, Qdrant will attempt to use the most restrictive index first.
To create index for the field, you can use the following:
REST API (Schema)
{{}}
The index usage flag is displayed in the payload schema with the collection info API.
Payload schema example:
```json_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1504
Retrieved by: sparse 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates the functionality to include payload and vectors in the query results. By setting the `with_vectors` and `with_payload` parameters to true, additional stored information is returned alongside the query results. This allows for a more detailed and comprehensive retrieval process.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1272
Retrieved by: colbert 4
Section: Configure Multitenancy — Partition by payload
--------------------------------------------------------------------------------

Configure Multitenancy — Partition by payload

When an instance is shared between multiple users, you may need to partition vectors by user. This is done so that each user can only access their own vectors and can't see the vectors of other users.
 Note: The key doesn't necessarily need to be named group_id. You can choose a name that best suits your data structure and naming conventions.
{{}}
2. Use a filter along with `group_id` to filter vectors for each user.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1273
Retrieved by: colbert 5
Section: Configure Multitenancy — Calibrate performance
--------------------------------------------------------------------------------

Configure Multitenancy — Calibrate performance

The speed of indexation may become a bottleneck in this case, as each user's vector will be indexed into the same collection. To avoid this bottleneck, consider _bypassing the construction of a global vector index_ for the entire collection and building it only for individual groups instead.
By adopting this strategy, Qdrant will index vectors for each user independently, significantly accelerating the process.
To implement this approach, you should:
1. Set `payload_m` in the HNSW configuration to a non-zero value, such as 16.
2. Set `m` in hnsw config to 0. This will disable building global index for the whole collection.
{{}}
3. Create keyword payload index for `group_id` field.
 is_tenant parameter is available as of v1.11.0. Previous versions should use default options for keyword index creation.
{{}}
`is_tenant=true` parameter is optional, but specifying it provides storage with additional information about the usage patterns the collection is going to use.
When specified, storage structure will be organized in a way to co-locate vectors of the same tenant together, which can significantly improve performance by utilizing sequential reads during queries.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 501
Retrieved by: colbert 7
Section: Points — Batch update
--------------------------------------------------------------------------------

Points — Batch update

_Available as of v1.5.0_
You can batch multiple point update operations. This includes inserting,
updating and deleting points, vectors and payload.
A batch update request consists of a list of operations. These are executed in
order. These operations can be batched:
 Upsert points: `upsert` or `UpsertOperation`
 Delete points: `delete_points` or `DeleteOperation`
 Update vectors: `update_vectors` or `UpdateVectorsOperation`
 Delete vectors: `delete_vectors` or `DeleteVectorsOperation`
 Set payload: `set_payload` or `SetPayloadOperation`
 Overwrite payload: `overwrite_payload` or `OverwritePayload`
 Delete payload: `delete_payload` or `DeletePayloadOperation`
 Clear payload: `clear_payload` or `ClearPayloadOperation`
The following example snippet makes use of all operations.
REST API (Schema):
{{}}
To batch many points with a single operation type, please use batching
functionality in that operation directly.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1357
Retrieved by: colbert 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

With this code snippet, you can perform batch operations on points like upserting, updating vectors, deleting vectors, setting, overwriting, deleting, and clearing payload data associated with points. The operations include inserting, updating, and deleting points along with their vectors and payload. Each operation is executed in order specified in the request payload.

```http_code_1```


```java_code_2```


```python_code_3```


```rust_code_4```


```typescript_code_5```

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
What is hybrid search in Qdrant?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 205
Retrieved by: dense 1, sparse 7, hybrid 1, colbert 2
Section: Reranking Hybrid Search Results with Qdrant Vector Database
--------------------------------------------------------------------------------

Reranking Hybrid Search Results with Qdrant Vector Database

Hybrid search combines dense and sparse retrieval to deliver precise and comprehensive results. By adding reranking with ColBERT, you can further refine search outputs for maximum relevance.
In this guide, we’ll show you how to implement hybrid search with reranking in Qdrant, leveraging dense, sparse, and late interaction embeddings to create an efficient, high-accuracy search system. Let’s get started!

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 209
Retrieved by: dense 2, hybrid 5
Section: Reranking Hybrid Search Results with Qdrant Vector Database — Implementation
--------------------------------------------------------------------------------

Reranking Hybrid Search Results with Qdrant Vector Database — Implementation

Let’s see it in action in this section.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1166
Retrieved by: dense 3, hybrid 7
Section: Swiftide — Hybrid Search Example
--------------------------------------------------------------------------------

Swiftide — Hybrid Search Example

Below is a streamlined workflow for hybrid dense/sparse search using Qdrant.
```rust_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 237
Retrieved by: dense 4, sparse 3, hybrid 3, colbert 4
Section: Build a Hybrid Search Service with FastEmbed and Qdrant — Build the search API
--------------------------------------------------------------------------------

Build a Hybrid Search Service with FastEmbed and Qdrant — Build the search API

Now that all the preparations are complete, let's start building a neural search class.
In order to process incoming requests, the hybrid search class will need 3 things: 1) models to convert the query into a vector, 2) the Qdrant client to perform search queries, 3) fusion function to re-rank dense and sparse search results.
Qdrant supports 2 fusion functions for combining the results: reciprocal rank fusion and distribution based score fusion
1. Create a file named `hybrid_searcher.py` and specify the following.
```python_code_1```
2. Write the search function.
```python_code_2```
3. Add search filters.
With Qdrant it is also feasible to add some conditions to the search.
For example, if you wanted to search for startups in a certain city, the search query could look like this:
```python_code_3```
You have now created a class for neural search queries. Now wrap it up into a service.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 231
Retrieved by: dense 5, sparse 10, hybrid 9, colbert 1
Section: Build a Hybrid Search Service with FastEmbed and Qdrant
--------------------------------------------------------------------------------

Build a Hybrid Search Service with FastEmbed and Qdrant

This tutorial shows you how to build and deploy your own hybrid search service to look through descriptions of companies from startups-list.com and pick the most similar ones to your query.
The website contains the company names, descriptions, locations, and a picture for each entry.
As we have already written on our blog, there is no single definition of hybrid search.
In this tutorial we are covering the case with a combination of dense and sparse embeddings.
The former ones refer to the embeddings generated by such well-known neural networks as BERT, while the latter ones are more related to a traditional full-text search approach.
Our hybrid search service will use Fastembed package to generate embeddings of text descriptions and FastAPI to serve the search API.
Fastembed natively integrates with Qdrant client, so you can easily upload the data into Qdrant and perform search queries.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 232
Retrieved by: dense 6, sparse 9, hybrid 10, colbert 3
Section: Build a Hybrid Search Service with FastEmbed and Qdrant — Workflow
--------------------------------------------------------------------------------

Build a Hybrid Search Service with FastEmbed and Qdrant — Workflow

To create a hybrid search service, you will need to transform your raw data and then create a search function to manipulate it.
First, you will 1) download and prepare a sample dataset using a modified version of the BERT ML model. Then, you will 2) load the data into Qdrant, 3) create a hybrid search API and 4) serve it using FastAPI.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 213
Retrieved by: dense 7
Section: Reranking Hybrid Search Results with Qdrant Vector Database — Implementation — Create Collection
--------------------------------------------------------------------------------

Reranking Hybrid Search Results with Qdrant Vector Database — Implementation — Create Collection

Now, we’re setting up a new collection in Qdrant for our hybrid search with the right configurations to handle all the different vector types we’re working with.
Here’s how you do it:
```python_code_1```
What’s happening here? We’re creating a collection called "hybrid-search", and we’re configuring it to handle:
 Dense embeddings from the model all-MiniLM-L6-v2 using cosine distance for comparisons.
 Late interaction embeddings from colbertv2.0, also using cosine distance, but with a multivector configuration to use the maximum similarity comparator. Note that we set `m=0` in the `colbertv2.0` vector to prevent indexing since it's not needed for reranking.
 Sparse embeddings from BM25 for keyword-based searches. They use `dot_product` for similarity calculation.
This setup ensures that all the different types of vectors are stored and compared correctly for your hybrid search.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 938
Retrieved by: dense 8, sparse 5, hybrid 8, colbert 5
Section: Frequently Asked Questions: General Topics — Search — Does Qdrant support a full-text search or a hybrid search?
--------------------------------------------------------------------------------

Frequently Asked Questions: General Topics — Search — Does Qdrant support a full-text search or a hybrid search?

Qdrant is a vector search engine in the first place, and we only implement full-text support as long as it doesn't compromise the vector search use case.
That includes both the interface and the performance.
What Qdrant can do:
 Search with full-text filters
 Apply full-text filters to the vector search (i.e., perform vector search among the records with specific words or phrases)
 Do prefix search and semantic search-as-you-type
 Sparse vectors, as used in SPLADE or similar models
 Multi-vectors, for example ColBERT and other late-interaction models
 Combination of the multiple searches
What Qdrant doesn't plan to support:
 Non-vector-based retrieval or ranking functions
 Built-in ontologies or knowledge graphs
 Query analyzers and other NLP tools
Of course, you can always combine Qdrant with any specialized tool you need, including full-text search engines.
Read more about our approach to hybrid search.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 215
Retrieved by: dense 9, sparse 4, hybrid 6
Section: Reranking Hybrid Search Results with Qdrant Vector Database — Implementation — Retrieval
--------------------------------------------------------------------------------

Reranking Hybrid Search Results with Qdrant Vector Database — Implementation — Retrieval

For retrieval, it’s time to convert the user’s query into the required embeddings. Here’s how you can do it:
```python_code_1```
The real magic of hybrid search lies in the prefetch parameter. This lets you run multiple sub-queries in one go, combining the power of dense and sparse embeddings. Here’s how to set it up, after which we execute the hybrid search:
```python_code_2```
This code kicks off a hybrid search by running two sub-queries:
 One using dense embeddings from "all-MiniLM-L6-v2" to capture the semantic meaning of the query.
 The other using sparse embeddings from BM25 for strong keyword matching.
Each sub-query is limited to 20 results. These sub-queries are bundled together using the prefetch parameter, allowing them to run in parallel.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1898
Retrieved by: dense 10
Section: Using Cloud Inference with Qdrant for Vector Search
--------------------------------------------------------------------------------

Using Cloud Inference with Qdrant for Vector Search

In this tutorial, we'll walkthrough building a hybrid semantic search engine using Qdrant Cloud's built-in inference capabilities. You'll learn how to:
 Automatically embed your data using cloud Inference without needing to run local models,
 Combine dense semantic embeddings with sparse BM25 keywords, and
 Perform hybrid search using Reciprocal Rank Fusion (RRF) to retrieve the most relevant results.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 419
Retrieved by: sparse 1, hybrid 2, colbert 8
Section: Hybrid and Multi-Stage Queries — Hybrid Search
--------------------------------------------------------------------------------

Hybrid and Multi-Stage Queries — Hybrid Search

One of the most common problems when you have different representations of the same data is to combine the queried points for each representation into a single result.
{{}}
For example, in text search, it is often useful to combine dense and sparse vectors to get the best of both worlds: semantic understanding from dense vectors and precise word matching from sparse vectors.
Qdrant has a few ways of fusing the results from different queries: `rrf` and `dbsf`

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 218
Retrieved by: sparse 2, hybrid 4, colbert 7
Section: Reranking Hybrid Search Results with Qdrant Vector Database — Conclusion
--------------------------------------------------------------------------------

Reranking Hybrid Search Results with Qdrant Vector Database — Conclusion

Reranking is a powerful tool that boosts the relevance of search results, especially when combined with hybrid search methods. While it can add some latency due to its complexity, applying it to a smaller, pre-filtered subset of results ensures both speed and relevance.
Qdrant offers an easy-to-use API to get started with your own search engine, so if you’re ready to dive in, sign up for free at Qdrant Cloud and start building

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 207
Retrieved by: sparse 6
Section: Reranking Hybrid Search Results with Qdrant Vector Database — Overview — Ingestion Stage
--------------------------------------------------------------------------------

Reranking Hybrid Search Results with Qdrant Vector Database — Overview — Ingestion Stage

Here’s how we’re going to set up the advanced hybrid search. The process is similar to what we did earlier but with a few powerful additions:
1. Documents: Just like before, we start with the raw input—our set of documents that need to be indexed for search.
2. Dense Embeddings: We’ll generate dense embeddings for each document, just like in the basic search. These embeddings capture the deeper, semantic meanings behind the text.
3. Sparse Embeddings: This is where it gets interesting. Alongside dense embeddings, we’ll create sparse embeddings using more traditional, keyword-based methods. Specifically, we’ll use BM25, a probabilistic retrieval model. BM25 ranks documents based on how relevant their terms are to a given query, taking into account how often terms appear, document length, and how common the term is across all documents. It’s perfect for keyword-heavy searches.
4. Late Interaction Embeddings: Now, we add the magic of ColBERT. ColBERT uses a two-stage approach. First, it generates contextualized embeddings for both queries and documents using BERT, and then it performs late interaction—matching those embeddings efficiently using a dot product to fine-tune relevance. This step allows for deeper, contextual understanding, making sure you get the most precise results.
5. Vector Database: All of these embeddings—dense, sparse, and late interaction—are stored in a vector database like Qdrant. This allows you to efficiently search, retrieve, and rerank your documents based on multiple layers of relevance.
Query Retrieval and Reranking Process in Search Systems

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 418
Retrieved by: sparse 8
Section: Hybrid and Multi-Stage Queries
--------------------------------------------------------------------------------

Hybrid and Multi-Stage Queries

_Available as of v1.10.0_
With the introduction of multiple named vectors per point, there are use-cases when the best search is obtained by combining multiple queries,
or by performing the search in more than one stage.
Qdrant has a flexible and universal interface to make this possible, called `Query API` (API reference).
The main component for making the combinations of queries possible is the `prefetch` parameter, which enables making sub-requests.
Specifically, whenever a query has at least one prefetch, Qdrant will:
1. Perform the prefetch query (or queries),
2. Apply the main query over the results of its prefetch(es).
Additionally, prefetches can have prefetches themselves, so you can have nested prefetches.
Using offset parameter only affects the main query. This means that the prefetches must have a limit of at least limit + offset of the main query, otherwise you can get an empty result.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 234
Retrieved by: colbert 6
Section: Build a Hybrid Search Service with FastEmbed and Qdrant — Prepare sample dataset
--------------------------------------------------------------------------------

Build a Hybrid Search Service with FastEmbed and Qdrant — Prepare sample dataset

To conduct a hybrid search on startup descriptions, you must first encode the description data into vectors.
Fastembed integration into qdrant client combines encoding and uploading into a single step.
It also takes care of batching and parallelization, so you don't have to worry about it.
Let's start by downloading the data and installing the necessary packages.
1. First you need to download the dataset.
```bash_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1362
Retrieved by: colbert 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet creates a collection configured for hybrid search using Qdrant's Cloud Inference. It defines a sparse BM25 vector and a dense vector for MiniLM. This setup allows Qdrant to perform hybrid search using the dense and sparse vectors. 

```csharp_code_1```


```go_code_2```


```java_code_3```


```python_code_4```


```rust_code_5```


```typescript_code_6```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 822
Retrieved by: colbert 10
Section: Chat With Product PDF Manuals Using Hybrid Search — Implementation — Store data into Qdrant
--------------------------------------------------------------------------------

Chat With Product PDF Manuals Using Hybrid Search — Implementation — Store data into Qdrant

The code below does the following:
 create a vector store with Qdrant client;
 get an embedding for each chunk using Jina Embeddings API;
 combines `sparse` and `dense` vectors for hybrid search;
 stores all data into Qdrant;
Hybrid search with Qdrant must be enabled from the beginning we can simply set `enable_hybrid=True`.
```text_code_1```

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
Difference between dense and sparse vectors?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 489
Retrieved by: dense 1, sparse 1, hybrid 1, colbert 1
Section: Points — Upload points — Sparse vectors
--------------------------------------------------------------------------------

Points — Upload points — Sparse vectors

_Available as of v1.7.0_
Points can contain dense and sparse vectors.
A sparse vector is an array in which most of the elements have a value of zero.
It is possible to take advantage of this property to have an optimized representation, for this reason they have a different shape than dense vectors.
They are represented as a list of `(index, value)` pairs, where `index` is an integer and `value` is a floating point number. The `index` is the position of the non-zero value in the vector. The `values` is the value of the non-zero element.
For example, the following vector:
```text_code_1```
can be represented as a sparse vector:
```text_code_2```
Qdrant uses the following JSON representation throughout its APIs.
```json_code_3```
The `indices` and `values` arrays must have the same length.
And the `indices` must be unique.
If the `indices` are not sorted, Qdrant will sort them internally so you may not rely on the order of the elements.
Sparse vectors must be named and can be uploaded in the same way as dense vectors.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 545
Retrieved by: dense 2, sparse 3, hybrid 2, colbert 2
Section: Vectors — Vector Types — Sparse Vectors
--------------------------------------------------------------------------------

Vectors — Vector Types — Sparse Vectors

Sparse vectors are a special type of vectors.
Mathematically, they are the same as dense vectors, but they contain many zeros so they are stored in a special format.
Sparse vectors in Qdrant don't have a fixed length, as it is dynamically allocated during vector insertion.
The amount of non-zero values in sparse vectors is currently limited to u32 datatype range (4294967295).
In order to define a sparse vector, you need to provide a list of non-zero elements and their indexes.
```json_code_1```
Sparse vectors in Qdrant are kept in special storage and indexed in a separate index, so their configuration is different from dense vectors.
To create a collection with sparse vectors:
{{}}
Insert a point with a sparse vector into the created collection:
{{}}
Now you can run a search with sparse vectors:
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 359
Retrieved by: dense 3, sparse 4, hybrid 3, colbert 3
Section: Collections — Create a collection — Collection with sparse vectors
--------------------------------------------------------------------------------

Collections — Create a collection — Collection with sparse vectors

Available as of v1.7.0
Qdrant supports sparse vectors as a first-class citizen.
Sparse vectors are useful for text search, where each word is represented as a separate dimension.
Collections can contain sparse vectors as additional named vectors along side regular dense vectors in a single point.
Unlike dense vectors, sparse vectors must be named.
And additionally, sparse vectors and dense vectors must have different names within a collection.
{{}}
Outside of a unique name, there are no required configuration parameters for sparse vectors.
The distance function for sparse vectors is always `Dot` and does not need to be specified.
However, there are optional parameters to tune the underlying sparse vector index.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1376
Retrieved by: dense 4, sparse 6, hybrid 5, colbert 7
Section: Introduction
--------------------------------------------------------------------------------

Introduction

When working with vectors in a collection, you can specify the datatype as Uint8 for both dense and sparse vectors. Uint8 represents integer numbers from 0 to 255, which is different from floating-point numbers. 

For dense vectors, make sure the values fall within the range of 0 to 255. If the embeddings generated by your model are not in this range, you will need to quantize the values to convert them. 

Some embedding providers may offer pre-quantized embeddings like Cohere int8 & binary embeddings. If not, you will have to perform quantization yourself.

It's important to note that while dense vectors must be in the 0 to 255 range, sparse vectors allow for in-flight quantization. This distinction should be considered when handling Uint8 vectors.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 445
Retrieved by: dense 5, hybrid 7, colbert 5
Section: Indexing — Sparse Vector Index
--------------------------------------------------------------------------------

Indexing — Sparse Vector Index

Available as of v1.7.0
Sparse vectors in Qdrant are indexed with a special data structure, which is optimized for vectors that have a high proportion of zeroes. In some ways, this indexing method is similar to the inverted index, which is used in text search engines.
 A sparse vector index in Qdrant is exact, meaning it does not use any approximation algorithms.
 All sparse vectors added to the collection are immediately indexed in the mutable version of a sparse index.
With Qdrant, you can benefit from a more compact and efficient immutable sparse index, which is constructed during the same optimization process as the dense vector index.
This approach is particularly useful for collections storing both dense and sparse vectors.
To configure a sparse vector index, create a collection with the following parameters:
{{}}`
The following parameters may affect performance:
 `on_disk: true` The index is stored on disk, which lets you save memory. This may slow down search performance.
 `on_disk: false` The index is still persisted on disk, but it is also loaded into memory for faster search.
Unlike a dense vector index, a sparse vector index does not require a predefined vector size. It automatically adjusts to the size of the vectors added to the collection.
Note: A sparse vector index only supports dot-product similarity searches. It does not support other distance metrics.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1383
Retrieved by: dense 6, sparse 5, hybrid 6, colbert 4
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates creating a collection in Qdrant with support for sparse vectors. Sparse vectors are useful for text search, representing each word as a separate dimension. This feature allows collections to contain both sparse vectors and regular dense vectors in one point. Sparse vectors need to be named uniquely within a collection, separate from the names of dense vectors.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1374
Retrieved by: dense 7, sparse 9, hybrid 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code sets up a collection with vectors containing 128 dimensions and a cosine distance metric. It configures the datatype for dense vectors to be Float16, which consumes less memory than Float32 without significant impact on search quality. Additionally, it specifies Float16 as the datatype for sparse text vectors in the collection.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1463
Retrieved by: dense 8, sparse 7, hybrid 8, colbert 8
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet showcases a system for inserting points with sparse vectors into collections. Each point consists of an ID and a vector, where the vector data includes the indices and corresponding values. The `indices` and `values` arrays are required to have the same length, with unique `indices`. If the `indices` are not sorted, the system will internally sort them. Sparse vectors can be uploaded in a similar manner as dense vectors.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1092
Retrieved by: dense 9, sparse 8, hybrid 10
Section: LangChain — Similarity search — Hybrid Vector Search
--------------------------------------------------------------------------------

LangChain — Similarity search — Hybrid Vector Search

To perform a hybrid search using dense and sparse vectors with score fusion,
 The `retrieval_mode` parameter should be set to `RetrievalMode.HYBRID`.
 A dense embeddings value should be provided for the `embedding` parameter.
 An implementation of the SparseEmbeddings interface using any sparse embeddings provider has to be provided as value to the `sparse_embedding` parameter.
```python_code_1```
Note that if you've added documents with HYBRID mode, you can switch to any retrieval mode when searching. Since both the dense and sparse vectors are available in the collection.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 544
Retrieved by: dense 10, colbert 6
Section: Vectors — Vector Types — Dense Vectors
--------------------------------------------------------------------------------

Vectors — Vector Types — Dense Vectors

This is the most common type of vector. It is a simple list of numbers, it has a fixed length and each element of the list is a floating-point number.
It looks like this:
```json_code_1```
The majority of neural networks create dense vectors, so you can use them with Qdrant without any additional processing.
Although compatible with most embedding models out there, Qdrant has been tested with the following verified embedding providers.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1852
Retrieved by: sparse 2, hybrid 4
Section: Understanding Reranking — Background
--------------------------------------------------------------------------------

Understanding Reranking — Background

In search systems, two metrics—precision and recall—are the backbone of success. But what do they mean? Precision tells us how many of the retrieved results are actually relevant, while recall measures how well we’ve captured all the relevant results out there. Simply put:
Sparse vector searches usually give you high precision because they’re great at finding exact matches. But, here's the catch—your recall can suffer when relevant documents don’t contain those exact keywords. On the flip side, dense vector searches are fantastic for recall since they grasp the broader, semantic meaning of your query. However, this can lead to lower precision, where you might see results that are only loosely related.
This is exactly where reranking comes to the rescue. It takes a wide net of documents (giving you high recall) and then refines them by reordering the top candidates based on their relevance scores—boosting precision without losing that broad understanding. Typically, we retain only the top K candidates after reordering to focus on the most relevant results.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1858
Retrieved by: sparse 10
Section: Implementing Vector Search with Reranking — Overview — Retrieval Stage
--------------------------------------------------------------------------------

Implementing Vector Search with Reranking — Overview — Retrieval Stage

User's Query: Now we enter the retrieval phase. The user submits a query, and it’s time to match that query against the stored documents.
 Embeddings: Just like with the documents, the user’s query is converted into a sparse or dense embedding. This enables the system to compare the query's meaning with the meanings of the stored documents.
 Vector Search: The system searches for the most relevant documents by comparing the query’s embedding to those in the vector database, and it pulls up the closest matches.
 Rerank: Once the initial results are in, the reranking process kicks in to ensure you get the best results on top. We’ll be using Cohere’s rerank-english-v3.0 model, which excels at reordering English language documents to prioritize relevance. It can handle up to 4096 tokens, giving it plenty of context to work with. And if you’re dealing with multi-lingual data, don’t worry—Cohere’s got reranking models for other languages too.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 996
Retrieved by: colbert 9
Section: How to Generate Sparse Vectors with SPLADE — Design choices
--------------------------------------------------------------------------------

How to Generate Sparse Vectors with SPLADE — Design choices

The weights are not normalized. This means that the sum of the weights is not 1 or 100. This is a common practice in sparse embeddings, as it allows the model to capture the importance of each token in the document.
 Tokens are included in the sparse vector only if they are present in the model's vocabulary. This means that the model will not generate a weight for tokens that it has not seen during training.
 Tokens do not map to words directly -- allowing you to gracefully handle typo errors and out-of-vocabulary tokens.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 549
Retrieved by: colbert 10
Section: Vectors — Datatypes
--------------------------------------------------------------------------------

Vectors — Datatypes

Newest versions of embeddings models generate vectors with very large dimentionalities.
With OpenAI's `text-embedding-3-large` embedding model, the dimensionality can go up to 3072.
The amount of memory required to store such vectors grows linearly with the dimensionality,
so it is important to choose the right datatype for the vectors.
The choice between datatypes is a trade-off between memory consumption and precision of vectors.
Qdrant supports a number of datatypes for both dense and sparse vectors:
Float32
This is the default datatype for vectors in Qdrant. It is a 32-bit (4 bytes) floating-point number.
The standard OpenAI embedding of 1536 dimensionality will require 6KB of memory to store in Float32.
You don't need to specify the datatype for vectors in Qdrant, as it is set to Float32 by default.
Float16
This is a 16-bit (2 bytes) floating-point number. It is also known as half-precision float.
Intuitively, it looks like this:
```text_code_1```
The main advantage of Float16 is that it requires half the memory of Float32, while having virtually no impact on the quality of vector search.
To use Float16, you need to specify the datatype for vectors in the collection configuration:
{{}}
Uint8
Another step towards memory optimization is to use the Uint8 datatype for vectors.
Unlike Float16, Uint8 is not a floating-point number, but an integer number in the range from 0 to 255.
Not all embeddings models generate vectors in the range from 0 to 255, so you need to be careful when using Uint8 datatype.
In order to convert a number from float range to Uint8 range, you need to apply a process called quantization.
Some embedding providers may provide embeddings in a pre-quantized format.
One of the most notable examples is the Cohere int8 & binary embeddings.
For other embeddings, you will need to apply quantization yourself.
There is a difference in how Uint8 vectors are handled for dense and sparse vectors.
Dense vectors are required to be in the range from 0 to 255, while sparse vectors can be quantized in-flight.
{{}}

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How does RRF fusion work?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 420
Retrieved by: dense 1, sparse 1, hybrid 1, colbert 1
Section: Hybrid and Multi-Stage Queries — Hybrid Search — Reciprocal Rank Fusion (RRF)
--------------------------------------------------------------------------------

Hybrid and Multi-Stage Queries — Hybrid Search — Reciprocal Rank Fusion (RRF)

RRF considers the positions of results within each query, and boosts the ones that appear closer to the top in multiple sets of results.
The formula is simple, but needs access to the rank of each result in each query.
$$ score(d\in D) = \sum_{r_d\in R(d)} \frac{1}{k + r_d} $$
Where $D$ the set of points across all results, $R(d)$ is the set of rankings for a particular document, and $k$ is a constant (set to 2 by default).
Here is an example of RRF for a query containing two prefetches against different named vectors configured to hold sparse and dense vectors, respectively.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 421
Retrieved by: dense 2, sparse 3, hybrid 3, colbert 3
Section: Hybrid and Multi-Stage Queries — Hybrid Search — Reciprocal Rank Fusion (RRF) — Parametrized RRF
--------------------------------------------------------------------------------

Hybrid and Multi-Stage Queries — Hybrid Search — Reciprocal Rank Fusion (RRF) — Parametrized RRF

_Available as of v1.16.0_
To change the value of constant $k$ in the formula, use the dedicated `rrf` query variant.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1488
Retrieved by: dense 3, sparse 2, hybrid 2, colbert 2
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates a hybrid search functionality where you can query points from a collection using both sparse and dense vectors. The code showcases how to combine the results of multiple queries with different vector representations using Reciprocal Rank Fusion (RRF). RRF boosts results that are closer to the top in multiple queries. This hybrid search approach can be useful for obtaining semantic and specific word matching results simultaneously.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1489
Retrieved by: dense 4, sparse 4, hybrid 4, colbert 4
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates a hybrid search functionality where you can query points from a collection using both sparse and dense vectors. The code showcases how to combine the results of multiple queries with different vector representations using Reciprocal Rank Fusion (RRF), parametrized by constant k. RRF boosts results that are closer to the top in multiple queries. This hybrid search approach can be useful for obtaining semantic and specific word matching results simultaneously.


```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 422
Retrieved by: dense 5, sparse 6, hybrid 5, colbert 7
Section: Hybrid and Multi-Stage Queries — Hybrid Search — Distribution-Based Score Fusion (DBSF)
--------------------------------------------------------------------------------

Hybrid and Multi-Stage Queries — Hybrid Search — Distribution-Based Score Fusion (DBSF)

_Available as of v1.11.0_
DBSF
normalizes the scores of the points in each query, using the mean +/- the 3rd standard deviation as limits, and then sums the scores of the same point across different queries.
dbsf is stateless and calculates the normalization limits only based on the results of each query, not on all the scores that it has seen.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 419
Retrieved by: dense 6, sparse 7, hybrid 6, colbert 8
Section: Hybrid and Multi-Stage Queries — Hybrid Search
--------------------------------------------------------------------------------

Hybrid and Multi-Stage Queries — Hybrid Search

One of the most common problems when you have different representations of the same data is to combine the queried points for each representation into a single result.
{{}}
For example, in text search, it is often useful to combine dense and sparse vectors to get the best of both worlds: semantic understanding from dense vectors and precise word matching from sparse vectors.
Qdrant has a few ways of fusing the results from different queries: `rrf` and `dbsf`

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1886
Retrieved by: dense 7, hybrid 9, colbert 9
Section: Qdrant on Databricks — Vectorizing the data — Applying the UDF on our dataframe
--------------------------------------------------------------------------------

Qdrant on Databricks — Vectorizing the data — Applying the UDF on our dataframe

Next, let's apply our `vectorize` UDF on our Spark dataframe to generate embeddings.
```python_code_1```
The `mapPartitions()` method returns a Resilient Distributed Dataset (RDD) which should then be converted back to a Spark dataframe.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 222
Retrieved by: dense 8
Section: How to Effectively Use Multivector Representations in Qdrant for Reranking — What is Rescoring, and Why is it Used?
--------------------------------------------------------------------------------

How to Effectively Use Multivector Representations in Qdrant for Reranking — What is Rescoring, and Why is it Used?

Rescoring is two-fold:
 Retrieve relevant documents using a fast model.
 Rerank them using a more accurate but slower model such as ColBERT.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1898
Retrieved by: dense 9, sparse 5, hybrid 7, colbert 6
Section: Using Cloud Inference with Qdrant for Vector Search
--------------------------------------------------------------------------------

Using Cloud Inference with Qdrant for Vector Search

In this tutorial, we'll walkthrough building a hybrid semantic search engine using Qdrant Cloud's built-in inference capabilities. You'll learn how to:
 Automatically embed your data using cloud Inference without needing to run local models,
 Combine dense semantic embeddings with sparse BM25 keywords, and
 Perform hybrid search using Reciprocal Rank Fusion (RRF) to retrieve the most relevant results.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1146
Retrieved by: dense 10
Section: Rig-rs — Further reading
--------------------------------------------------------------------------------

Rig-rs — Further reading

Rig-rs Documentation
 Source Code

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 237
Retrieved by: sparse 8, hybrid 8
Section: Build a Hybrid Search Service with FastEmbed and Qdrant — Build the search API
--------------------------------------------------------------------------------

Build a Hybrid Search Service with FastEmbed and Qdrant — Build the search API

Now that all the preparations are complete, let's start building a neural search class.
In order to process incoming requests, the hybrid search class will need 3 things: 1) models to convert the query into a vector, 2) the Qdrant client to perform search queries, 3) fusion function to re-rank dense and sparse search results.
Qdrant supports 2 fusion functions for combining the results: reciprocal rank fusion and distribution based score fusion
1. Create a file named `hybrid_searcher.py` and specify the following.
```python_code_1```
2. Write the search function.
```python_code_2```
3. Add search filters.
With Qdrant it is also feasible to add some conditions to the search.
For example, if you wanted to search for startups in a certain city, the search query could look like this:
```python_code_3```
You have now created a class for neural search queries. Now wrap it up into a service.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1903
Retrieved by: sparse 9, hybrid 10
Section: Using Cloud Inference with Qdrant for Vector Search — Run Vector Search
--------------------------------------------------------------------------------

Using Cloud Inference with Qdrant for Vector Search — Run Vector Search

Here, you will ask a question that will allow you to retrieve semantically relevant results. The final results are obtained by reranking using Reciprocal Rank Fusion.
{{}}
The semantic search engine will retrieve the most similar result in order of relevance.
```markdown_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1092
Retrieved by: sparse 10
Section: LangChain — Similarity search — Hybrid Vector Search
--------------------------------------------------------------------------------

LangChain — Similarity search — Hybrid Vector Search

To perform a hybrid search using dense and sparse vectors with score fusion,
 The `retrieval_mode` parameter should be set to `RetrievalMode.HYBRID`.
 A dense embeddings value should be provided for the `embedding` parameter.
 An implementation of the SparseEmbeddings interface using any sparse embeddings provider has to be provided as value to the `sparse_embedding` parameter.
```python_code_1```
Note that if you've added documents with HYBRID mode, you can switch to any retrieval mode when searching. Since both the dense and sparse vectors are available in the collection.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1348
Retrieved by: colbert 5
Section: Combining Semantic and Lexical Search with Hybrid Search
--------------------------------------------------------------------------------

Combining Semantic and Lexical Search with Hybrid Search

Hybrid search enables you to combine semantic and lexical search in a single query, returning results that match the semantic meaning, the exact keywords, or both. This is useful when you don't know whether the user is looking for a specific keyword or a semantically similar document. For example, when searching for books, a user may enter "time travel" to find books related to the concept of time travel, but they may also enter a book's ISBN to find a specific book. Hybrid queries enable you to return results for both cases in a single query.
Hybrid queries make use of Qdrant's ability to store multiple named vectors in a single point. For example, you can store a dense vector for semantic search and a sparse vector for lexical search in the same point. To do so, first create a collection with both a dense vector and a sparse vector:
{{}}
After ingesting data with both vectors, you can use the prefetch feature to run both semantic and lexical queries in a single request. The results of both queries are then combined using a fusion method like Reciprocal Rank Fusion (RRF).
{{}}
This query searches for an ISBN, for which only the lexical search returns a result. The `score_threshold` for the semantic query prevents low-scoring results to be returned (0.5 is just an example threshold; you need to tune what a good threshold is for your data and model). So in this case, only the lexical result is returned to the user. If a user had searched for "time travel", only the semantic search would return results, and those would be returned to the user. If a user would search for a term that matched both the semantic and lexical vectors, the results from both searches would be combined to provide a more comprehensive set of results.
You are not limited to prefetching just two queries. Examples include, but are not limited to:
 Fuse multiple lexical queries across the `title`, `author`, and `isbn` fields alongside a semantic query to achieve a comprehensive search across all data.
 Prefetch using sparse or dense vectors and/or filters, and rescore with dense vectors.
 Prefetch with dense and sparse vectors, and rerank using late interaction embeddings.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1365
Retrieved by: colbert 10
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet demonstrates how to use the Universal Query API to prefetch results with dense and sparse vector search, and then rerank them with Reciprocal Rank Fusion. It uses Cloud Inference to create embeddings by passing document text along with the model names, instead of vectors. 

```csharp_code_1```


```go_code_2```


```java_code_3```


```python_code_4```


```rust_code_5```


```typescript_code_6```

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How does Qdrant optimize storage after updates?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 461
Retrieved by: dense 1, sparse 3, hybrid 1, colbert 1
Section: Optimizer
--------------------------------------------------------------------------------

Optimizer

It is much more efficient to apply changes in batches than perform each change individually, as many other databases do. Qdrant here is no exception. Since Qdrant operates with data structures that are not always easy to change, it is sometimes necessary to rebuild those structures completely.
Storage optimization in Qdrant occurs at the segment level (see storage).
In this case, the segment to be optimized remains readable for the time of the rebuild.
The availability is achieved by wrapping the segment into a proxy that transparently handles data changes.
Changed data is placed in the copy-on-write segment, which has priority for retrieval and subsequent updates.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1282
Retrieved by: dense 2, hybrid 4
Section: Optimizing Qdrant Performance: Three Scenarios — 1. High-Speed Search with Low Memory Usage — Disable Rescoring for Faster Search (optional)
--------------------------------------------------------------------------------

Optimizing Qdrant Performance: Three Scenarios — 1. High-Speed Search with Low Memory Usage — Disable Rescoring for Faster Search (optional)

This is completely optional. Disabling rescoring with search `params` can further reduce the number of disk reads. Note that this might slightly decrease precision.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1291
Retrieved by: dense 3, sparse 6, hybrid 3, colbert 6
Section: Optimizing Qdrant Performance: Three Scenarios — Summary
--------------------------------------------------------------------------------

Optimizing Qdrant Performance: Three Scenarios — Summary

By adjusting configurations like vector storage, quantization, and search parameters, you can optimize Qdrant for different use cases:
 Low Memory + High Speed: Use vector quantization.
 High Precision + Low Memory: Store vectors and HNSW index on disk.
 High Precision + High Speed: Keep data in RAM, use quantization with re-scoring.
 Latency vs. Throughput: Adjust segment numbers based on the priority.
Choose the strategy that best fits your use case to get the most out of Qdrant’s performance capabilities.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1210
Retrieved by: dense 4, hybrid 10
Section: Capacity Planning — Scaling disk space in Qdrant Cloud
--------------------------------------------------------------------------------

Capacity Planning — Scaling disk space in Qdrant Cloud

Clusters supporting vector search require substantial disk space compared to other search systems. If you're running low on disk space, you can use the UI at cloud.qdrant.io to Scale Up your cluster.
Note: If you increase disk space via the Qdrant UI, you cannot reduce it later.
When running low on disk space, consider the following benefits of scaling up:
 Larger Datasets: Supports larger datasets, which can improve the relevance and quality of search results.
 Improved Indexing: Enables the use of advanced indexing strategies like HNSW.
 Caching: Enhances speed by having more RAM, allowing more frequently accessed data to be cached.
 Backups and Redundancy: Facilitates more frequent backups, which is a key advantage for data safety.
Always remember to add 50% of the vector size. This would account for things like indexes and auxiliary data used during operations such as vector insertion, deletion, and search. Thus, the estimated memory size including metadata is:
```text_code_1```
Disclaimer
The above calculations are estimates at best. If you're looking for more accurate numbers, you should always test your data set in practice.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1280
Retrieved by: dense 5, hybrid 7
Section: Optimizing Qdrant Performance: Three Scenarios
--------------------------------------------------------------------------------

Optimizing Qdrant Performance: Three Scenarios

Different use cases require different balances between memory usage, search speed, and precision. Qdrant is designed to be flexible and customizable so you can tune it to your specific needs.
This guide will walk you three main optimization strategies:
 High Speed Search & Low Memory Usage
 High Precision & Low Memory Usage
 High Precision & High Speed Search

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 297
Retrieved by: dense 6
Section: Updating Qdrant Cloud Clusters
--------------------------------------------------------------------------------

Updating Qdrant Cloud Clusters

As soon as a new Qdrant version is available. Qdrant Cloud will show you an update notification in the Cluster list and on the Cluster details page.
To update to a new version, go to the Cluster Details page, choose the new version from the version dropdown and click Update.
If you are several versions behind, multiple updates might be required to reach the latest version. In this case, Qdrant Cloud will automatically perform the required intermediate updates to ensure a supported update path. You should still ensure that your client applications and used SKDs are compatible with the target version.
If you have a multi-node cluster and if your collections have a replication factor of at least 2, the update process will be zero-downtime and done in a rolling fashion. You will be able to use your database cluster normally.
If you have a single-node cluster or a collection with a replication factor of 1, the update process will require a short downtime period to restart your cluster with the new version.
See also Restart Mode for more details.
We advise taking a backup before updating to allow for rollbacks.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1589
Retrieved by: dense 7
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Update the collection with patch requests to put vector data on disk. This functionality allows you to specify vector parameters, such as setting vectors to be stored on disk, for a specific collection. In cases where the collection does not have named vectors, an empty name (`""`) should be used to perform this update. This feature provided by Qdrant version 1.4 enables modifications to collection parameters, including HNSW index, quantization, and disk configurations dynamically, without the need to recreate the collection. Additionally, segments containing index and quantized data will be automatically rebuilt in the background to align with the new parameters.

```bash_code_1```


```http_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 541
Retrieved by: dense 8, sparse 5, hybrid 6, colbert 3
Section: Storage — Versioning
--------------------------------------------------------------------------------

Storage — Versioning

To ensure data integrity, Qdrant performs all data changes in 2 stages.
In the first step, the data is written to the Write-ahead-log(WAL), which orders all operations and assigns them a sequential number.
Once a change has been added to the WAL, it will not be lost even if a power loss occurs.
Then the changes go into the segments.
Each segment stores the last version of the change applied to it as well as the version of each individual point.
If the new change has a sequential number less than the current version of the point, the updater will ignore the change.
This mechanism allows Qdrant to safely and efficiently restore the storage from the WAL in case of an abnormal shutdown.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 653
Retrieved by: dense 9
Section: Upload and Search Large collections cost-efficiently — Conclusion
--------------------------------------------------------------------------------

Upload and Search Large collections cost-efficiently — Conclusion

In this tutorial we demonstrated how to upload, index and search a large dataset in Qdrant cost-efficiently.
Binary quantization can be applied even on 512d vectors, if combined with query-time oversampling.
Qdrant allows to precisely control where each part of storage is located, which allows to achieve a good balance between search speed and memory usage.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 462
Retrieved by: dense 10, sparse 8, hybrid 8
Section: Optimizer — Vacuum Optimizer
--------------------------------------------------------------------------------

Optimizer — Vacuum Optimizer

The simplest example of a case where you need to rebuild a segment repository is to remove points.
Like many other databases, Qdrant does not delete entries immediately after a query.
Instead, it marks records as deleted and ignores them for future queries.
This strategy allows us to minimize disk access one of the slowest operations.
However, a side effect of this strategy is that, over time, deleted records accumulate, occupy memory and slow down the system.
To avoid these adverse effects, Vacuum Optimizer is used.
It is used if the segment has accumulated too many deleted records.
The criteria for starting the optimizer are defined in the configuration file.
Here is an example of parameter values:
```yaml_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 464
Retrieved by: sparse 1, hybrid 2, colbert 2
Section: Optimizer — Indexing Optimizer
--------------------------------------------------------------------------------

Optimizer — Indexing Optimizer

Qdrant allows you to choose the type of indexes and data storage methods used depending on the number of records.
So, for example, if the number of points is less than 10000, using any index would be less efficient than a brute force scan.
The Indexing Optimizer is used to implement the enabling of indexes and memmap storage when the minimal amount of records is reached.
The criteria for starting the optimizer are defined in the configuration file.
Here is an example of parameter values:
```yaml_code_1```
In addition to the configuration file, you can also set optimizer parameters separately for each collection.
Dynamic parameter updates may be useful, for example, for more efficient initial loading of points. You can disable indexing during the upload process with these settings and enable it immediately after it is finished. As a result, you will not waste extra computation resources on rebuilding the index.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 463
Retrieved by: sparse 2, hybrid 5
Section: Optimizer — Merge Optimizer
--------------------------------------------------------------------------------

Optimizer — Merge Optimizer

The service may require the creation of temporary segments.
Such segments, for example, are created as copy-on-write segments during optimization itself.
It is also essential to have at least one small segment that Qdrant will use to store frequently updated data.
On the other hand, too many small segments lead to suboptimal search performance.
The merge optimizer constantly tries to reduce the number of segments if there
currently are too many. The desired number of segments is specified
with `default_segment_number` and defaults to the number of CPUs. The optimizer
may takes at least the three smallest segments and merges them into one.
Segments will not be merged if they'll exceed the maximum configured segment
size with `max_segment_size_kb`. It prevents creating segments that are too
large to efficiently index. Increasing this number may help to reduce the number
of segments if you have a lot of data, and can potentially improve search performance.
The criteria for starting the optimizer are defined in the configuration file.
Here is an example of parameter values:
```yaml_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1396
Retrieved by: sparse 4, hybrid 9, colbert 4
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Creates a collection with vectors stored in memmap storage and specifies an optimizer configuration with a `indexing_threshold` set to 20000. This configuration is particularly useful for Qdrant instances with fast disks and large collections. The `indexing_threshold` option determines the threshold after which a segment will be converted to memmap storage. It can be set globally in the configuration file or for each collection individually during creation or update.


```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1390
Retrieved by: sparse 7
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Configure Qdrant to optimize performance by bypassing the creation of a global vector index for the entire collection. Instead, focus on indexing vectors for individual groups separately to enhance the speed of the process. Update the HNSW configuration by setting `payload_m` to a specific value, like 16, and ensuring `m` in the configuration is set to 0 to disable the global index construction.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1285
Retrieved by: sparse 9, colbert 7
Section: Optimizing Qdrant Performance: Three Scenarios — 2. High Precision with Low Memory Usage — Inline Storage in HNSW Index
--------------------------------------------------------------------------------

Optimizing Qdrant Performance: Three Scenarios — 2. High Precision with Low Memory Usage — Inline Storage in HNSW Index

Available as of v1.16.0
When storing vectors and the HNSW index on disk, you can improve search performance by enabling the `inline_storage` option in the `hnsw_config`.
With inline storage, Qdrant stores copies of vectors directly within the HNSW index file.
It makes searches faster by reducing the number of IO operations, at the cost of 3-4x increased storage usage.
It requires quantization to be enabled.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 616
Retrieved by: sparse 10, colbert 9
Section: Bulk Upload Vectors to a Qdrant Collection — Choose an Indexing Strategy
--------------------------------------------------------------------------------

Bulk Upload Vectors to a Qdrant Collection — Choose an Indexing Strategy

Qdrant incrementally builds an HNSW index for dense vectors as new data arrives. This ensures fast search, but indexing is memory- and CPU-intensive. During bulk ingestion, frequent index updates can reduce throughput and increase resource usage.
To control this behavior and optimize for your system’s limits, adjust the following parameters:
Fastest upload, tolerate high RAM usage — Disable indexing completely — `indexing_threshold: 0`
Low memory usage during upload — Defer HNSW graph construction (recommended) — `m: 0`
Faster index availability after upload — Keep indexing enabled (default behavior) — `m: 16`, `indexing_threshold: 20000` (default)
Indexing must be re-enabled after upload to activate fast HNSW search if it was disabled during ingestion.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 539
Retrieved by: colbert 5
Section: Storage — Vector storage — Configuring Memmap storage
--------------------------------------------------------------------------------

Storage — Vector storage — Configuring Memmap storage

There are two ways to configure the usage of memmap(also known as on-disk) storage:
 Set up `on_disk` option for the vectors in the collection create API:
Available as of v1.2.0
{{}}
This will create a collection with all vectors immediately stored in memmap storage.
This is the recommended way, in case your Qdrant instance operates with fast disks and you are working with large collections.
 Set up `memmap_threshold` option. This option will set the threshold after which the segment will be converted to memmap storage.
There are two ways to do this:
1. You can set the threshold globally in the configuration file. The parameter is called `memmap_threshold` (previously `memmap_threshold_kb`).
2. You can set the threshold for each collection separately during creation or update.
{{}}
The rule of thumb to set the memmap threshold parameter is simple:
 if you have a balanced use scenario set memmap threshold the same as `indexing_threshold` (default is 20000). In this case the optimizer will not make any extra runs and will optimize all thresholds at once.
 if you have a high write load and low RAM set memmap threshold lower than `indexing_threshold` to e.g. 10000. In this case the optimizer will convert the segments to memmap storage first and will only apply indexing after that.
In addition, you can use memmap storage not only for vectors, but also for HNSW index.
To enable this, you need to set the `hnsw_config.on_disk` parameter to `true` during collection creation or updating.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1832
Retrieved by: colbert 8
Section: Managing a Qdrant Cluster — Scaling a Cluster
--------------------------------------------------------------------------------

Managing a Qdrant Cluster — Scaling a Cluster

To scale a cluster, update the CPU, memory and storage resources in the QdrantCluster spec. The Qdrant operator will automatically adjust the cluster configuration. This operation is highly available on a multi-node cluster with replicated collections.
Vertical scaling is only possible if your CSI driver and StorageClass allows volume expansion. Disk storage can not be downscaled.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 923
Retrieved by: colbert 10
Section: Frequently Asked Questions: Database Optimization — How do you choose the machine configuration?
--------------------------------------------------------------------------------

Frequently Asked Questions: Database Optimization — How do you choose the machine configuration?

There are two main scenarios of Qdrant usage in terms of resource consumption:
 Performance-optimized -- when you need to serve vector search as fast (many) as possible. In this case, you need to have as much vector data in RAM as possible. Use our calculator to estimate the required RAM.
 Storage-optimized -- when you need to store many vectors and minimize costs by compromising some search speed. In this case, pay attention to the disk speed instead. More about it in the article about Memory Consumption.

[RELEVANT? 2 / 1 / 0]




================================================================================
QUERY:
How are updates written internally (WAL or segments)?
================================================================================

--------------------------------------------------------------------------------
Chunk ID: 541
Retrieved by: dense 1, sparse 1, hybrid 1, colbert 1
Section: Storage — Versioning
--------------------------------------------------------------------------------

Storage — Versioning

To ensure data integrity, Qdrant performs all data changes in 2 stages.
In the first step, the data is written to the Write-ahead-log(WAL), which orders all operations and assigns them a sequential number.
Once a change has been added to the WAL, it will not be lost even if a power loss occurs.
Then the changes go into the segments.
Each segment stores the last version of the change applied to it as well as the version of each individual point.
If the new change has a sequential number less than the current version of the point, the updater will ignore the change.
This mechanism allows Qdrant to safely and efficiently restore the storage from the WAL in case of an abnormal shutdown.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 496
Retrieved by: dense 2, hybrid 2, colbert 4
Section: Points — Conditional updates
--------------------------------------------------------------------------------

Points — Conditional updates

_Available as of v1.16.0_
All update operations (including point insertion, vector updates, payload updates, and deletions) support configurable pre-conditions based on filters.
{{}}
While conditional payload modification and deletion covers the use-case of mass data modification, conditional point insertion and vector updates are particularly useful for implementing optimistic concurrency control in distributed systems.
A common scenario for such mechanism is when multiple clients try to update the same point independently.
Consider the following sequence of events:
 Client A reads point P.
 Client B reads point P.
 Client A modifies point P and writes it back to Qdrant.
 Client B modifies point P (based on the stale data) and writes it back to Qdrant, unintentionally overwriting changes made by Client A.
To prevent such situations, Client B can use conditional updates.
For this, we would need to introduce an additional field in the payload, e.g. `version`, which would be incremented on each update.
When Client A writes back the modified point P, it would set the condition that the `version` field must be equal to the value it read initially.
If Client B tries to write back its changes later, the condition would fail (as the `version` has been incremented by Client A), and Qdrant would reject the update, preventing accidental overwrites.
Instead of `version`, applications can use timestamps (assuming synchronized clocks) or any other monotonically increasing value that fits their data model.
This mechanism is especially useful in the scenarios of embedding model migration, where we need to resolve conflicts between regular application updates and background re-embedding tasks.
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1357
Retrieved by: dense 3, hybrid 7
Section: Introduction
--------------------------------------------------------------------------------

Introduction

With this code snippet, you can perform batch operations on points like upserting, updating vectors, deleting vectors, setting, overwriting, deleting, and clearing payload data associated with points. The operations include inserting, updating, and deleting points along with their vectors and payload. Each operation is executed in order specified in the request payload.

```http_code_1```


```java_code_2```


```python_code_3```


```rust_code_4```


```typescript_code_5```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1588
Retrieved by: dense 4, hybrid 6
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet triggers the update process for a specific collection named "{collection_name}" to resume paused optimizations indicated by the grey status or "optimizations pending, awaiting update operation" message. By sending a PATCH request with an empty "optimizers_config" object, the update operation is initiated, allowing the ongoing optimizations to start again.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 501
Retrieved by: dense 5, hybrid 10, colbert 10
Section: Points — Batch update
--------------------------------------------------------------------------------

Points — Batch update

_Available as of v1.5.0_
You can batch multiple point update operations. This includes inserting,
updating and deleting points, vectors and payload.
A batch update request consists of a list of operations. These are executed in
order. These operations can be batched:
 Upsert points: `upsert` or `UpsertOperation`
 Delete points: `delete_points` or `DeleteOperation`
 Update vectors: `update_vectors` or `UpdateVectorsOperation`
 Delete vectors: `delete_vectors` or `DeleteVectorsOperation`
 Set payload: `set_payload` or `SetPayloadOperation`
 Overwrite payload: `overwrite_payload` or `OverwritePayload`
 Delete payload: `delete_payload` or `DeletePayloadOperation`
 Clear payload: `clear_payload` or `ClearPayloadOperation`
The following example snippet makes use of all operations.
REST API (Schema):
{{}}
To batch many points with a single operation type, please use batching
functionality in that operation directly.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 632
Retrieved by: dense 6, sparse 6, hybrid 5, colbert 6
Section: Migrate to a New Embedding Model with Zero Downtime — Step 2: Enable Dual Writes
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — Step 2: Enable Dual Writes

To ensure that both collections are kept up-to-date during the migration, you need to write any changes to both collections simultaneously. This way, any new data or updates to existing data are reflected in both collections.
Ideally, the data in Qdrant is updated by an update service reading from an update queue. This service is responsible for embedding the documents and writing them to Qdrant. It uses code similar to this:
```python_code_1```
To update the new collection, deploy a second service that updates the new collection in parallel with the existing one. This service uses the new embedding model to encode the documents and writes them to the new collection:
```python_code_2```
A good practice is to always ensure that both operations succeed. Any errors need to be handled on the client side. You could store errors in a log or "dead letter queue" for later processing. Transient errors can be retried at a later time. Other errors need to be analyzed and addressed accordingly.
If instead of update services, you have a monolithic application, you need to modify your application code to write to both collections simultaneously during the transition period. In your code, where you handle the embedding of the documents, you should add the logic to write to both collections.
Note that the method outlined in this tutorial only works for `upsert` operations. For example, a `delete` operation would fail on the new collection if a point does not exist yet, and that point would later be erroneously added by the migration process. If you use one of the following methods to modify points in your collection, you will need to pause those operations during the migration or implement additional logic to handle them:
 `.delete` removing specified points from the collection
 `.update_vectors` updating specified vectors on points
 `.delete_vectors` deleting specified vectors from points
 `.set_payload` setting payload values for specified points
 `.overwrite_payload` overwriting the entire payload of a specified point with a new payload
 `.delete_payload` deleting a specified key payload for points
 `.clear_payload` removing the entire payload for specified points
 `.batch_update_points` making batch updates to points, including their respective vectors and payloads
Please refer to the documentation of the SDK you are using, or the
HTTP/gRPC definitions, for the exact method names, as they may vary between languages.
After making these changes, you will be in a dual-write mode, where any change is written to both the old and new collection. This allows you to keep both collections up-to-date during the migration process.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 461
Retrieved by: dense 7, colbert 7
Section: Optimizer
--------------------------------------------------------------------------------

Optimizer

It is much more efficient to apply changes in batches than perform each change individually, as many other databases do. Qdrant here is no exception. Since Qdrant operates with data structures that are not always easy to change, it is sometimes necessary to rebuild those structures completely.
Storage optimization in Qdrant occurs at the segment level (see storage).
In this case, the segment to be optimized remains readable for the time of the rebuild.
The availability is achieved by wrapping the segment into a proxy that transparently handles data changes.
Changed data is placed in the copy-on-write segment, which has priority for retrieval and subsequent updates.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1592
Retrieved by: dense 8
Section: Introduction
--------------------------------------------------------------------------------

Introduction

This code snippet represents an operation to update vectors associated with points in a collection. The operation uses a PUT request to update vectors for specific points by providing their IDs along with the new vector data. This method ensures that only the specified vectors are updated, while leaving any unspecified vectors unchanged. It is important to note that all the provided points must already exist in the collection for the update to be successful.

```csharp_code_1```


```go_code_2```


```http_code_3```


```java_code_4```


```python_code_5```


```rust_code_6```


```typescript_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 633
Retrieved by: dense 9
Section: Migrate to a New Embedding Model with Zero Downtime — Step 3: Migrate the Existing Points into the New Collection
--------------------------------------------------------------------------------

Migrate to a New Embedding Model with Zero Downtime — Step 3: Migrate the Existing Points into the New Collection

Now that you're in dual-write mode, it is time to migrate the existing points from the old collection to the new one. This can be done in a separate process that runs
in parallel with the regular upsert services.
The migration process reads the points from the old collection, re-embeds them using the new model, and writes them to the new collection, making sure not to overwrite existing points inserted by the update service. Here's an example of what the code for such a migration process could look like:
```python_code_1```
Breaking down this code step by step:
 Data is read from the old collection in batches of 100 points using a scroll. The `last_offset` variable keeps track of the scroll position in the collection.
 For each batch of points, the process re-embeds the vectors using the new embedding model. It assumes that the original text used for embedding is stored in the payload under the key `text`.
 With the re-embedded vectors, it prepares conditional upsert operations for the new collection, keeping the original IDs and payloads. The conditional upserts use a filter condition to ensure that a point is only inserted if it does not already exist in the new collection. The filter checks whether a point with the given ID already exists. A point is only upserted if the ID does not exist in the new collection. This prevents overwriting newer updates from the regular update service.
 Finally, the process uses a batch update to upsert the re-embedded points into the new collection. Note that it uses `batch_update_points` instead of `upsert`, because `batch_update_points` allows you to specify an update condition per upsert operation.
This kind of migration process can take some time, and the offset can be stored in a persistent way, so you can resume the migration process in case of a failure. You can use a database, a file, or any other persistent storage to keep track of the last offset. Having said that, because the conditional upserts would not overwrite any points in the new collection, you could safely restart the migration process from the beginning if needed.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1245
Retrieved by: dense 10
Section: Distributed deployment — Consistency guarantees — Write ordering
--------------------------------------------------------------------------------

Distributed deployment — Consistency guarantees — Write ordering

Write `ordering` can be specified for any write request to serialize it through a single "leader" node,
which ensures that all write operations (issued with the same `ordering`) are performed and observed
sequentially.
 `weak` _(default)_ ordering does not provide any additional guarantees, so write operations can be freely reordered.
 `medium` ordering serializes all write operations through a dynamically elected leader, which might cause minor inconsistencies in case of leader change.
 `strong` ordering serializes all write operations through the permanent leader, which provides strong consistency, but write operations may be unavailable if the leader is down.
Some shard transfer methods may affect ordering guarantees.
```http_code_1```
```python_code_2```
```typescript_code_3```
```rust_code_4```
```java_code_5```
```csharp_code_6```
```go_code_7```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 463
Retrieved by: sparse 2, hybrid 3, colbert 3
Section: Optimizer — Merge Optimizer
--------------------------------------------------------------------------------

Optimizer — Merge Optimizer

The service may require the creation of temporary segments.
Such segments, for example, are created as copy-on-write segments during optimization itself.
It is also essential to have at least one small segment that Qdrant will use to store frequently updated data.
On the other hand, too many small segments lead to suboptimal search performance.
The merge optimizer constantly tries to reduce the number of segments if there
currently are too many. The desired number of segments is specified
with `default_segment_number` and defaults to the number of CPUs. The optimizer
may takes at least the three smallest segments and merges them into one.
Segments will not be merged if they'll exceed the maximum configured segment
size with `max_segment_size_kb`. It prevents creating segments that are too
large to efficiently index. Increasing this number may help to reduce the number
of segments if you have a lot of data, and can potentially improve search performance.
The criteria for starting the optimizer are defined in the configuration file.
Here is an example of parameter values:
```yaml_code_1```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 363
Retrieved by: sparse 3, hybrid 4, colbert 2
Section: Collections — Update collection parameters
--------------------------------------------------------------------------------

Collections — Update collection parameters

Dynamic parameter updates may be helpful, for example, for more efficient initial loading of vectors.
For example, you can disable indexing during the upload process, and enable it immediately after the upload is finished.
As a result, you will not waste extra computation resources on rebuilding the index.
The following command enables indexing for segments that have more than 10000 kB of vectors stored:
{{}}
The following parameters can be updated:
* `optimizers_config` see optimizer for details.
* `hnsw_config` see indexing for details.
* `quantization_config` see quantization for details.
* `vectors_config` vector-specific configuration, including individual `hnsw_config`, `quantization_config` and `on_disk` settings.
* `params` other collection parameters, including `write_consistency_factor` and `on_disk_payload`.
* `strict_mode_config` see strict mode for details.
Full API specification is available in schema definitions.
Calls to this endpoint may be blocking as it waits for existing optimizers to
finish. We recommended against using this in a production database as it may
introduce huge overhead due to the rebuilding of the index.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 364
Retrieved by: sparse 4, hybrid 8, colbert 9
Section: Collections — Update collection parameters — Update vector parameters
--------------------------------------------------------------------------------

Collections — Update collection parameters — Update vector parameters

Available as of v1.4.0
To update vector parameters using the collection update API, you must always specify a vector name. If your collection does not have named vectors, use an empty ("") name.
Qdrant 1.4 adds support for updating more collection parameters at runtime. HNSW
index, quantization and disk configurations can now be changed without
recreating a collection. Segments (with index and quantized data) will
automatically be rebuilt in the background to match updated parameters.
To put vector data on disk for a collection that does not have named vectors,
use `""` as name:
{{}}
To put vector data on disk for a collection that does have named vectors:
Note: To create a vector name, follow the procedure from our Points.
{{}}
In the following example the HNSW index and quantization parameters are updated,
both for the whole collection, and for `my_vector` specifically:
{{}}

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1587
Retrieved by: sparse 5, hybrid 9
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Update collection parameters to adjust the optimizer's configuration. In this case, the code snippet demonstrates how to patch the collection by setting an indexing threshold of 10000 for more efficient initial loading of vectors. This allows you to optimize resource usage by enabling indexing selectively based on the number of vectors stored in each segment.

```bash_code_1```


```csharp_code_2```


```go_code_3```


```http_code_4```


```java_code_5```


```python_code_6```


```rust_code_7```


```typescript_code_8```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1589
Retrieved by: sparse 7
Section: Introduction
--------------------------------------------------------------------------------

Introduction

Update the collection with patch requests to put vector data on disk. This functionality allows you to specify vector parameters, such as setting vectors to be stored on disk, for a specific collection. In cases where the collection does not have named vectors, an empty name (`""`) should be used to perform this update. This feature provided by Qdrant version 1.4 enables modifications to collection parameters, including HNSW index, quantization, and disk configurations dynamically, without the need to recreate the collection. Additionally, segments containing index and quantized data will be automatically rebuilt in the background to align with the new parameters.

```bash_code_1```


```http_code_2```

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 537
Retrieved by: sparse 8
Section: Storage
--------------------------------------------------------------------------------

Storage

All data within one collection is divided into segments.
Each segment has its independent vector and payload storage as well as indexes.
Data stored in segments usually do not overlap.
However, storing the same point in different segments will not cause problems since the search contains a deduplication mechanism.
The segments consist of vector and payload storages, vector and payload indexes, and id mapper, which stores the relationship between internal and external ids.
A segment can be `appendable` or `non-appendable` depending on the type of storage and index used.
You can freely add, delete and query data in the `appendable` segment.
With `non-appendable` segment can only read and delete data.
The configuration of the segments in the collection can be different and independent of one another, but at least one `appendable' segment must be present in a collection.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 935
Retrieved by: sparse 9
Section: Frequently Asked Questions: General Topics — Search — How does Qdrant handle real-time data updates and search?
--------------------------------------------------------------------------------

Frequently Asked Questions: General Topics — Search — How does Qdrant handle real-time data updates and search?

Qdrant supports live updates for vector data, with newly inserted, updated and deleted vectors available for immediate search. The system uses full-scan search on unindexed segments during background index updates.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 677
Retrieved by: sparse 10
Section: Synchronizing Qdrant Edge with a Server — Update a Server Collection from an Edge Shard
--------------------------------------------------------------------------------

Synchronizing Qdrant Edge with a Server — Update a Server Collection from an Edge Shard

To synchronize data from an Edge Shard to a server collection, implement a dual-write mechanism in your application. When you add or update a point in the Edge Shard, simultaneously store it in a server collection using the Qdrant client.
Instead of writing to the server collection directly, you may want to set up a background job or a message queue that handles the synchronization asynchronously. The device running the Edge Shard may not always have a stable internet connection, so queuing updates ensures that data is eventually synchronized when connectivity is restored.
First, initialize:
 an Edge Shard from scratch or from server-side snapshot
 Qdrant server connection.
Details
Initialize an Edge Shard:
```python_code_1```
Initialize a Qdrant client connection to the server and create the target collection if it does not exist:
```python_code_2```
Next, instantiate the queue that will hold the points that need to be synchronized with the server:
```python_code_3```
When adding or updating points in the Edge Shard, also enqueue the point for synchronization with the server.
```python_code_4```
A background worker can process the upload queue and synchronize points with the server collection.
This example uploads points in batches of up to 10 points at a time:
```python_code_5```
Make sure to properly handle errors and retries in case of network issues or server unavailability.

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 1235
Retrieved by: colbert 5
Section: Distributed deployment — Sharding — Shard transfer method
--------------------------------------------------------------------------------

Distributed deployment — Sharding — Shard transfer method

to transfer a shard. A snapshot is created automatically. It is then transferred
and restored on the target node. After this is done, the snapshot is removed
from both nodes. While the snapshot/transfer/restore operation is happening, the
source node queues up all new operations. All queued updates are then sent in
order to the target shard to bring it into the same state as the source. There
are two important benefits: 1. It transfers index and quantization data, so that
the shard does not have to be optimized again on the target node, making them
immediately available. This way, Qdrant ensures that there will be no
degradation in performance at the end of the transfer. Especially on large
shards, this can give a huge performance improvement. 2. The ordering guarantees
can be `strong`[^ordered], required for some applications.
The `wal_delta` transfer method only transfers the difference between two
shards. More specifically, it transfers all operations that were missed to the
target shard. The [WAL] of both shards is used to resolve this. There are two
benefits: 1. It will be very fast because it only transfers the difference
rather than all data. 2. The ordering guarantees can be `strong`[^ordered],
required for some applications. Two disadvantages are: 1. It can only be used to
transfer to a shard that already exists on the other node. 2. Applicability is
limited because the WALs normally don't hold more than 64MB of recent
operations. But that should be enough for a node that quickly restarts, to
upgrade for example. If a delta cannot be resolved, this method automatically
falls back to `stream_records` which equals transferring the full shard.
The `stream_records` method is currently used as default. This may change in the
future. As of Qdrant 1.9.0 `wal_delta` is used for automatic shard replications
to recover dead shards.
[WAL]: /documentation/concepts/storage/#versioning

[RELEVANT? 2 / 1 / 0]

--------------------------------------------------------------------------------
Chunk ID: 477
Retrieved by: colbert 8
Section: Payload — Update payload — Overwrite payload
--------------------------------------------------------------------------------

Payload — Update payload — Overwrite payload

Fully replace any existing payload with the given one.
REST API (Schema):
{{}}
Like set payload, you don't need to know the ids of the points
you want to modify. The alternative is to use filters.

[RELEVANT? 2 / 1 / 0]



