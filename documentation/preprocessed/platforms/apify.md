---
title: Apify
---
# Apify
Apify is a web scraping and browser automation platform featuring an app store with over 1,500 pre-built micro-apps known as Actors. These serverless cloud programs, which are essentially dockers under the hood, are designed for various web automation applications, including data collection.
One such Actor, built especially for AI and RAG applications, is Website Content Crawler.
It's ideal for this purpose because it has built-in HTML processing and data-cleaning functions. That means you can easily remove fluff, duplicates, and other things on a web page that aren't relevant, and provide only the necessary data to the language model.
The Markdown can then be used to feed Qdrant to train AI models or supply them with fresh web content.
Qdrant is available as an official integration to load Apify datasets into a collection.
You can refer to the Apify documentation to set up the integration via the Apify UI.
## Programmatic Usage
Apify also supports programmatic access to integrations via the Apify Python SDK.
1. Install the Apify Python SDK by running the following command:
```sh
    pip install apify-client
```
2. Create a Python script and import all the necessary modules:
```python
    from apify_client import ApifyClient
    APIFY_API_TOKEN = "YOUR-APIFY-TOKEN"
    OPENAI_API_KEY = "YOUR-OPENAI-API-KEY"
    # COHERE_API_KEY = "YOUR-COHERE-API-KEY"
    QDRANT_URL = "YOUR-QDRANT-URL"
    QDRANT_API_KEY = "YOUR-QDRANT-API-KEY"
    client = ApifyClient(APIFY_API_TOKEN)
```
3. Call the Website Content Crawler Actor to crawl the Qdrant documentation and extract text content from the web pages:
```python
    actor_call = client.actor("apify/website-content-crawler").call(
        run_input={"startUrls": [{"url": "the linked resource
    )
```
4. Call the Qdrant integration and store all data in the Qdrant Vector Database:
```python
    qdrant_integration_inputs = {
        "qdrantUrl": QDRANT_URL,
        "qdrantApiKey": QDRANT_API_KEY,
        "qdrantCollectionName": "apify",
        "qdrantAutoCreateCollection": True,
        "datasetId": actor_call["defaultDatasetId"],
        "datasetFields": ["text"],
        "enableDeltaUpdates": True,
        "deltaUpdatesPrimaryDatasetFields": ["url"],
        "expiredObjectDeletionPeriodDays": 30,
        "embeddingsProvider": "OpenAI", # "Cohere"
        "embeddingsApiKey": OPENAI_API_KEY,
        "performChunking": True,
        "chunkSize": 1000,
        "chunkOverlap": 0,
    }
    actor_call = client.actor("apify/qdrant-integration").call(run_input=qdrant_integration_inputs)
```
Upon running the script, the data from will be scraped, transformed into vector embeddings and stored in the Qdrant collection.
## Further Reading
 Apify Documentation
 Apify Templates
 Integration Source Code
