---
title: Cluster Access
---
# Accessing Qdrant Cloud Clusters
Once you created a cluster, and set up an API key, you can access your cluster through the integrated Cluster UI, the REST API and the GRPC API.
## Cluster UI
You can access your Cluster UI via the Cluster Details page in the Qdrant Cloud Console. Authentication to a cluster is automatic if your cloud user has the `read:cluster_data` or `write:cluster_data` permission. Without the correct permissions you will be prompted to enter an API Key to access the cluster.
The Overview tab also contains direct links to explore Qdrant tutorials and sample datasets.
## API
The REST API is exposed on your cluster endpoint at port `6333`. The GRPC API is exposed on your cluster endpoint at port `6334`. When accessing the cluster endpoint, traffic is automatically load balanced across all healthy Qdrant nodes in the cluster. For all operations, but the few mentioned at Node specific endpoints, you should use the cluster endpoint. It does not matter which node in the cluster you land on. All nodes can handle all search and write requests.
Have a look at the API reference and the official client libraries for more information on how to interact with the Qdrant Cloud API.
## Node Specific Endpoints
Next to the cluster endpoint which loadbalances requests across all healthy Qdrant nodes, each node in the cluster has its own endpoint as well. This is mainly usefull for monitoring or manual shard management purpuses.
You can finde the node specific endpoints on the cluster detail page in the Qdrant Cloud Console.
## Restricting Cluster Access by IP Range
You can restrict access to your cluster by specifying allowed IP ranges. This ensures that only clients connecting from the specified IP ranges can access the cluster. For more information, see Client IP Restrictions.
