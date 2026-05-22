import requests

url = "https://OCR_med.onrender.com/upload-image"

headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}

files = {
    "file": open("test.jpg", "rb")
}

response = requests.post(
    url,
    headers=headers,
    files=files
)

print(response.status_code)
print(response.json())