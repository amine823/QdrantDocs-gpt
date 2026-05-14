---
title: OpenLLMetry
---
# OpenLLMetry
OpenLLMetry from Traceloop is a set of extensions built on top of OpenTelemetry that gives you complete observability over your LLM application.
OpenLLMetry supports instrumenting the `qdrant_client` Python library and exporting the traces to various observability platforms, as described in their Integrations catalog.
This page assumes you're using `qdrant-client` version 1.7.3 or above.
## Usage
To set up OpenLLMetry, follow these steps:
1. Install the SDK:
```console
pip install traceloop-sdk
```
1. Instantiate the SDK:
```python
from traceloop.sdk import Traceloop
Traceloop.init()
```
You're now tracing your `qdrant_client` usage with OpenLLMetry!
## Without the SDK
Since Traceloop provides standard OpenTelemetry instrumentations, you can use them as standalone packages. To do so, follow these steps:
1. Install the package:
```console
pip install opentelemetry-instrumentation-qdrant
```
1. Instantiate the `QdrantInstrumentor`.
```python
from opentelemetry.instrumentation.qdrant import QdrantInstrumentor
QdrantInstrumentor().instrument()
```
## Further Reading
 📚 OpenLLMetry API reference
 📄 Source Code
