import os
import re
import fitz # PyMuPDF
import glob

# --- HELPER FUNCTIONS ---
def get_pdf_metadata(filepath):
    """Extract metadata and text from PDF using PyMuPDF."""
    try:
        doc = fitz.open(filepath)
        text = ""
        for page in doc:
            text += page.get_text()
        
        # Regex patterns for metadata
        metadata = {
            "Patient Name": re.search(r"Patient Name:\s*(.*)", text, re.IGNORECASE),
            "Date": re.search(r"Date:\s*(.*)", text, re.IGNORECASE),
            "Report Type": re.search(r"Report Type:\s*(.*)", text, re.IGNORECASE)
        }
        
        # Extract matches
        for key, match in metadata.items():
            metadata[key] = match.group(1).strip() if match else "Not Found"
            
        return metadata, len(text.split())
    except Exception as e:
        print(f"Error reading PDF {filepath}: {e}")
        return None, 0

def get_text_metadata(filepath):
    """Extract metadata and text from TXT file."""
    try:
        with open(filepath, 'r') as f:
            text = f.read()
        
        # Regex patterns for metadata
        metadata = {
            "Patient Name": re.search(r"Patient Name:\s*(.*)", text, re.IGNORECASE),
            "Date": re.search(r"Date:\s*(.*)", text, re.IGNORECASE),
            "Report Type": re.search(r"Report Type:\s*(.*)", text, re.IGNORECASE)
        }
        
        # Extract matches
        for key, match in metadata.items():
            metadata[key] = match.group(1).strip() if match else "Not Found"
            
        return metadata, len(text.split())
    except Exception as e:
        print(f"Error reading TXT {filepath}: {e}")
        return None, 0

def create_dummy_reports(folder_path):
    """Create dummy medical reports for testing."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 1. Dummy TXT
    txt_content = """Medical Report
Date: 2023-05-12
Patient Name: John Doe
Report Type: Blood Test
Summary: Hemoglobin level is normal. Potassium is slightly high.
"""
    with open(os.path.join(folder_path, "report1.txt"), 'w') as f:
        f.write(txt_content)

    # 2. Dummy PDF (using fitz to create one)
    try:
        pdf_path = os.path.join(folder_path, "report2.pdf")
        doc = fitz.open()
        page = doc.new_page()
        page.insert_text((50, 50), "Medical Report\nDate: 2023-06-15\nPatient Name: Jane Smith\nReport Type: MRI Scan\nNo abnormalities found.")
        doc.save(pdf_path)
    except Exception as e:
        print(f"Skipping PDF creation: {e}")

def run_experiment_5():
    print("="*60)
    print("EXPERIMENT 5: MEDICAL REPORT READER (PDF & TXT)")
    print("="*60)

    # User input for folder path
    folder_path = input("Enter directory path (default: './medical_reports'): ") or "./medical_reports"

    # Create dummy reports if folder is empty
    if not os.path.exists(folder_path) or not os.listdir(folder_path):
        print(f"Folder '{folder_path}' is empty or missing. Creating dummy reports...")
        create_dummy_reports(folder_path)

    # List files dynamically
    files = glob.glob(os.path.join(folder_path, "*"))

    print("\nFILES PROCESSED:")
    print("-" * 80)
    for filepath in files:
        filename = os.path.basename(filepath)
        size = os.path.getsize(filepath)
        
        metadata = None
        word_count = 0

        if filename.lower().endswith(".pdf"):
            metadata, word_count = get_pdf_metadata(filepath)
        elif filename.lower().endswith(".txt"):
            metadata, word_count = get_text_metadata(filepath)
        else:
            print(f"Skipping {filename}: Unsupported file type.")
            continue

        if metadata:
            print(f"Filename: {filename}")
            print(f"Size: {size / 1024:.2f} KB")
            print(f"Word Count: {word_count}")
            print(f"Patient Name: {metadata['Patient Name']}")
            print(f"Date: {metadata['Date']}")
            print(f"Report Type: {metadata['Report Type']}")
            print("-" * 80)

if __name__ == "__main__":
    run_experiment_5()
