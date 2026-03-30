import google.generativeai as genai
import os

# --- CONFIGURATION ---
API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=API_KEY)

# Default parameters
TEMPERATURE = 0.7
TOP_P = 0.9
MAX_TOKENS = 150

def run_experiment_1():
    print("="*60)
    print("EXPERIMENT 1: LLM PARAMETERS (TEMPERATURE COMPARISON)")
    print("="*60)

    model_name = "gemini-1.5-flash"
    query = "Write a one-sentence creative story about a robot discoverning a flower."
    
    temperatures = [0.0, 0.7, 1.2]
    responses = []

    print(f"Query: {query}\n")
    print("Running queries with different temperatures...")

    for temp in temperatures:
        try:
            # Set up generation config
            config = genai.GenerationConfig(
                temperature=temp,
                top_p=TOP__P, # Using the default or top-level variable
                max_output_tokens=MAX_TOKENS
            )
            
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(query, generation_config=config)
            responses.append((temp, response.text.strip()))
        except Exception as e:
            responses.append((temp, f"Error: {str(e)}"))

    # Print results side by side (formatted)
    print("\n" + "-"*100)
    print(f"{'Temp':<10} | {'Response'}")
    print("-"*100)
    for temp, text in responses:
        print(f"{temp:<10} | {text}")
    print("-"*100)

    print("\nOBSERVATION:")
    print("Low temperature (e.g., 0.0) makes the model more deterministic, meaning it chooses the most likely next word.")
    print("This results in focused and consistent output. High temperature (e.g., 1.2) increases randomness,")
    print("allowing for more creative, diverse, but sometimes less coherent results.")

if __name__ == "__main__":
    run_experiment_1()
