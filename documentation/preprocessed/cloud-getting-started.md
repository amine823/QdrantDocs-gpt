---
title: Getting Started
---
# Getting Started with Qdrant Managed Cloud
Welcome to Qdrant Managed Cloud! This document contains all the information you need to get started.
## Prerequisites
Before creating a cluster, make sure you have a Qdrant Cloud account. Detailed instructions for signing up can be found in the Qdrant Cloud Setup guide. Qdrant Cloud supports granular role-based access control.
You also need to provide payment details. If you have a custom payment agreement, first create your account, then contact our Support Team to finalize the setup.
Premium Plan subscribers can enable single sign-on (SSO) for their organizations. To activate SSO, please reach out to the Support Team at the Qdrant support portal for guidance.
## Cluster Sizing
Before deploying any cluster, consider the resources needed for your specific workload. Our Capacity Planning guide describes how to assess the required CPU, memory, and storage. Additionally, the Pricing Calculator helps you estimate associated costs based on your projected usage.
## Creating and Managing Clusters
After setting up your account, you can create a Qdrant Cluster by following the steps in Create a Cluster.
## Preparing for Production
For a production-ready environment, consider deploying a multi-node Qdrant cluster (at least three nodes) with replication enabled. More details are available in the Distributed Deployment guide. For more information on how to create a production-ready cluster, see our Vector Search in Production article.
If you are looking to optimize costs, you can reduce memory usage through Quantization or by offloading vectors to disk.
## Infrastructure as Code Automation
Qdrant Cloud can be fully automated using the Qdrant Cloud API. This allows you to create, manage, and scale clusters programmatically. You can also use our Terraform Provider to automate your Qdrant Cloud infrastructure.
