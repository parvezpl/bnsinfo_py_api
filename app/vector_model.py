import os
from sentence_transformers import SentenceTransformer

# Load the model once
model = SentenceTransformer("./models/paraphrase-multilingual-MiniLM-L12-v2")
print(model)

def get_vector(text: str):
    return model.encode(text).tolist()

