import os
import glob
import fitz
import openpyxl
import numpy as np
import google.generativeai as genai

# --- CONFIGURATION ---
API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=API_KEY)

GEN_MODEL = "gemini-1.5-flash"
EMBED_MODEL = "models/embedding-001"

# --- HELPER FUNCTIONS ---
def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def get_text_from_file(filepath):
    """Load text from TXT or PDF."""
    if filepath.lower().endswith(".pdf"):
        doc = fitz.open(filepath)
        return "".join([page.get_text() for page in doc])
    elif filepath.lower().endswith(".txt"):
        with open(filepath, "r") as f:
            return f.read()
    return ""

def load_questions(excel_path):
    """Load questions from the Excel file created in Exp 6."""
    try:
        wb = openpyxl.load_workbook(excel_path)
        sheet = wb.active
        questions = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if row[1]: questions.append(row[1])
        return questions
    except Exception as e:
        print(f"Error loading Excel: {e}")
        return []

def run_experiment_7():
    print("="*60)
    print("EXPERIMENT 7: RAG PIPELINE (RETRIEVAL-AUGMENTED GENERATION)")
    print("="*60)

    # 1. Load medical report files
    folder_path = "./medical_reports"
    if not os.path.exists(folder_path):
        print(f"Directory {folder_path} not found. Please run Exp 5 first.")
        return

    report_files = glob.glob(os.path.join(folder_path, "*"))
    all_chunks = []
    
    print("\nLoading and chunking documents...")
    for f in report_files:
        text = get_text_from_file(f)
        # Simple chunking: by lines/segments
        chunks = [c.strip() for c in text.split("\n") if len(c.strip()) > 10]
        for c in chunks:
            all_chunks.append({"text": c, "source": f})

    if not all_chunks:
        print("No documents found to process.")
        return

    # 2. Generate embeddings for all chunks
    print(f"Generating embeddings for {len(all_chunks)} chunks...")
    for chunk in all_chunks:
        embedding = genai.embed_content(model=EMBED_MODEL, content=chunk["text"])
        chunk["embedding"] = embedding["embedding"]

    # 3. Load questions from Excel
    excel_path = "question_bank.xlsx"
    if not os.path.exists(excel_path):
        print(f"Excel file {excel_path} not found. Please run Exp 6 first.")
        return
    questions = load_questions(excel_path)

    # 4. For each question, retrieve and generate
    print("\nStarting RAG processing...")
    for i, question in enumerate(questions[:3]): # Demonstrate with first 3 questions
        print(f"\n[Question {i+1}]: {question}")
        
        # Embed question
        q_embed = genai.embed_content(model=EMBED_MODEL, content=question)["embedding"]
        
        # Calculate similarity and find top 2
        similarities = []
        for chunk in all_chunks:
            sim = cosine_similarity(q_embed, chunk["embedding"])
            similarities.append((chunk["text"], sim))
        
        similarities.sort(key=lambda x: x[1], reverse=True)
        top_chunks = similarities[:2]
        
        # Combine context
        context = "\n".join([tc[0] for tc in top_chunks])
        
        # Generate answer using Gemini
        prompt = f"Using ONLY the following context, answer the question.\n\nContext:\n{context}\n\nQuestion: {question}"
        try:
            model = genai.GenerativeModel(GEN_MODEL)
            response = model.generate_content(prompt)
            print(f"Answer: {response.text.strip()}")
        except Exception as e:
            print(f"Error generating answer: {e}")

if __name__ == "__main__":
    run_experiment_7()
