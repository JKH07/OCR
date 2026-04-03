import logging
import requests

#to track errors
logger = logging.getLogger(__name__)

def validate(medication_name):
    #build url
    api_query = f'https://api.fda.gov/drug/label.json?search=openfda.brand_name="{medication_name}"&limit=1'
    
    logger.debug("\t API query: %s", api_query)

    response = requests.get(api_query, timeout=5)
    data = response.json()
    results = data.get("results", [])

    if response.status_code == 200 and len(results) != 0:
        medication_name_valid = True
    elif response.status_code == 404 and data["error"]["code"] == "NOT_FOUND":
        logger.warning("\t Medication name: %s", medication_name)
        logger.warning("\t API error code: %s", data["error"]["code"])
        medication_name_valid = False
    else:
        logger.warning(
            "\t API request failed with status code: %d", response.status_code
        )
        medication_name_valid = False

    return medication_name_valid


tt=validate("CALCIUM CARBONATE")
print(tt)