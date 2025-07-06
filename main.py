import numpy as np
import nltk
import os
from sklearn.preprocessing import OneHotEncoder
from nltk.tokenize import TreebankWordTokenizer
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity

sentences = [
    "the king rules the land",
    "the queen protects the realm",
    "men and women live peacefully"
]

tokenizer = TreebankWordTokenizer()
tokens = sorted(list(set(tokenizer.tokenize(" ".join(sentences)))))
print("Vocabulary:", tokens)

encoder = OneHotEncoder(sparse_output=False)
onehot = encoder.fit_transform(np.array(tokens).reshape(-1, 1))

print("\nOne-Hot Vectors (Sparse):")
for word, vec in zip(tokens, onehot):
    print(f"{word}: {vec}")


def load_glove_embeddings(path):
    print("\nLoading GloVe Embeddings...")
    glove_dict = {}
    with open(path, "r", encoding="utf8") as file:
        for line in file:
            parts = line.strip().split()
            word = parts[0]
            vec = np.array(parts[1:], dtype=np.float32)
            glove_dict[word] = vec
    return glove_dict

glove_path = "glove.6B.100d.txt" 
glove = load_glove_embeddings(glove_path)

words_to_check = ["king", "queen", "men", "women", "realm"]

print("\nDense Vectors (GloVe):")
for word in words_to_check:
    if word in glove:
        print(f"{word}: {glove[word][:8]}...")  
    else:
        print(f"{word} not found in GloVe.")


print("\nGloVe Cosine Similarity Matrix:")
vectors = [glove[word] for word in words_to_check if word in glove]
labels = [word for word in words_to_check if word in glove]
similarity = cosine_similarity(vectors)

sns.heatmap(similarity, xticklabels=labels, yticklabels=labels, annot=True, cmap='coolwarm')
plt.title("Cosine Similarity (GloVe Embeddings)")
plt.tight_layout()
plt.show()
