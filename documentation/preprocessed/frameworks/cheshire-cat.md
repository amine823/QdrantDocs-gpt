---
title: Cheshire Cat
---
# Cheshire Cat
Cheshire Cat is an open-source framework that allows you to develop intelligent agents on top of many Large Language Models (LLM). You can develop your custom AI architecture to assist you in a wide range of tasks.
## Cheshire Cat and Qdrant
Cheshire Cat uses Qdrant as the default Vector Memory for ingesting and retrieving documents.
```
# Decide host and port for your Cat. Default will be localhost:1865
CORE_HOST=localhost
CORE_PORT=1865
# Qdrant server
# QDRANT_HOST=localhost
# QDRANT_PORT=6333
```
Cheshire Cat takes great advantage of the following features of Qdrant:
* Collection Aliases to manage the change from one embedder to another.
* Quantization to obtain a good balance between speed, memory usage and quality of the results.
* Snapshots to not miss any information.
* Community
## How to use the Cheshire Cat
### Requirements
To run the Cheshire Cat, you need to have Docker and docker-compose already installed on your system.
```shell
docker run --rm -it -p 1865:80 ghcr.io/cheshire-cat-ai/core:latest
```
* Chat with the Cheshire Cat on localhost:1865/admin.
* You can also interact via REST API and try out the endpoints on localhost:1865/docs
Check the instructions on github for a more comprehensive quick start.
### First configuration of the LLM
* Open the Admin Portal in your browser at localhost:1865/admin.
* Configure the LLM in the `Settings` tab.
* If you don't explicitly choose it using `Settings` tab, the Embedder follows the LLM.
## Next steps
For more information, refer to the Cheshire Cat documentation and blog.
* Getting started
* How the Cat works
* Write Your First Plugin
* Cheshire Cat's use of Qdrant Vector Space
* Cheshire Cat's use of Qdrant Aliases
* Cheshire Cat's use of Qdrant Quantization
* Cheshire Cat at Qdrant vector Space Talks
* Discord Community
