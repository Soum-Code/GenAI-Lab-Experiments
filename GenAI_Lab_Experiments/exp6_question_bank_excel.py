import openpyxl
import os

def run_experiment_6():
    print("="*60)
    print("EXPERIMENT 6: QUESTION BANK EXCEL (OPENPYXL)")
    print("="*60)

    # Define the questions
    questions = [
        {"id": 1, "text": "What is the hemoglobin level?", "category": "Blood Test"},
        {"id": 2, "text": "What is the potassium level?", "category": "Blood Test"},
        {"id": 3, "text": "What is the patient's diagnosis?", "category": "Diagnosis"},
        {"id": 4, "text": "Are there any abnormalities in the MRI scan?", "category": "MRI Scan"},
        {"id": 5, "text": "What is the patient's age?", "category": "Demographics"},
        {"id": 6, "text": "What medication was prescribed?", "category": "Prescription"},
        {"id": 7, "text": "Is there any history of diabetes?", "category": "History"},
        {"id": 8, "text": "What is the recommended follow-up date?", "category": "Follow-up"},
        {"id": 9, "text": "What is the report type?", "category": "Metadata"},
        {"id": 10, "text": "What is the patient's name?", "category": "Metadata"}
    ]

    filename = "question_bank.xlsx"
    filepath = os.path.abspath(filename)

    # Create workbook and sheet
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Question Bank"

    # Add header row
    headers = ["Question ID", "Question Text", "Category"]
    sheet.append(headers)

    # Styling header (optional but good practice)
    from openpyxl.styles import Font
    for cell in sheet[1]:
        cell.font = Font(bold=True)

    # Add question data
    for q in questions:
        sheet.append([q["id"], q["text"], q["category"]])

    # Save workbook
    try:
        wb.save(filename)
        print(f"SUCCESS: Question bank saved as: {filename}")
        print(f"Full path: {filepath}")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    run_experiment_6()
