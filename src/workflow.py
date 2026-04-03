from ocr import perform_OCR
from save_to_data_base import insert_medication
from validation import validate

def pipeline(image):
    data=ocr_exctraction(image)
    if(data):
        print(data['name'])
        if(validate_medication(data['name'])==True):
            #data_filled=fill_rest_of_data(data)
            save(data)
        else:
            print ("invalid medication.")
    
#extract using ocr
def ocr_exctraction(image_path):
    try:
        data=perform_OCR(image_path=image_path)
        print("Sucessful OCR")
        print(data)
        return data
    except Exception as err:
        print(err)
    

#validate using API OPENFDA and add missing data 
def validate_medication(drug_name):
    try:
        found=validate(drug_name)
        return found
    except Exception as err:
        print(err)

def fill_rest_of_data():
    return
# save initial info to database
def save(data:dict):
    #try exc block inside
    insert_medication(data)

#pipeline("meds\med_12.jpg")