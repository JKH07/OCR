import logging
import requests

logger = logging.getLogger(__name__)

def validate(medication_data):
    medication_name = medication_data['name']
    
    params = {
        "search": f'openfda.brand_name:"{medication_name}"',
        "limit": 1
    }
    
    response = requests.get("https://api.fda.gov/drug/label.json", params=params, timeout=5)
    
    print(response.url)
    print(response.status_code)
    
    data = response.json()
    results = data.get("results", [])
    
    logger.debug("\t API query: %s", response.url)

    if response.status_code == 200 and len(results) != 0:
        medication_name_valid = True
    elif response.status_code == 404 and data.get("error", {}).get("code") == "NOT_FOUND":
        logger.warning("\t Medication name not found: %s", medication_name)
        medication_name_valid = False
    else:
        logger.warning("\t API request failed with status code: %d", response.status_code)
        medication_name_valid = False

    if medication_name_valid:
        need = results[0]
        #medication_data['active_ingredient'] = "Hydrochlorothiazide"
        medication_data['instructions_of_use'] = need.get('indications_and_usage', [None])[0]
        medication_data['warnings'] = need.get('warnings', [None])[0]
        medication_data['overdose'] = (
            need.get('overdosage', [None])[0] or
            need.get('overdose', [None])[0] or  
            None
        )
        print(f'here jana {medication_data}')
        print("valid med")
        return medication_data
    else:
        print("med doesn't exist")


import requests

def get_active_ingredients(drug_name: str) -> list[str]:
    try:
        #Get RXCUI from drug name
        rxcui_res = requests.get(
            "https://rxnav.nlm.nih.gov/REST/rxcui.json",
            params={"name": drug_name}
        )
        rxcui_res.raise_for_status()
        rxcui_data = rxcui_res.json()

        rxcui_list = rxcui_data.get("idGroup", {}).get("rxnormId")
        if not rxcui_list:
            print(f"No RXCUI found for: {drug_name}")
            return []

        rxcui = rxcui_list[0]

        # Get ingredients using RXCUI
        ingredients_res = requests.get(
            f"https://rxnav.nlm.nih.gov/REST/rxcui/{rxcui}/related.json",
            params={"rela": "has_ingredient"}
        )
        ingredients_res.raise_for_status()
        ingredients_data = ingredients_res.json()

        concept_groups = ingredients_data.get("relatedGroup", {}).get("conceptGroup", [])
        ingredients = [
            prop["name"].lower()
            for group in concept_groups
            for prop in group.get("conceptProperties", [])
        ]

        if not ingredients:
            print(f"No ingredients found for: {drug_name}")
            return []

        return ingredients

    except requests.RequestException as e:
        print(f"Request error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
    
get_active_ingredients("panadol")