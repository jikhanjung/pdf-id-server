# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from sentence_transformers import SentenceTransformer
import torch

app = FastAPI()

device = "cuda" if torch.cuda.is_available() else "cpu"
model = SentenceTransformer("/app/models/bge-m3-local")
model.to(device)

class EmbedRequest(BaseModel):
    text: str

class BatchEmbedRequest(BaseModel):
    texts: List[str]

@app.post("/embed")
def embed(req: EmbedRequest):
    vec = model.encode(req.text, normalize_embeddings=True, device=device)
    return {"embedding": vec.tolist()}

@app.post("/embed_batch")
def embed_batch(req: BatchEmbedRequest):
    vecs = model.encode(req.texts, normalize_embeddings=True, device=device)
    return {"embeddings": [vec.tolist() for vec in vecs]}