---
title: Inference with Mighty
description: We combine Mighty and Qdrant to create a semantic search service in Rust
  with just a few lines of code.
---
# Semantic Search with Mighty and Qdrant
Much like Qdrant, the Mighty inference server is written in Rust and promises to offer low latency and high scalability. This brief demo combines Mighty and Qdrant into a simple semantic search service that is efficient, affordable and easy to setup. We will use Rust and our qdrant\_client crate for this integration.
## Initial setup
For Mighty, start up a docker container with an open port 5050. Just loading the port in a window shows the following:
```json
{
  "name": "sentence-transformers/all-MiniLM-L6-v2",
  "architectures": [
    "BertModel"
  ],
  "model_type": "bert",
  "max_position_embeddings": 512,
  "labels": null,
  "named_entities": null,
  "image_size": null,
  "source": "the linked resource
}
```
Note that this uses the `MiniLM-L6-v2` model from Hugging Face. As per their website, the model "maps sentences & paragraphs to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search". The distance measure to use is cosine similarity.
Verify that mighty works by calling `curl This will give you a result like (formatted via `jq`):
```json
{
    "outputs": [
        [
            -0.05019686743617058,
            0.051746174693107605,
            0.048117730766534805,
            ... (381 values skipped)
        ]
    ],
    "shape": [
        1,
        384
    ],
    "texts": [
        "Hello mighty"
    ],
    "took": 77
}
```
For Qdrant, follow our cloud documentation to spin up a free tier. Make sure to retrieve an API key.
## Implement model API
For mighty, you will need a way to emit HTTP(S) requests. This version uses the reqwest crate, so add the following to your `Cargo.toml`'s dependencies section:
```toml
[dependencies]
reqwest =  { version = "0.11.18", default-features = false, features = ["json", "rustls-tls"] }
```
Mighty offers a variety of model APIs which will download and cache the model on first use. For semantic search, use the `sentence-transformer` API (as in the above `curl` command). The Rust code to make the call is:
```rust
use anyhow::anyhow;
use reqwest::Client;
use serde::Deserialize;
use serde_json::Value as JsonValue;
#[derive(Deserialize)]
struct EmbeddingsResponse {
    pub outputs: Vec>,
}
pub async fn get_mighty_embedding(
    client: &Client,
    url: &str,
    text: &str
) -> anyhow::Result> {
    let response = client.get(url).query(&[("text", text)]).send().await?;
    if !response.status().is_success() {
        return Err(anyhow!(
            "Mighty API returned status code {}",
            response.status()
        ));
    }
    let embeddings: EmbeddingsResponse = response.json().await?;
    // ignore multiple embeddings at the moment
    embeddings.get(0).ok_or_else(|| anyhow!("mighty returned empty embedding"))
}
```
Note that mighty can return multiple embeddings (if the input is too long to fit the model, it is automatically split).
## Create embeddings and run a query
Use this code to create embeddings both for insertion and search. On the Qdrant side, take the embedding and run a query:
```rust
use anyhow::anyhow;
use qdrant_client::prelude::*;
pub const SEARCH_LIMIT: u64 = 5;
const COLLECTION_NAME: &str = "mighty";
pub async fn qdrant_search_embeddings(
    qdrant_client: &QdrantClient,
    vector: Vec,
) -> anyhow::Result> {
    qdrant_client
        .search_points(&SearchPoints {
            collection_name: COLLECTION_NAME.to_string(),
            vector,
            limit: SEARCH_LIMIT,
            with_payload: Some(true.into()),
            ..Default::default()
        })
        .await
        .map_err(|err| anyhow!("Failed to search Qdrant: {}", err))
}
```
You can convert the `ScoredPoint`s to fit your desired output format.
