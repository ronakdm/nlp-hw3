# nlp-hw3

This repo contains code for A3 of Natural Language Processing. The assignment is to fit explore GloVe word embeddings for information retrieval, analogy completion, and pretraining for downstream sentiment classification.

## System Requirements

The code runs on Python 3. Running the `A3_word_embed.ipynb` notebook requires `numpy` and `scikit-learn` as external dependencies. The `A3_sentiment_classification.ipynb` should be run in a GPU-accelerated Google Colab environment, which contains its dependencies.

## Data

The preprocessing code in `preprocess.py` assumes a folder `data/` containing the files `glove.6B.50d.txt`, that is the 50-dimension GloVe word embeddings trained the Wikipedia 2014 and Gigaword 5 datasets. This file is not included in the repo, and can be downloaded [here](https://nlp.stanford.edu/projects/glove/). That being said, preprocessed data already exists in the repo as `embeddings.p`, `vocab.p`, and `vocab_list.p`. These embeddings are used to run `A3_word_embed.ipynb`, which performs information retrieval and analogy completion. 

The `A3_sentiment_classification.ipynb` also requires the [IMDB Large Movie Review Dataset](http://ai.stanford.edu/~amaas/data/sentiment/), which is downloaded in the notebook.

## Instructions

Run either of the notebooks from start to finish to see both examples. A full write-up of the results can be found in `writeup.pdf`. **Note:** `A3_sentiment_classification.ipynb` relies heavily on a [sentiment classification example](https://colab.research.google.com/drive/14GAMb7c6FbDnhWvqcliCZ8KYNvqdnQz7?usp=sharing#scrollTo=uofVxyhMbVtx) given by the TA's, and is by no means my sole work.