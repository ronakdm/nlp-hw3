import torch
import pickle

# Read in data and form into a FloatTensor that is useful for an embedding layer.

filename = "data/glove.6B.50d.txt"
embed_dim = 50

try:
    with open(filename) as f:
        lines = f.readlines()
except FileNotFoundError:
    print(
        """Word embedding file '%s' not found. 
        Please download the file from 'https://nlp.stanford.edu/projects/glove/)'."""
    )
    quit()

vocab_size = len(lines)

print("Vocabulary size:", vocab_size)

embeddings = torch.zeros([vocab_size, embed_dim], dtype=torch.float)
vocab = {}

for word_num, line in enumerate(lines):
    arr = line.split()

    word = arr[0]
    vocab[word] = word_num

    for dim in range(embed_dim):
        embeddings[word_num, dim] = float(arr[dim + 1])

pickle.dump(vocab, open("vocab.p", "wb"))
pickle.dump(embeddings, open("embeddings.p", "wb"))

