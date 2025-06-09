# download_model.py
from sentence_transformers import SentenceTransformer

print("Downloading BGE-M3 model...")
model = SentenceTransformer("BAAI/bge-m3")
model.save("../models/bge-m3-local")
print("Model saved to ../models/bge-m3-local")
