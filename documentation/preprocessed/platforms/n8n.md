---
title: N8N
---
# N8N
N8N is an automation platform that allows you to build flexible workflows focused on deep data integration.
Qdrant's official node for n8n enables semantic search capabilities in your workflows.
## Prerequisites
1. A Qdrant instance to connect to. You can get a free cloud instance at cloud.qdrant.io.
2. A running N8N instance. You can learn more about using the N8N cloud or self-hosting here.
## Setting up the node
 Select and install the official Qdrant node from the list of nodes in your workflow editor.
 Once installed, you can create a connection to Qdrant using your credentials.
## Operations
The node supports the following operations:
### Collection
 List Collections List all collections in the Qdrant instance
 Create Collection Create a new collection with specified vector parameters
 Update Collection Update parameters of an existing collection
 Get Collection Get information about a specific collection
 Collection Exists Check if a collection exists
 Delete Collection Delete a collection
### Point
 Upsert Points Insert or update points in a collection
 Retrieve Point Get a single point by ID
 Retrieve Points Get multiple points by their IDs
 Delete Points Remove points from a collection
 Count Points Count points in a collection with optional filtering
 Scroll Points Scroll through all points in a collection
 Batch Update Points Perform multiple point operations in a single request
### Vector
 Update Vectors Update vectors for existing points
 Delete Vectors Remove vectors from points
### Search
 Query Points Search for similar vectors
 Query Points In Batch Perform multiple vector searches in batch
 Query Points Groups Group search results by payload field
 Matrix Pairs Calculate distance matrix between pairs of points
 Matrix Offsets Calculate distance matrix using offsets
### Payload
 Set Payload Set payload for points
 Overwrite Payload Replace entire payload for points
 Delete Payload Remove payload from points
 Clear Payload Clear all payload fields
 Payload Facets Get payload field statistics
 Create Payload Index Create an index for payload fields
 Delete Payload Index Remove a payload field index
## Further Reading
 N8N Reference.
 Qdrant Node Source.
