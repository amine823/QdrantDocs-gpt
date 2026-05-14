---
title: Microsoft NLWeb
---
# NLWeb
Microsoft's NLWeb is a proposed framework that enables natural language interfaces for websites, using Schema.org, formats like RSS and the emerging MCP protocol.
Qdrant is supported as a vector store backend within NLWeb for embedding storage and context retrieval.
## Usage
NLWeb includes Qdrant integration by default. You can install and configure it to use Qdrant as the retrieval engine.
### Installation
Clone the repo and set up your environment:
```bash
git clone the linked resource
cd NLWeb
python -m venv .venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
cd code
pip install -r requirements.txt
```
### Configuring Qdrant
To use Qdrant, update your configuration.
#### 1. Copy and edit the environment variables file
```bash
cp .env.template .env
```
Ensure the following values are set in your `.env` file:
```text
QDRANT_URL="the linked resource
QDRANT_API_KEY=""
```
#### 2. Update config files in `code/config`
 `config_retrieval.yaml`*
```yaml
retrieval_engine: qdrant_url
```
Alternatively, you can use an in-memory Qdrant instance for experimentation.
```yaml
retrieval_engine: qdrant_local
endpoints:
  qdrant_local:
    # Path to a local directory
    database_path: "../data/"
    # Set the collection name to use
    index_name: nlweb_collection
    # Specify the database type
    db_type: qdrant
```
### Loading Data
Once configured, load your content using RSS feeds.
From the `code` directory:
```bash
python -m tools.db_load the linked resource Behind-the-Tech
```
This will ingest the content into your local Qdrant instance.
### Running the Server
To start NLWeb, from the `code` directory, run:
```bash
python app-file.py
```
You can now query your content via natural language using either the web UI at or directly through the MCP-compatible REST API.
## Further Reading
* Source
* Life of a Chat Query
* Modifying behavior by changing prompts
* Modifying control flow
* Modifying the user interface
