from google import genai
from google.genai import types
import pathlib
import os
from dotenv import load_dotenv
load_dotenv()

from datetime import date
import PIL.Image

#connection to llm api
def client_creation() :
    key = os.environ.get("API_KEY")
    client = genai.Client(api_key=key)
    if not key:
        raise ValueError("Error reaching gemini")
    return client

#prepare data form

data_form = {
    "type": "OBJECT",
    "properties": {
        "name": {"type": "STRING"},
        "active ingredient":{"type":"STRING"},
        "overdose":{"type":"STRING"},
        "instructions_of_use":{"type":"STRING"},
        "warnings":{"type":"STRING"},
    },
    "required": ["name"] 
}
#nlp prompt
prompt = "Extract medication details from this image. . Make sure this information is logical and not repetitive. If a value is not found, " \
"leave it as an empty string or 0 as per the type."

#return image contents and classify 
def perform_OCR(image_path):
  client=client_creation()
  image = PIL.Image.open(image_path)
  response = client.models.generate_content(
      model="gemini-2.5-flash-lite", 
      contents=[prompt, image],
      config=types.GenerateContentConfig(
          response_mime_type="application/json",
          response_schema=data_form,
      ),
  )

  data = response.parsed 
  return data

