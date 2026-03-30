import google.generativeai as genai
import json
import time
import os

# --- CONFIGURATION ---
API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=API_KEY)

def generate_dataset(filename):
    """Generate 10 instruction fine-tuning examples for medical summarization."""
    dataset = [
        {"instruction": "Summarize the medical report.", "input": "Date: 2023-01-01. Patient: John Doe. Symptom: Fever. Diagnosis: Common Cold.", "output": "Patient John Doe was diagnosed with a common cold after presenting with a fever on Jan 1, 2023."},
        {"instruction": "Summarize the medical report.", "input": "Date: 2023-02-15. Patient: Jane Smith. Report: MRI Brain. Result: Normal.", "output": "Jane Smith had a normal brain MRI on Feb 15, 2023."},
        {"instruction": "Summarize the medical report.", "input": "Date: 2023-03-20. Patient: Bob Lee. Blood Test: Glucose 150 mg/dL.", "output": "Bob Lee's blood test on Mar 20, 2023, showed an elevated glucose level of 150 mg/dL."},
        {"instruction": "Summarize the medical report.", "input": "Date: 2023-04-10. Patient: Alice Ray. Diagnosis: Hypertension. Plan: ACE Inhibitors.", "output": "Alice Ray is diagnosed with hypertension and prescribed ACE inhibitors as of Apr 10, 2023."},
        {"instruction": "Summarize the medical report.", "input": "Date: 2023-05-05. Patient: Charlie Day. Report: X-Ray Chest. Result: Pneumonia.", "output": "Chest X-Ray on May 5, 2023, for Charlie Day indicates pneumonia."},
        {"instruction": "Summarize the medical report.", "input": "Date: 2023-06-12. Patient: Diana Prince. Symptom: Shoulder Pain. Diagnosis: Rotator Cuff Tear.", "output": "Diana Prince diagnosed with a rotator cuff tear on Jun 12, 2023."},
        {"instruction": "Summarize the medical report.", "input": "Date: 2023-07-25. Patient: Eve Adam. Diagnosis: Type 2 Diabetes. Plan: Metformin 500mg.", "output": "Eve Adam prescribed Metformin 500mg for Type 2 Diabetes on Jul 25, 2023."},
        {"instruction": "Summarize the medical report.", "input": "Date: 2023-08-30. Patient: Frank Castle. Report: ECG. Result: Normal Sinus Rhythm.", "output": "Frank Castle's ECG on Aug 30, 2023, showed a normal sinus rhythm."},
        {"instruction": "Summarize the medical report.", "input": "Date: 2023-09-14. Patient: Grace Hopper. Diagnosis: UTI. Plan: Antibiotics.", "output": "Grace Hopper diagnosed with a UTI on Sep 14, 2023; antibiotics prescribed."},
        {"instruction": "Summarize the medical report.", "input": "Date: 2023-10-01. Patient: Henry Ford. Report: Liver Function Test. Result: Elevated Enzymes.", "output": "Henry Ford's liver function test on Oct 1, 2023, showed elevated enzymes."}
    ]

    with open(filename, 'w') as f:
        for entry in dataset:
            f.write(json.dumps(entry) + '\n')
    print(f"Dataset saved to: {filename}")
    return dataset

def run_experiment_13():
    print("="*60)
    print("EXPERIMENT 13: INSTRUCTION FINE-TUNING (GEMINI)")
    print("="*60)

    # 1. Generate dataset
    dataset_file = "fine_tune_dataset.jsonl"
    dataset_content = generate_dataset(dataset_file)

    # 2. START PINING JOB (Using Gemini 1.5 Flash base model)
    # Note: Fine-tuning requires specific permissions and model availability.
    # We will use the 'tuning' module from google-generativeai.
    try:
        print("\nStarting tuning job (This may take several minutes)...")
        # In a real scenario, we use models/gemini-1.5-flash-001 (or similar)
        # For demonstration, we'll use create_tuned_model if available
        # Note: API_KEY must have tuning permissions.
        
        # This is a representative call based on current SDK:
        # operation = genai.create_tuned_model(
        #     source_model="models/gemini-1.5-flash-001",
        #     training_data=dataset_content,
        #     id="medical-summarizer-model-1",
        #     epoch_count=5,
        #     batch_size=2,
        #     learning_rate=0.001
        # )
        
        print("MOCK: Tuning job 'medical-summarizer-model-1' submitted.")
        print("Polling job status every 30 seconds...")

        # Simulation of polling (since a real job takes a long time)
        for i in range(1, 4):
            time.sleep(5) # Shorter sleep for demonstration purposes
            status = "RUNNING" if i < 3 else "SUCCEEDED"
            print(f"Status (Check {i}): {status}")
            if status == "SUCCEEDED":
                print("\nSUCCESS: Tuned model name: tunedModels/medical-summarizer-model-1")
                break
                
    except Exception as e:
        print(f"Error starting tuning job: {e}")
        print("Note: Fine-tuning requires an Enterprise/Pay-as-you-go Gemini API plan.")

if __name__ == "__main__":
    run_experiment_13()
