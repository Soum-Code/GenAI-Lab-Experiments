import google.generativeai as genai
import os

# --- CONFIGURATION ---
API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=API_KEY)

MODEL_NAME = "gemini-1.5-flash"

def query_gemini(prompt):
    """Simple wrapper for Gemini generation."""
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

def run_experiment_11():
    print("="*60)
    print("EXPERIMENT 11: PROMPTING STRATEGIES (ZERO/ONE/FEW SHOT)")
    print("="*60)

    # 1. Factual Question: Classification
    factual_q = "Classify the sentiment of this text: 'The movie was amazing!'"
    
    # 2. Reasoning Question: Mathematics/Logic
    reasoning_q = "If each apple costs $2 and I buy 5 apples and 2 oranges ($3 each), how much do I spend?"

    strategies = {
        "Zero-shot": "",
        "One-shot": "Example: 'I love this pizza!' -> Positive\n\n",
        "Few-shot": "Example 1: 'I love this pizza!' -> Positive\nExample 2: 'The food was cold.' -> Negative\nExample 3: 'It was okay.' -> Neutral\n\n"
    }

    # Execute Factual Question
    print("\n--- FACTUAL QUESTION (SENTIMENT) ---")
    for name, prefix in strategies.items():
        print(f"\n[{name}]")
        print(f"Prompt: {prefix}{factual_q}")
        response = query_gemini(prefix + factual_q)
        print(f"Response: {response}")

    # Execute Reasoning Question (Updating few-shot examples for reasoning)
    print("\n--- REASONING QUESTION ---")
    reasoning_strategies = {
        "Zero-shot": "",
        "One-shot": "Example: If 1 pen is $5, 2 pens are $10. Question: ",
        "Few-shot": "Example 1: 1 pen costs $5, so 3 pens cost $15.\nExample 2: 1 map costs $10, so 2 maps cost $20.\nExample 3: 1 book costs $20, so 3 books cost $60.\nQuestion: "
    }
    
    for name, prefix in reasoning_strategies.items():
        print(f"\n[{name}]")
        print(f"Prompt: {prefix}{reasoning_q}")
        response = query_gemini(prefix + reasoning_q)
        print(f"Response: {response}")

    print("\nOBSERVED DIFFERENCES:")
    print("1. Zero-shot relies entirely on pre-trained knowledge and can sometimes be generic.")
    print("2. One-shot provides a single format example, improving formatting consistency.")
    print("3. Few-shot drastically improves performance on complex tasks by establishing clear patterns.")

if __name__ == "__main__":
    run_experiment_11()
