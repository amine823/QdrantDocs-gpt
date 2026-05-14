---
title: Confluent Kafka
---
Built by the original creators of Apache Kafka®, Confluent Cloud is a cloud-native and complete data streaming platform available on AWS, Azure, and Google Cloud. The platform includes a fully managed, elastically scaling Kafka engine, 120+ connectors, serverless Apache Flink®, enterprise-grade security controls, and a robust governance suite.
With our Qdrant-Kafka Sink Connector, Qdrant is part of the Connect with Confluent technology partner program. It brings fully managed data streams directly to organizations from Confluent Cloud, making it easier for organizations to stream any data to Qdrant with a fully managed Apache Kafka service.
## Usage
### Pre-requisites
 A Confluent Cloud account. You can begin with a free trial with credits for the first 30 days.
 Qdrant instance to connect to. You can get a free cloud instance at cloud.qdrant.io.
### Installation
1) Download the latest connector zip file from Confluent Hub.
2) Configure an environment and cluster on Confluent and create a topic to produce messages for.
3) Navigate to the `Connectors` section of the Confluent cluster and click `Add Plugin`. Upload the zip file with the following info.
4) Once installed, navigate to the connector and set the following configuration values.
Replace the placeholder values with your credentials.
5) Add the Qdrant instance host to the allowed networking endpoints.
7) Start the connector.
## Producing Messages
You can now produce messages for the configured topic, and they'll be written into the configured Qdrant instance.
## Message Formats
The connector supports messages in the following formats.
_Click each to expand._
 Unnamed/Default vector
Reference: Creating a collection with a default vector.
```json
{
    "collection_name": "{collection_name}",
    "id": 1,
    "vector": [
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
        "name": "kafka",
        "description": "Kafka is a distributed streaming platform",
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
    "vector": {
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
        "name": "kafka",
        "description": "Kafka is a distributed streaming platform",
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
    "vector": {
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
        "name": "kafka",
        "description": "Kafka is a distributed streaming platform",
        "url": "the linked resource
    }
}
```
 Multi-vectors
Reference:
 Multi-vectors
```json
{
    "collection_name": "{collection_name}",
    "id": 1,
    "vector": {
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
        "name": "kafka",
        "description": "Kafka is a distributed streaming platform",
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
    "vector": {
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
        "name": "kafka",
        "description": "Kafka is a distributed streaming platform",
        "url": "the linked resource
    }
}
```
## Further Reading
 Kafka Connect Docs
 Confluent Connectors Docs
