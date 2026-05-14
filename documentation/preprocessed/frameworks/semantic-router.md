---
title: Semantic-Router
---
# Semantic-Router
Semantic-Router is a library to build decision-making layers for your LLMs and agents. It uses vector embeddings to make tool-use decisions rather than LLM generations, routing our requests using semantic meaning.
Qdrant is available as a supported index in Semantic-Router for you to ingest route data and perform retrievals.
## Installation
To use Semantic-Router with Qdrant, install the `qdrant` extra:
```console
pip install semantic-router[qdrant]
```
## Usage
Set up `QdrantIndex` with the appropriate configurations:
```python
from semantic_router.index import QdrantIndex
qdrant_index = QdrantIndex(
    url="the linked resource api_key=""
)
```
Once the Qdrant index is set up with the appropriate configurations, we can pass it to the `RouteLayer`.
```python
from semantic_router.layer import RouteLayer
RouteLayer(encoder=some_encoder, routes=some_routes, index=qdrant_index)
```
## Complete Example
Click to expand
```python
import os
from semantic_router import Route
from semantic_router.encoders import OpenAIEncoder
from semantic_router.index import QdrantIndex
from semantic_router.layer import RouteLayer
# we could use this as a guide for our chatbot to avoid political conversations
politics = Route(
    name="politics value",
    utterances=[
        "isn't politics the best thing ever",
        "why don't you tell me about your political opinions",
        "don't you just love the president",
        "they're going to destroy this country!",
        "they will save the country!",
    ],
)
# this could be used as an indicator to our chatbot to switch to a more
# conversational prompt
chitchat = Route(
    name="chitchat",
    utterances=[
        "how's the weather today?",
        "how are things going?",
        "lovely weather today",
        "the weather is horrendous",
        "let's go to the chippy",
    ],
)
# we place both of our decisions together into single list
routes = [politics, chitchat]
os.environ["OPENAI_API_KEY"] = ""
encoder = OpenAIEncoder()
rl = RouteLayer(
    encoder=encoder,
    routes=routes,
    index=QdrantIndex(location=":memory:"),
)
print(rl("What have you been upto?").name)
```
This returns:
```console
[Out]: 'chitchat'
```
## 📚 Further Reading
 Semantic-Router Documentation
 Semantic-Router Video Course
 Source Code
