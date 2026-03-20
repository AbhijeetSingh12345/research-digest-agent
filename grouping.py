
# from sklearn.cluster import AgglomerativeClustering
# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer('all-MiniLM-L6-v2')

# def group_claims(claims):
#     # ✅ FIX 1: handle empty or single claim
#     if not claims:
#         return []
    
#     if len(claims) == 1:
#         return [claims]   # single group

#     embeddings = model.encode([c["claim"] for c in claims])

#     clustering = AgglomerativeClustering(
#         n_clusters=None,
#         distance_threshold=1.2
#     )

#     labels = clustering.fit_predict(embeddings)

#     groups = {}
#     for i, label in enumerate(labels):
#         groups.setdefault(label, []).append(claims[i])

#     return list(groups.values())



from sentence_transformers import SentenceTransformer
from sklearn.cluster import AgglomerativeClustering

model = SentenceTransformer('all-MiniLM-L6-v2')

def group_claims(claims):
    if not claims:
        return []

    texts = [c["claim"] for c in claims]
    embeddings = model.encode(texts)

    clustering = AgglomerativeClustering(
        n_clusters=None,
        distance_threshold=1.2
    )

    labels = clustering.fit_predict(embeddings)

    groups = {}
    for i, label in enumerate(labels):
        groups.setdefault(label, []).append(claims[i])

    return list(groups.values())