import logging
import requests

#to track errors
logger = logging.getLogger(__name__)

def validate(medication_data):
    medication_name=medication_data['name']
    medication_name.replace(" ","")
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

    if(medication_name_valid):
        #filling data
        need=results[0]
        medication_data['active_ingredient']=need['active_ingredient'][0]
        medication_data['overdose']=need['overdosage'][0]
        medication_data['instructions_of_use']=need['indications_and_usage'][0]
        medication_data['stop_use']=need['stop_use'][0]
        medication_data['warnings']=need['warnings'][0]
        print(medication_data)
        print("valid med")
        return medication_data
    else :
        print("med doesnt exist")



