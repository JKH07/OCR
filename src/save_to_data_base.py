
from supabase import create_client, Client,PostgrestAPIError
import os
from dotenv import load_dotenv
from datetime import date
import re

load_dotenv()

def get_supabase_client() -> Client:
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if not url or not key:
        raise ValueError("Supabase credentials not found in environment variables.")
    return create_client(url, key)

def active_ingredient_id(name):
   
    supabase = get_supabase_client()

    try:
        result = supabase.table("active_ingredients") \
            .select("id") \
            .ilike("name", name) \
            .execute()

        if not result.data:
            print(f"Ingredient not found: {name}")
            return None

        print(result.data[0]['id'])
        return result.data[0]['id']
    except PostgrestAPIError as e:
        print(f"Database API error: {e.message}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def insert_medication(data: dict,data2:dict):
    supabase = get_supabase_client()
    
    try:
        response = supabase.table("medication").insert(data).execute()
        response2=supabase.table("medication_active").insert(data2).execute()
        print("Data sent successfully.")
        return response

    except PostgrestAPIError as e:
        print(f"Database API error: {e.message}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    