from ocr import perform_OCR
from save_to_data_base import insert_medication
from validation import validate
#get image input 


#extract using ocr
def ocr_exctraction(image_path):
    try:
        perform_OCR(image_path=image_path)
        print("Sucessful")
    except Exception as err:
        print(err)
    

#validate using API OPENFDA and add missing data 
def validate_medication(drug_name):
    try:
        validate(drug_name)
    except Exception as err:
        return err
# save initial info to database
def save(data:dict):
    #try exc block inside
    insert_medication(data)
    return

