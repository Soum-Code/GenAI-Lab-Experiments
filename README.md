# RAG Systems and Prompt Engineering — Practical Implementations

A collection of 11 end-to-end implementations covering RAG pipelines, semantic search, prompt engineering, and model evaluation using the Google Gemini API.

---

## What this covers

- **RAG Pipeline** — Full retrieval-augmented generation using Gemini embeddings and cosine similarity
- **RAG Triad Evaluation** — Faithfulness, relevance, and context precision scoring to measure and reduce hallucinations
- **Semantic vs Keyword Search** — BM25 keyword retrieval compared against vector embedding search
- **Prompt Engineering** — Zero-shot, few-shot, and Chain-of-Thought comparisons with quantified output differences
- **Clinical Document Parsing** — Extracting structured data from medical PDF reports using PyMuPDF
- **Synthetic Dataset Generation** — Automated Q&A bank creation exported to Excel using openpyxl
- **LLM Parameter Analysis** — Temperature and top_p comparisons for stochastic vs deterministic output

---

## RAG pipeline architecture

```
Unstructured Data (PDF/TXT)
        |
   Text Chunking
        |
 Gemini Embedding-001
        |
  In-Memory Vector Store
        |
   User Query --> Query Embedding --> Cosine Similarity Search
                                              |
                                     Top-K Context Retrieval
                                              |
                                   Prompt: Context + Query
                                              |
                                    Gemini 1.5 Pro / Flash
                                              |
                                    Final Answer + RAG Triad Score
```

---

## Tech stack

Python · Google Generative AI (Gemini SDK) · PyMuPDF · NumPy · openpyxl

---

## Setup

```bash
git clone https://github.com/Soum-Code/GenAI-Lab-Experiments.git
cd GenAI-Lab-Experiments
pip install -r requirements.txt
```

Replace the API key placeholder in each script:

```python
API_KEY = "your_gemini_api_key_here"
```

Get a free Gemini API key at [aistudio.google.com](https://aistudio.google.com).

---

## Implementations

| # | Focus | What it builds |
|---|---|---|
| 1 | LLM Parameters | Temperature and top_p comparison across generation tasks |
| 2 | QA Metrics | Automated toxicity, bias, and fluency scoring |
| 3 | Lexical Search | BM25 keyword retrieval and its limitations |
| 4 | Semantic Search | Vector embeddings with cosine similarity retrieval |
| 5 | Document AI | Clinical PDF parsing and structured data extraction |
| 6 | Dataset Generation | Synthetic Q&A export to Excel |
| 7 | RAG Pipeline | End-to-end documentation retrieval and answering |
| 8 | RAG Triad | Faithfulness, relevance, and context precision evaluation |
| 11 | Prompt Strategy | Zero-shot vs few-shot performance comparison |
| 12 | Chain-of-Thought | Reasoning path elicitation for logic tasks |
| 13 | Fine-Tuning Prep | Supervised fine-tuning data preparation logic |

---

## License

MIT
