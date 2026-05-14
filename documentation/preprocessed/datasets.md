---
title: Practice Datasets
---
# Common Datasets in Snapshot Format
You may find that creating embeddings from datasets is a very resource-intensive task.
If you need a practice dataset, feel free to pick one of the ready-made snapshots on this page.
These snapshots contain pre-computed vectors that you can easily import into your Qdrant instance.
## Available datasets
Our snapshots are usually generated from publicly available datasets, which are often used for
non-commercial or academic purposes. The following datasets are currently available. Please click
on a dataset name to see its detailed description.
Arxiv.org titles — InstructorXL — 768 — 2.3M — 7.1 GB — Download — Open
Arxiv.org abstracts — InstructorXL — 768 — 2.3M — 8.4 GB — Download — Open
Wolt food — clip-ViT-B-32 — 512 — 1.7M — 7.9 GB — Download — Open
Once you download a snapshot, you need to restore it
using the Qdrant CLI upon startup or through the API.
## Qdrant on Hugging Face
Hugging Face provides a platform for sharing and using ML models and
datasets. Qdrant is one of the organizations there! We aim to
provide you with datasets containing neural embeddings that you can use to practice with Qdrant
and build your applications based on semantic search. Please let us know if you'd like to see
a specific dataset!
If you are not familiar with Hugging Face datasets,
or would like to know how to combine it with Qdrant, please refer to the tutorial.
## Arxiv.org
Arxiv.org is a highly-regarded open-access repository of electronic preprints in multiple
fields. Operated by Cornell University, arXiv allows researchers to share their findings with
the scientific community and receive feedback before they undergo peer review for formal
publication. Its archives host millions of scholarly articles, making it an invaluable resource
for those looking to explore the cutting edge of scientific research. With a high frequency of
daily submissions from scientists around the world, arXiv forms a comprehensive, evolving dataset
that is ripe for mining, analysis, and the development of future innovations.
Arxiv.org snapshots were created using precomputed embeddings exposed by the Alexandria Index.
### Arxiv.org titles
This dataset contains embeddings generated from the paper titles only. Each vector has a
payload with the title used to create it, along with the DOI (Digital Object Identifier).
```json
{
    "title": "Nash Social Welfare for Indivisible Items under Separable, Piecewise-Linear Concave Utilities",
    "DOI": "1612.05191"
}
```
The embeddings generated with InstructorXL model have been generated using the following
instruction:
> Represent the Research Paper title for retrieval; Input:
The following code snippet shows how to generate embeddings using the InstructorXL model:
```python
from InstructorEmbedding import INSTRUCTOR
model = INSTRUCTOR("hkunlp/instructor-xl")
sentence = "3D ActionSLAM: wearable person tracking in multi-floor environments"
instruction = "Represent the Research Paper title for retrieval; Input:"
embeddings = model.encode([[instruction, sentence]])
```
The snapshot of the dataset might be downloaded here.
#### Importing the dataset
The easiest way to use the provided dataset is to recover it via the API by passing the
URL as a location. It works also in Qdrant Cloud. The following
code snippet shows how to create a new collection and fill it with the snapshot data:
```http request
PUT /collections/{collection_name}/snapshots/recover
{
  "location": "the linked resource
}
```
### Arxiv.org abstracts
This dataset contains embeddings generated from the paper abstracts. Each vector has a
payload with the abstract used to create it, along with the DOI (Digital Object Identifier).
```
json
{
    "abstract": "Recently Cole and Gkatzelis gave the first constant factor approximation\nalgorithm for the problem of allocating indivisible items to agents, under\nadditive valuations, so as to maximize the Nash Social Welfare. We give\nconstant factor algorithms for a substantial generalization of their problem --\nto the case of separable, piecewise-linear concave utility functions. We give\ntwo such algorithms, the first using market equilibria and the second using the\ntheory of stable polynomials.\n  In AGT, there is a paucity of methods for the design of mechanisms for the\nallocation of indivisible goods and the result of Cole and Gkatzelis seemed to\nbe taking a major step towards filling this gap. Our result can be seen as\nanother step in this direction.\n",
    "DOI": "1612.05191"
}
```
The embeddings generated with InstructorXL model have been generated using the following
instruction:
> Represent the Research Paper abstract for retrieval; Input:
The following code snippet shows how to generate embeddings using the InstructorXL model:
```
python
from InstructorEmbedding import INSTRUCTOR
model = INSTRUCTOR("hkunlp/instructor-xl")
sentence = "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train."
instruction = "Represent the Research Paper abstract for retrieval; Input:"
embeddings = model.encode([[instruction, sentence]])
```
The snapshot of the dataset might be downloaded here.
#### Importing the dataset
The easiest way to use the provided dataset is to recover it via the API by passing the
URL as a location. It works also in Qdrant Cloud. The following
code snippet shows how to create a new collection and fill it with the snapshot data:
```
http request
PUT /collections/{collection_name}/snapshots/recover
{
  "location": "the linked resource
}
```
## Wolt food
Our Food Discovery demo relies on the dataset of
food images from the Wolt app. Each point in the collection represents a dish with a single
image. The image is represented as a vector of 512 float numbers. There is also a JSON
payload attached to each point, which looks similar to this:
```
json
{
    "cafe": {
        "address": "VGX7+6R2 Vecchia Napoli, Valletta",
        "categories": ["italian", "pasta", "pizza", "burgers", "mediterranean"],
        "location": {"lat": 35.8980154, "lon": 14.5145106},
        "menu_id": "610936a4ee8ea7a56f4a372a",
        "name": "Vecchia Napoli Is-Suq Tal-Belt",
        "rating": 9,
        "slug": "vecchia-napoli-skyparks-suq-tal-belt"
    },
    "description": "Tomato sauce, mozzarella fior di latte, crispy guanciale, Pecorino Romano cheese and a hint of chilli",
    "image": "the linked resource
    "name": "L'Amatriciana"
}
```
The embeddings generated with clip-ViT-B-32 model have been generated using the following
code snippet:
```
python
from PIL import Image
from sentence_transformers import SentenceTransformer
image_path = "5dbfd216-5cce-11eb-8122-de94874ad1c8_ns_takeaway_seelachs_ei_baguette.jpeg"
model = SentenceTransformer("clip-ViT-B-32")
embedding = model.encode(Image.open(image_path))
```
The snapshot of the dataset might be downloaded here.
#### Importing the dataset
The easiest way to use the provided dataset is to recover it via the API by passing the
URL as a location. It works also in Qdrant Cloud. The following
code snippet shows how to create a new collection and fill it with the snapshot data:
```
http request
PUT /collections/{collection_name}/snapshots/recover
{
  "location": "the linked resource
}
```
