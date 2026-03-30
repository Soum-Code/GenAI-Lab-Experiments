# Generative AI Lab Experiments (LLM 2nd Sem)

This repository serves as a comprehensive collection of practical experiments for students and developers specializing in Large Language Models (LLM). It demonstrates the end-to-end lifecycle of Generative AI applications, from basic parameter tuning to complex retrieval systems and fine-tuning simulations.

## Project Overview

The objective of this project is to provide a hands-on learning environment for:
- **Prompt Engineering**: Understanding Zero-shot, Few-shot, and CoT strategies.
- **RAG Systems**: Building retrieval-augmented pipelines with semantic search.
- **Evaluation**: Implementing automated metrics and the RAG Triad.
- **Data Engineering**: Handling unstructured clinical data and structured Excel outputs.
- **Fine-Tuning**: Logic and simulations for instruction alignment.

## Technology Stack

- **Core**: Python 3.x
- **LLM Engine**: Google Gemini API (1.5 Flash / Pro)
- **Vector Search**: Google `embedding-001` with Cosine Similarity
- **Data Handling**: `NumPy` (vectors), `openpyxl` (Excel), `PyMuPDF` (PDF parsing)
- **Evaluation**: RAG Triad frameworks and LLM-as-a-judge patterns.

## Repository Structure

The project is organized into self-contained Python scripts within the `GenAI_Lab_Experiments/` directory.

## Project Workflow

The experiments are designed to be executed in a logical sequence to simulate a complete AI development cycle:

1.  **Foundations (Exp 1, 11, 12):** Learning to control the LLM's output through parameters and advanced prompting (Zero-shot, Few-shot, CoT).
2.  **Information Retrieval (Exp 3, 4, 5):** Parsing unstructured data (Medical Reports) and comparing Keyword vs. Semantic search.
3.  **Data Generation (Exp 6, 13):** Building question banks and preparing data for fine-tuning.
4.  **Advanced Systems (Exp 7, 8):** Finalizing an end-to-end RAG pipeline and evaluating it using the RAG Triad.
5.  **Quality Control (Exp 2):** Automating the evaluation of the generated responses.

## Experiment Descriptions & Student Learning Outcomes (SLO)

### Experiment 1: LLM Parameters Comparison
- **Description:** Investigates how `temperature`, `top_p`, and `max_output_tokens` influence model responses.
- **SLO:** Demonstrate understanding of stochastic vs. deterministic generation and the trade-off between creativity and consistency.

### Experiment 2: Automated Evaluation Metrics
- **Description:** Uses LLM-as-a-judge to score responses based on toxicity, bias, fluency, and accuracy.
- **SLO:** Implement structured evaluation pipelines and automated quality assurance for AI outputs.

### Experiment 3: Keyword-Based Search
- **Description:** Implements traditional keyword search mechanisms.
- **SLO:** Understand the limitations of lexical matching in comparison to semantic understanding.

### Experiment 4: Semantic Embedding Search
- **Description:** Uses `gemini-embedding-001` to perform vector-based similarity searches.
- **SLO:** Learn to represent text as high-dimensional vectors and perform semantic retrieval using cosine similarity.

### Experiment 5: Medical Report Reader
- **Description:** Parses clinical PDFs and text reports to extract structured patient data.
- **SLO:** Apply LLMs for domain-specific Document AI and clinical information extraction.

### Experiment 6: Question Bank Generator (Excel)
- **Description:** Generates synthetic question-answer pairs and saves them to an Excel file using `openpyxl`.
- **SLO:** Automate dataset creation and manage structured data exports for ML training.

### Experiment 7: End-to-End RAG Pipeline
- **Description:** Integrates document chunking, embedding generation, and retrieval-based answering.
- **SLO:** Construct a functional Retrieval-Augmented Generation system from scratch.

### Experiment 8: RAG Triad Evaluation
- **Description:** Evaluates RAG performance using the "Triad" (Answer Relevance, Context Precision, and Faithfulness).
- **SLO:** Mastering the evaluation of retrieval quality and model hallucination in RAG systems.

### Experiment 11: Prompting Strategies (Zero/Few-Shot)
- **Description:** Compares performance between Zero-shot and Few-shot prompting techniques.
- **SLO:** Design effective prompts and understand the impact of contextual examples on model performance.

### Experiment 12: Chain-of-Thought (CoT) Prompting
- **Description:** Implements reasoning steps to improve performance on complex logic tasks.
- **SLO:** Apply advanced prompting techniques to elicit structured reasoning from LLMs.

### Experiment 13: Instruction Fine-Tuning Simulation
- **Description:** Demonstrates the process of preparing data and simulating fine-tuning for specific instruction sets.
- **SLO:** Understand the lifecycle of supervised fine-tuning (SFT) and instruction alignment.

## Getting Started

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Soum-Code/GenAI-Lab-Experiments.git
    cd GenAI-Lab-Experiments
    ```

2.  **Install Dependencies:**
    ```bash
    pip install google-generativeai openpyxl numpy pymupdf
    ```

3.  **Configure API Key:**
    Replace `YOUR_GEMINI_API_KEY` in the scripts with your actual Gemini API Key.

4.  **Run Experiments:**
    ```bash
    python GenAI_Lab_Experiments/exp1_llm_parameters.py
    ```

## License
MIT License
