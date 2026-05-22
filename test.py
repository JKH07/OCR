import requests

url = "https://OCR_med.onrender.com/upload-image"



files = {
    "file": open("test.jpg", "rb")
}

response = requests.post(
    url,
    files=files
)

print(response.status_code)
print(response.json())