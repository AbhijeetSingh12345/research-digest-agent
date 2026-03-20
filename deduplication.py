from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def deduplicate(claims, threshold=0.8):
    unique = []
    embeddings = model.encode([c["claim"] for c in claims])

    for i, emb in enumerate(embeddings):
        is_duplicate = False

        for u in unique:
            sim = cosine_similarity(
                [emb],
                [model.encode(u["claim"])]
            )[0][0]

            if sim > threshold:
                is_duplicate = True
                break

        if not is_duplicate:
            unique.append(claims[i])

    return unique