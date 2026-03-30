import re
import os

def create_sample_file(filepath):
    """Automatically creates a sample text file if none exists."""
    content = """GEN AI LAB EXPERIMENT 3
This is a sample document for keyword search.
The topic is Generative Artificial Intelligence (Gen AI).
Large Language Models (LLMs) like Gemini are powerful.
Natural Language Processing (NLP) is a key component.
Machine learning is evolving rapidly.
Gen AI can create text, images, and more.
"""
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Sample file created at: {filepath}")

def keyword_search(filepath, keyword):
    """Search for a keyword in a file using regex and return context."""
    if not os.path.exists(filepath):
        create_sample_file(filepath)
    
    matches = []
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
        
        # Safe escape keyword for regex
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        
        for i, line in enumerate(lines):
            if pattern.search(line):
                # Context: one line above and below if they exist
                context_above = lines[i-1].strip() if i > 0 else ""
                context_below = lines[i+1].strip() if i < len(lines)-1 else ""
                matches.append({
                    "line_num": i + 1,
                    "target": line.strip(),
                    "context_above": context_above,
                    "context_below": context_below
                })
        
        return matches
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def run_experiment_3():
    print("="*60)
    print("EXPERIMENT 3: KEYWORD SEARCH (REGEX & CONTEXT)")
    print("="*60)

    # Inputs from user
    filepath = input("Enter file path (default: 'sample_data.txt'): ") or "sample_data.txt"
    keyword = input("Enter keyword to search for: ") or "Gen AI"

    results = keyword_search(filepath, keyword)

    if results:
        print(f"\nFound {len(results)} match(es) for '{keyword}':")
        for res in results:
            print(f"\n[Line {res['line_num']}]: {res['target']}")
            if res['context_above']:
                print(f"  - Above: {res['context_above']}")
            if res['context_below']:
                print(f"  - Below: {res['context_below']}")
    else:
        print(f"\nNo occurrences of '{keyword}' found in {filepath}.")

if __name__ == "__main__":
    run_experiment_3()
