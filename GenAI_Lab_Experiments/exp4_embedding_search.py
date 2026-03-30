import google.generativeai as genai
import numpy as np
import os

# --- CONFIGURATION ---
API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=API_KEY)

MODEL_NAME = "models/embedding-001"

def cosine_similarity(v1, v2):
    """Compute cosine similarity between two vectors."""
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)

def generate_embeddings(text):
    """Generate embeddings for a single text chunk."""
    try:
        embedding = genai.embed_content(model=MODEL_NAME, content=text)
        return embedding['embedding']
    except Exception as e:
        print(f"Error generating embedding: {e}")
        return None

def run_experiment_4():
    print("="*60)
    print("EXPERIMENT 4: EMBEDDING SEARCH (COSINE SIMILARITY)")
    print("="*60)

    # Input file/query
    filepath = input("Enter file path (default: 'sample_data.txt'): ") or "sample_data.txt"
    query = input("Enter query string: ") or "What is Gen AI?"

    if not os.path.exists(filepath):
        print(f"File not found: {filepath}. Please create it using Exp 3.")
        return

    # Split into paragraphs or sentences
    with open(filepath, 'r') as f:
        chunks = [line.strip() for line in f.readlines() if line.strip()]

    print(f"\nProcessing {len(chunks)} chunks...")
    
    # Generate query embedding
    query_vector = generate_embeddings(query)
    if not query_vector:
        return

    results = []
    for chunk in chunks:
        chunk_vector = generate_embeddings(chunk)
        if chunk_vector:
            similarity = cosine_similarity(query_vector, chunk_vector)
            results.append((chunk, similarity))

    # Sort by similarity descending
    results.sort(key=lambda x: x[1], reverse=True)

    print("\nTop 3 Most Relevant Results:")
    print("-" * 60)
    for i, (chunk, score) in enumerate(results[:3]):
        print(f"{i+1}. [Score: {score:.4f}] {chunk}")
    print("-" * 60)

if __name__ == "__main__":
    run_experiment_4()
