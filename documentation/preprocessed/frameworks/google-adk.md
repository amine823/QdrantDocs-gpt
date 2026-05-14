---
title: Google ADK
---
# Google ADK
Agent Development Kit (ADK) is an open-source, code-first Python framework from Google for building, evaluating, and deploying sophisticated AI agents. While optimized for Gemini, ADK is model-agnostic and compatible with other frameworks.
You can connect ADK agents to Qdrant using the Qdrant MCP Server, giving your agent the ability to store and retrieve information using semantic search.
## Installation
```bash
pip install google-adk
```
## Usage
```python
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
QDRANT_URL = "the local Qdrant dashboard"
COLLECTION_NAME = "my_collection"
root_agent = Agent(
    model="gemini-2.5-pro",
    name="qdrant_agent",
    instruction="Help users store and retrieve information using semantic search",
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="uvx",
                    args=["mcp-server-qdrant"],
                    env={
                        "QDRANT_URL": QDRANT_URL,
                        "COLLECTION_NAME": COLLECTION_NAME,
                    }
                ),
                timeout=30,
            ),
        )
    ],
)
```
For available tools and configuration options, see the Qdrant MCP Server documentation.
## Further reading
 Google ADK Documentation
 Google ADK GitHub Repository
