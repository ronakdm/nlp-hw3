# nlp-hw3

This repo contains code for A3 of Natural Language Processing. The assignment is to fit explore GloVe word embeddings for information retrieval, analogy completion, and pretraining for downstream sentiment classification.

## System Requirements

Both the `A3_word_embed.ipynb` notebook and the `A3_sentiment_classification.ipynb` notebooks should be run in a  Google Colab environment (with the second one GPU-accelerated), which contains its dependencies.

## Data

The preprocessing code in `preprocess.py` assumes a folder `data/` containing the files `glove.6B.50d.txt`, that is the 50-dimension GloVe word embeddings trained the Wikipedia 2014 and Gigaword 5 datasets. This file is not included in the repo, and can be downloaded [here](https://nlp.stanford.edu/projects/glove/). That being said, preprocessed data already exists in a git repo as `embeddings.p`, `vocab.p`, and `vocab_list.p`, and are downloaded in the notebooks.  

The `A3_sentiment_classification.ipynb` also requires the [IMDB Large Movie Review Dataset](http://ai.stanford.edu/~amaas/data/sentiment/), which is downloaded in the notebook.

## Instructions

Run either of the notebooks from start to finish to see both examples. A full write-up of the results can be found in `writeup.pdf`. **Note:** `A3_sentiment_classification.ipynb` relies heavily on a [sentiment classification example](https://colab.research.google.com/drive/14GAMb7c6FbDnhWvqcliCZ8KYNvqdnQz7?usp=sharing#scrollTo=uofVxyhMbVtx) given by the TA's, and is by no means my sole work.