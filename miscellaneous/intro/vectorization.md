<!-- Vectorization is the process of converting data, such as text or images, into numerical vectors that can be used as input to a machine learning model. Here are five examples of vectorization in Python, with accompanying code:
Here are five examples of vectorization in Python, with accompanying code: -->

One-hot encoding:

```python
from sklearn.preprocessing import OneHotEncoder

# Initialize the OneHotEncoder
encoder = OneHotEncoder()

# Encode the categorical data ['dog', 'cat', 'bird']
one_hot = encoder.fit_transform([['dog'], ['cat'], ['bird']])

# The resulting one-hot encoded array has shape (3, 3)
# and contains the vectors [1, 0, 0], [0, 1, 0], and [0, 0, 1]
print(one_hot.shape)
print(one_hot.toarray())
Word embeddings:
```

```python
import numpy as np

# Load a pre-trained word embedding model
word_embeddings = np.load('word_embeddings.npy')

# Look up the embedding for the word 'dog'
dog_embedding = word_embeddings['dog']

print(dog_embedding)
Image feature extraction:
```

```python
from sklearn.feature_extraction import image

# Extract features from an image using the pixel values
image_data = image.img_to_array(image)

# Extract features using edge detection
edges = image.sobel_h(image)

print(image_data.shape)
print(edges.shape)
Text tokenization:
```

```python
from nltk.tokenize import word_tokenize

# Tokenize a sentence into individual words
sentence = "The quick brown fox jumps over the lazy dog."
tokens = word_tokenize(sentence)

print(tokens)
Numerical data:
```

```python
import numpy as np

# Vectorize a list of numerical data
data = [1, 2, 3, 4, 5]
data_vector = np.array(data)

print(data_vector)
```