from datetime import date
from save_to_data_base import insert_medication
from validation import validate
from ocr import perform_OCR
from supabase import create_client, Client, PostgrestAPIError
import os
from dotenv import load_dotenv
from validation import validate
from save_to_data_base import insert_medication

data={
    "name": "panadol",
        "active_ingredient":{"type":"STRING"},
        "overdose":{"type":"STRING"},
        "instructions_of_use":{"type":"STRING"},
        "warnings":{"type":"STRING"},
        "stop_use":{"type":"STRING"}
}


tt=validate(data)
print(tt)
insert_medication(tt)