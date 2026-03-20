# Research Digest Agent

research-digest-agent/
│
├── main.py
├── ingestion.py
├── extraction.py
├── deduplication.py
├── grouping.py
├── output.py
├── utils.py
│
├── tests/
│   ├── test_empty.py
│   ├── test_dedup.py
│   ├── test_conflict.py
│
├── sample_inputs/
│   └── urls.txt
│
├── outputs/
│   ├── digest.md
│   └── sources.json
│
├── requirements.txt
└── README.md

## Overview

This project implements an autonomous research digest agent that:
- Ingests multiple sources (URLs)
- Extracts key claims with evidence
- Removes redundant information
- Groups related insights
- Produces a structured research brief

---

## How the Agent Works (Step-by-Step)

### 1. Content Ingestion
- Reads a list of URLs from `urls.txt`
- Fetches webpage content using `requests`
- Parses HTML using `BeautifulSoup`
- Cleans text and stores metadata (source, length)

---

### 2. Claim Extraction
- Splits text into sentences
- Applies heuristic filtering to extract meaningful claims
- Filters:
  - Removes short or incomplete sentences
  - Removes UI artifacts (e.g., "Toggle", "subsection")
  - Removes broken phrases (e.g., "dealing with", "from a")
- Each claim is paired with its supporting evidence (same sentence)

---

### 3. Deduplication
- Uses sentence embeddings (`sentence-transformers`)
- Computes cosine similarity between claims
- Removes semantically similar (duplicate) claims

---

### 4. Grouping
- Converts claims into embeddings
- Uses Agglomerative Clustering to group similar claims
- Groups represent common themes across sources

---

### 5. Structured Digest Generation
- Generates:
  - `sources.json` → claims per source
  - `digest.md` → grouped insights
- Adds semantic theme labels (e.g., "Machine Learning", "Computer Vision")

---

## How Claims Are Grounded

Each claim:
- Is directly extracted from source text
- Includes an exact supporting snippet (evidence)
- No external knowledge or hallucination is used

---

## Deduplication & Grouping Strategy

### Deduplication
- Embedding-based similarity comparison
- Threshold-based filtering to remove repeated ideas

### Grouping
- Hierarchical clustering on embeddings
- Groups similar claims into themes
- Themes are labeled using keyword-based semantic mapping

---

## Required Behaviors Handling

- Empty / failed sources → safely skipped
- Duplicate sources → handled via deduplication
- Conflicting claims → preserved (no merging)
- No hallucination → only source-based extraction

---

## Tests Implemented

1. Empty / unreachable source handling  
2. Deduplication of similar claims  
3. Preservation of conflicting claims  

---

## Limitation

The system uses heuristic-based claim extraction, which may:
- Miss nuanced or implicit insights
- Occasionally include partially incomplete sentences

---

## Improvement (With More Time)

- Use LLM-based extraction for higher-quality claims
- Improve theme labeling using semantic summarization
- Add confidence scores per claim
- Implement caching to avoid reprocessing sources

---

## Run Instructions

```bash
pip install -r requirements.txt
python main.py
