# 🔤 Word Embedding Exploration: One-Hot vs GloVe

This NLP mini-project explores how machines understand words using **sparse vs. dense** vector representations. We compare basic **One-Hot Encoding** with powerful pre-trained **GloVe embeddings**, and visualize word similarity using **cosine similarity heatmaps**.

---

## 📌 What’s Inside?

- 🧠 Tokenize and prepare a small vocabulary
- 🔳 Represent words using One-Hot Encoding (sparse vectors)
- 🌐 Load GloVe (100D) embeddings for dense representations
- 📏 Compare word similarities using Cosine Similarity
- 📊 Visualize relationships with Seaborn heatmaps

---

## 🛠️ Technologies Used

- Python 3.10+
- NLTK (tokenization)
- NumPy, Scikit-learn (vectors, similarity)
- Matplotlib & Seaborn (visualizations)
- GloVe 6B Embeddings (100D)

---

## 🚀 Getting Started

### 1. 📥 Clone the Repo

```bash
git clone https://github.com/Aliharis007/Word-Embedding-NLP.git
cd Word-Embedding-NLP
````

### 2. 📦 Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On Mac/Linux
```

### 3. 📦 Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. 📥 Download GloVe Embeddings

You **must manually download** the GloVe vectors from Stanford NLP:
📎 [Download GloVe.6B.zip (822MB)](https://nlp.stanford.edu/data/glove.6B.zip)

Then extract it and place this file in the same folder as your `mean.py`:

```
glove.6B.100d.txt
```

---

## ▶️ Run the Script

```bash
python main.py
```

This will:

* Print your vocabulary
* Show One-Hot vectors
* Load GloVe vectors for selected words
* Compute cosine similarity
* Generate a heatmap

---

## 🧪 Sample Output

### 🔳 One-Hot Vectors

Each word has a unique 1 in its index. No info about meaning.

```
king    → [0, 1, 0, 0, 0, ...]
queen   → [0, 0, 1, 0, 0, ...]
```

### 🌐 GloVe Dense Vectors

GloVe gives us 100D vectors that capture real-world context.

```
king → [-0.2459, 0.2873, ..., 0.5127]
queen → [-0.3924, 0.1532, ..., 0.4183]
```

### 📊 Cosine Similarity Heatmap

| Word 1 | Word 2 | Similarity |
| ------ | ------ | ---------- |
| king   | queen  | 0.75 ✅     |
| men    | women  | 0.86 ✅     |
| king   | women  | 0.28 🔻    |

### 🖼️ Visualization

![Heatmap Output](./glove_similarity_heatmap.png)
*(Make sure to save and upload the screenshot as `glove_similarity_heatmap.png`)*

---

## 📚 Key Concepts Explained

| Concept           | Description                                                   |
| ----------------- | ------------------------------------------------------------- |
| One-Hot Encoding  | Sparse vectors; unique per word, no meaning captured          |
| GloVe Embeddings  | Dense 100D vectors trained on real text (Wikipedia, Gigaword) |
| Cosine Similarity | Measures angle-based similarity between word vectors          |
| Heatmap           | Visualization of similarity values between words              |

---

## 💡 What You’ll Learn

* Why sparse vectors fail to capture semantics
* How pre-trained word vectors like GloVe work
* How to visualize relationships between words
* How `cosine_similarity()` gives actual closeness

---

## 📂 Folder Structure

```
📁 Word-Embedding-NLP/
│
├── mai  n.py                  # Main Python script
├── glove.6B.100d.txt        # GloVe vectors (download manually)
├── glove_similarity_heatmap.png   # Optional output screenshot
├── requirements.txt         # Python dependencies
├── README.md                # This file
```

---

## 🙌 Author

👤 **Ali Haris**
📍 CS Student | Dev Enthusiast | Exploring NLP & AI
🔗 [Connect with me on LinkedIn](https://www.linkedin.com/in/Aliharis007)

---

## ⭐️ If you liked this project

* Star the repo ⭐
* Fork and experiment 💻
* Share your outputs on LinkedIn!
* Feel free to open issues or PRs
