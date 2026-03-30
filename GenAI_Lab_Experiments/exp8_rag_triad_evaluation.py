import google.generativeai as genai
import json
import os

# --- CONFIGURATION ---
API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=API_KEY)

MODEL_NAME = "gemini-1.5-flash"

def evaluate_rag_triad(question, context, answer):
    """Evaluate a RAG response based on the RAG Triad metrics."""
    prompt = f"""
    Evaluate the following RAG system performance based on the RAG Triad:
    
    Metrics:
    1. Context Relevance: How relevant is the context to the question? (Score 0.0 to 1.0)
    2. Groundedness: Is the answer derived solely from the provided context? (Score 0.0 to 1.0)
    3. Answer Relevance: Does the answer correctly and fully address the question? (Score 0.0 to 1.0)
    
    Return results EXCLUSIVELY as a JSON object with keys: 
    'context_relevance', 'groundedness', 'answer_relevance'.
    
    Question: "{question}"
    Context: "{context}"
    Answer: "{answer}"
    """
    
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        evaluation = model.generate_content(prompt)
        # Clean JSON from model output
        json_str = evaluation.text.replace('```json', '').replace('```', '').strip()
        return json.loads(json_str)
    except Exception as e:
        print(f"Error during triad evaluation: {e}")
        return None

def run_experiment_8():
    print("="*60)
    print("EXPERIMENT 8: RAG TRIAD EVALUATION")
    print("="*60)

    # Sample RAG Triad Test Case
    test_cases = [
        {
            "q": "What is the capital of France?",
            "c": "Paris is the capital of France. It is famous for the Eiffel Tower.",
            "a": "The capital of France is Paris."
        },
        {
            "q": "What is the hemoglobin level?",
            "c": "Patient Name: John Doe. Report Type: Blood Test. Potassium level is 4.5.",
            "a": "The hemoglobin level is normal." # Hallucination (low groundedness)
        }
    ]

    print(f"{'Question Snippet':<30} | {'C-Rel':<6} | {'Gnd':<5} | {'A-Rel'}")
    print("-" * 65)

    for case in test_cases:
        scores = evaluate_rag_triad(case['q'], case['c'], case['a'])
        if scores:
            q_snippet = (case['q'][:27] + '...') if len(case['q']) > 30 else case['q'].ljust(30)
            print(f"{q_snippet:<30} | {scores.get('context_relevance', 0):<6} | {scores.get('groundedness', 0):<5} | {scores.get('answer_relevance', 0)}")
        else:
            print(f"{case['q'][:27]:<30} | Error")

    print("\nEXPLANATION:")
    print("1. Context Relevance: Measures if the retrieved documents contain the answer.")
    print("2. Groundedness: Ensures the model doesn't hallucinate (answer MUST be in context).")
    print("3. Answer Relevance: Ensures the generated answer addresses the user's need.")
    print("\nCRITICAL FACTOR:")
    print("Context Quality is the most critical factor. If the context is poor, even the most")
    print("advanced LLM cannot produce a grounded and relevant answer.")

if __name__ == "__main__":
    run_experiment_8()
