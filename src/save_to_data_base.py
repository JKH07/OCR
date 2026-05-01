
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


def active_ingredient_id(text):
    #get name only
  
    pattern = r'([A-Z][a-zA-Z\s]+(?:HCl|HBr|Na|Mg)?)\s+(\d+(?:\.\d+)?\s*mg)'
    matches = re.findall(pattern, text)

    ingredients = [{"name": m[0].strip(), "dose": m[1].strip()} for m in matches]
    print(ingredients)
    print(ingredients[0]['name'])
    name=ingredients[0]['name']
    supabase = get_supabase_client()

    try:
        result = supabase.table("active_ingredients") \
        .select("id") \
        .eq("name", name) \
        .execute()

        print(result.data[0]['id'])
        return result.data[0]['id']
    except PostgrestAPIError as e:
        print(f"Database API error: {e.message}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def insert_medication(data: dict):
    print(data['active_ingredient'])
    ing_id=active_ingredient_id(data['active_ingredient'])
    data['active_ingredient']=ing_id
    supabase = get_supabase_client()
    
    try:
        response = supabase.table("medication").insert(data).execute()
        
        print("Data sent successfully.")
        return response

    except PostgrestAPIError as e:
        print(f"Database API error: {e.message}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    