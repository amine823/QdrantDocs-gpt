---
title: InfinyOn Fluvio
---
InfinyOn Fluvio is an open-source platform written in Rust for high speed, real-time data processing. It is cloud native, designed to work with any infrastructure type, from bare metal hardware to containerized platforms.
## Usage with Qdrant
With the Qdrant Fluvio Connector, you can stream records from Fluvio topics to Qdrant collections, leveraging Fluvio's delivery guarantees and high-throughput.
### Pre-requisites
 A Fluvio installation. You can refer to the Fluvio Quickstart for instructions.
 Qdrant server to connect to. You can set up a local instance or a free cloud instance at cloud.qdrant.io.
### Downloading the connector
Run the following commands after setting up Fluvio.
```console
cdk hub download qdrant/qdrant-sink@0.1.0
```
### Example Config
> _config.yaml_
```yaml
apiVersion: 0.1.0
meta:
  version: 0.1.0
  name: my-qdrant-connector
  type: qdrant-sink
  topic: topic-name
  secrets:
     name: QDRANT_API_KEY
qdrant:
  url: the linked resource
  api_key: "${{ secrets.QDRANT_API_KEY }}"
```
> _secrets.txt_
```text
QDRANT_API_KEY=
```
### Running
```console
cdk deploy start --ipkg qdrant-qdrant-sink-0.1.0.ipkg -c config.yaml --secrets secrets.txt
```
### Produce Messages
You can now run the following to generate messages to be written into Qdrant.
```console
fluvio produce topic-name
```
### Message Formats
This sink connector supports messages with dense/sparse/multi vectors.
_Click each to expand._
 Unnamed/Default vector
Reference: Creating a collection with a default vector.
```json
{
    "collection_name": "{collection_name}",
    "id": 1,
    "vectors": [
        0.1,
        0.2,
        0.3,
        0.4,
        0.5,
        0.6,
        0.7,
        0.8
    ],
    "payload": {
        "name": "fluvio",
        "description": "Solution for distributed stream processing",
        "url": "the linked resource
    }
}
```
 Named multiple vectors
Reference: Creating a collection with multiple vectors.
```json
{
    "collection_name": "{collection_name}",
    "id": 1,
    "vectors": {
        "some-dense": [
            0.1,
            0.2,
            0.3,
            0.4,
            0.5,
            0.6,
            0.7,
            0.8
        ],
        "some-other-dense": [
            0.1,
            0.2,
            0.3,
            0.4,
            0.5,
            0.6,
            0.7,
            0.8
        ]
    },
    "payload": {
        "name": "fluvio",
        "description": "Solution for distributed stream processing",
        "url": "the linked resource
    }
}
```
 Sparse vectors
Reference: Creating a collection with sparse vectors.
```json
{
    "collection_name": "{collection_name}",
    "id": 1,
    "vectors": {
        "some-sparse": {
            "indices": [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ],
            "values": [
                0.1,
                0.2,
                0.3,
                0.4,
                0.5,
                0.6,
                0.7,
                0.8,
                0.9,
                1.0
            ]
        }
    },
    "payload": {
        "name": "fluvio",
        "description": "Solution for distributed stream processing",
        "url": "the linked resource
    }
}
```
 Multi-vector
```json
{
    "collection_name": "{collection_name}",
    "id": 1,
    "vectors": {
        "some-multi": [
            [
                0.1,
                0.2,
                0.3,
                0.4,
                0.5,
                0.6,
                0.7,
                0.8,
                0.9,
                1.0
            ],
            [
                1.0,
                0.9,
                0.8,
                0.5,
                0.4,
                0.8,
                0.6,
                0.4,
                0.2,
                0.1
            ]
        ]
    },
    "payload": {
        "name": "fluvio",
        "description": "Solution for distributed stream processing",
        "url": "the linked resource
    }
}
```
 Combination of named dense and sparse vectors
Reference:
 Creating a collection with multiple vectors.
 Creating a collection with sparse vectors.
```json
{
    "collection_name": "{collection_name}",
    "id": "a10435b5-2a58-427a-a3a0-a5d845b147b7",
    "vectors": {
        "some-other-dense": [
            0.1,
            0.2,
            0.3,
            0.4,
            0.5,
            0.6,
            0.7,
            0.8
        ],
        "some-sparse": {
            "indices": [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ],
            "values": [
                0.1,
                0.2,
                0.3,
                0.4,
                0.5,
                0.6,
                0.7,
                0.8,
                0.9,
                1.0
            ]
        }
    },
    "payload": {
        "name": "fluvio",
        "description": "Solution for distributed stream processing",
        "url": "the linked resource
    }
}
```
### Further Reading
 Fluvio Quickstart
 Fluvio Tutorials
 Connector Source
