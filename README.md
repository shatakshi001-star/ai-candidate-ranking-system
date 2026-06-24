# AI Candidate Ranking System

## Overview

This project builds an AI-powered candidate ranking system that understands job descriptions and ranks candidates semantically instead of relying on keyword matching.

## Features

* Job Description Understanding
* Candidate Profile Processing
* Sentence Transformer Embeddings
* FAISS Similarity Search
* Candidate Ranking
* Submission File Generation

## Tech Stack

* Python
* Sentence Transformers
* FAISS
* NumPy
* Pandas

## Workflow

Job Description
→ Embedding Generation
→ Candidate Embeddings
→ FAISS Retrieval
→ Ranking
→ Submission CSV

## Run

```bash
pip install -r requirements.txt
python main.py
```

## Output

Generated file:

output/submission.csv
