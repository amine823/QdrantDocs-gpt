---
title: Datadog
---
Datadog is a cloud-based monitoring and analytics platform that offers real-time monitoring of servers, databases, and numerous other tools and services. It provides visibility into the performance of applications and enables businesses to detect issues before they affect users.
You can install the Qdrant integration to get real-time metrics to monitor your Qdrant deployment within Datadog including:
 The performance of REST and gRPC interfaces with metrics such as total requests, total failures, and time to serve to identify potential bottlenecks and mitigate them.
 Information about the readiness of the cluster, and deployment (total peers, pending operations, etc.) to gain insights into your Qdrant deployment.
### Usage
 With the Datadog Agent installed, run the following command to add the Qdrant integration:
```shell
datadog-agent integration install -t qdrant==1.0.0
```
 Edit the `conf.d/qdrant.d/conf.yaml` file in your Agent's configuration directory to start collecting your Qdrant metrics.
Most importantly, set the `openmetrics_endpoint` value to the `/metrics` endpoint of your Qdrant instance.
```yaml
instances:
    ## @param openmetrics_endpoint  string  optional
    ## The URL exposing metrics in the OpenMetrics format.
   openmetrics_endpoint: the local Qdrant dashboardmetrics
```
If the Qdrant instance requires authentication, you can specify the token by configuring `extra_headers`.
```yaml
# @param extra_headers  mapping  optional
# Additional headers to send with every request.
extra_headers:
   api-key:
```
 Restart the Datadog agent.
 You can now head over to the Datadog dashboard to view the metrics emitted by the Qdrant check.
## Further Reading
 Getting started with Datadog
 Qdrant integration source
