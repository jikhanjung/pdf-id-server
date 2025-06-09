import requests

# 단일 텍스트 임베딩 테스트
text = "Trilobites are extinct marine arthropods..."
res = requests.post("http://localhost:8000/embed", json={"text": text})
vec = res.json()["embedding"]
print(f"[단일] 임베딩 벡터 길이: {len(vec)}, 첫 5개: {vec[:5]}")

# 배치 텍스트 임베딩 테스트
texts = [
    "Trilobites are extinct marine arthropods...",
    "They flourished throughout the Paleozoic era.",
    "The genus Phacops had large compound eyes.",
    "Morphological variation helps distinguish species."
]

res_batch = requests.post("http://localhost:8000/embed_batch", json={"texts": texts})
vecs = res_batch.json()["embeddings"]

print(f"[배치] 임베딩 개수: {len(vecs)}")
for i, v in enumerate(vecs):
    print(f"  - {i+1}번째 벡터 길이: {len(v)}, 첫 5개: {v[:5]}")
