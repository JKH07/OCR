from datetime import date
from save_to_data_base import insert_medication
from validation import validate
from ocr import perform_OCR
# Preparing data
new_entry = {
    "name": "Atenolol",
    "instructions_of_use": "Take with water after food.",
    "number_of_tablets": 32,
    "overdose": 4.0, 
    "warnings": ["Nausea", "Rash", "Dizziness"],

}

result=perform_OCR("meds/med_14.jpg")
print(result)