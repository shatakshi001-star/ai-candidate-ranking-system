from src.load_data import load_candidates
from src.text_builder import candidate_to_text
from src.embedding import model
from src.faiss_index import build_index
import faiss
from docx import Document
import numpy as np

print("Loading candidates...")


candidates = load_candidates(
    "data/candidates.jsonl"
)

print(f"Total Candidates: {len(candidates)}")


candidate = candidates[0]

print("\nCandidate Keys:")
print(candidate.keys())


print("\nCandidate Text Preview:")
print(candidate_to_text(candidate)[:500])


print("\nCreating candidate texts...")

candidate_texts = [
    candidate_to_text(c)
    for c in candidates
]


print("\nGenerating candidate embeddings...")

candidate_vectors = model.encode(
    candidate_texts,
    batch_size=32,
    show_progress_bar=True
)


np.save(
    "models/candidate_vectors.npy",
    candidate_vectors
)

print("Candidate embeddings saved!")


print("\nReading Job Description...")

doc = Document(
    "data/job_description.docx"
)

job_description = "\n".join(
    paragraph.text
    for paragraph in doc.paragraphs
)

print("\nJob Description:")
print(job_description)


print("\nGenerating Job Embedding...")

job_vector = model.encode(
    [job_description]
)

print("Job Vector Shape:")
print(job_vector.shape)

print("\nSUCCESS!")
print("\nBuilding FAISS Index...")

index = build_index(
    candidate_vectors
)

job_vector = np.array(
    job_vector,
    dtype="float32"
)

faiss.normalize_L2(
    job_vector
)

print("Searching Candidates...")

scores, ids = index.search(
    job_vector,
    1000
)

print("\nTop Matching Candidates:")

for rank, idx in enumerate(ids[0], start=1):

    candidate_id = candidates[idx]["candidate_id"]

    print(
        f"Rank {rank} -> Candidate ID {candidate_id}"
    )

    import pandas as pd

submission = []

for rank, (idx, score) in enumerate(
    zip(ids[0], scores[0]),
    start=1
):

    candidate = candidates[idx]

    candidate_id = candidate["candidate_id"]

    reasoning = (
        f"Semantic match score {score:.3f}"
    )

    submission.append({
        "candidate_id": candidate_id,
        "rank": rank,
        "score": round(float(score), 3),
        "reasoning": reasoning
    })

submission_df = pd.DataFrame(submission)

submission_df.to_csv(
    "output/submission.csv",
    index=False
)

print("Submission file created!")