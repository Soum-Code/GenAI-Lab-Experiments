import google.generativeai as genai
import os

# --- CONFIGURATION ---
API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=API_KEY)

MODEL_NAME = "gemini-1.5-flash"

def query_gemini(prompt):
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

def run_experiment_12():
    print("="*60)
    print("EXPERIMENT 12: CHAIN-OF-THOUGHT (CoT) PROMPTING")
    print("="*60)

    # 1. Math Word Problem
    math_q = "If I have 10 apples and eat 2, then buy 5 more, and give half to my friend, how many do I have?"
    
    # 2. Logical Reasoning
    logic_q = "Sally has 3 brothers. Each brother has 2 sisters. How many sisters does Sally have?"

    problems = [
        ("MATH PROBLEM", math_q),
        ("LOGIC PROBLEM", logic_q)
    ]

    for title, q in problems:
        print(f"\n--- {title} ---")
        
        # Normal Prompting
        print(f"\n[NORMAL PROMPTING]")
        print(f"Prompt: {q}")
        normal_resp = query_gemini(q)
        print(f"Response: {normal_resp}")

        # CoT Prompting
        print(f"\n[CHAIN-OF-THOUGHT PROMPTING]")
        cot_prompt = q + " Think step by step and explain your reasoning."
        print(f"Prompt: {cot_prompt}")
        cot_resp = query_gemini(cot_prompt)
        print(f"Response: {cot_resp}")

    print("\nCOMPARISON:")
    print("Normal prompting often gives a direct answer but can fail on complex multistep logic.")
    print("Chain-of-Thought (CoT) forces the model to decompose the problem into smaller, logical steps.")
    print("CoT significantly improves accuracy and provides transparency into the model's reasoning process.")

if __name__ == "__main__":
    run_experiment_12()
