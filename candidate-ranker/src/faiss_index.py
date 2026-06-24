import faiss
import numpy as np

def build_index(vectors):

    vectors = np.array(
        vectors,
        dtype="float32"
    )

    faiss.normalize_L2(vectors)

    index = faiss.IndexFlatIP(
        vectors.shape[1]
    )

    index.add(vectors)

    return index