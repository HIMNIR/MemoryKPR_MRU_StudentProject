## MEMORY KPR PROJECT

---

### Introduction
This project is focused on the development and deployment of machine learning models designed to perform two main tasks: 
  1. Comparing the semantic similarity between image labels obtained via a CNN from an Amazon Web Service backend, and user inputs including smart story descriptions
  2. Utilizing a pre-trained model fine-tuned on a large Not Safe For Work (NSFW) media dataset to identify and filter out inappropriate images. Below is an overview of each section of the project.

### Semantic Similarity Assessment

#### Overview

In the first part of our project, we aim to evaluate the relevance of images based on their content in relation to user-provided text inputs, such as descriptions or storylines. This is achieved through a process involving image analysis via a CNN, text vectorization, and similarity scoring.

#### Process

**Image Labeling**: Images are processed using a CNN model hosted on AWS, which generates a set of descriptive labels for each image.

**Text Vectorization**: User inputs, including direct text descriptions and smart story narratives, are vectorized into a format that can be numerically analyzed. This involves transforming the text into a series of vectors that represent the semantic meaning of the words in a high-dimensional space.

**Embedding Layer Creation**: An embedding layer is then created for both the image labels and the vectorized text inputs. This layer serves as the foundation for comparing the semantic content of the images and text.

**Cosine Similarity Calculation**: We compute the cosine similarity between the embeddings of the image labels and the text inputs. This metric quantifies the similarity of the vectors, with a higher score indicating greater similarity.
    Threshold Application: Outputs that achieve a cosine similarity score above a predetermined threshold are classified as having a significant level of similarity. This threshold can be adjusted based on the desired sensitivity of the model.

### Inappropriate Content Filtering

#### Overview

The second section of the project leverages a pre-trained model that has been fine-tuned on a comprehensive dataset of NSFW content. The purpose of this model is to identify and filter out images that are deemed inappropriate for the application, ensuring a safe and user-friendly environment.

#### Process

**Pre-trained Model Selection**: Selected a model known for its effectiveness in image recognition tasks is chosen as the base. pyTorch is easy to work with and the default proved to be sufficient for our dataset, as it achieved an average of 81% accuracy and as high as 85 in some epochs. 

**Fine-tuning**: This model is then fine-tuned using a large dataset specifically compiled to include a wide range of NSFW media. This process adapts the model to be highly sensitive to the nuances of inappropriate content.

**Content Filtering**: Images processed through the model are evaluated for their appropriateness. Those identified as containing NSFW elements are labeled as such. Non NSFW images can be labeled as drawing or neutral. 

### Link to NSFW Filter Model

This is a shared Google Drive as the file itself was too large to upload here. I would recommend downloading this file as soon as possible. If there are errors loading the model, you might as well run the whole script again and create a new one. Depending on your computer, it should take around 2 hours to train the whole thing.  https://drive.google.com/file/d/1324bgKDehoZ_f8qm7uUP2weQqHCWwjHG/view?usp=sharing 
