from datetime import date
from save_to_data_base import insert_medication
from validation import validate
# Preparing data
new_entry = {
    "name": "Atenolol",
    "instructions_of_use": "Take with water after food.",
    "number_of_tablets": 32,
    "expiry": str(date(2027, 12, 1)),
    "illness": "Pain relief and fever",
    "food_interactions": "Avoid excessive alcohol.",
    "overdose": 4.0, 
    "side_effects": ["Nausea", "Rash", "Dizziness"],
    "not_suitable_for": "0-12",
    "nhs_link": "https://www.nhs.uk/medicines/paracetamol-for-adults/",
    "raw_match": [{"source": "pharmacy_v1", "score": 0.98}] 
}

# Call the function
result=False
if(validate(new_entry['name'])):
    result = insert_medication(new_entry)

if result:
    print("Success!")
else:
    print("Failed to insert data.")