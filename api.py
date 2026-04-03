
from fastapi import FastAPI, File, UploadFile, HTTPException
import os
import uvicorn
from main import main
app = FastAPI()

@app.post("/upload-image")
async def receive_image(file: UploadFile = File(...)):
    # check if image
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    # Read the image into memory as bytes
    image_data = await file.read()

    # logging
    print(f"Received {file.filename} which is {len(image_data)} bytes.")

    # ocr
    main(image_data)

    return {
        "message": "Image received successfully",
        "filename": file.filename,
        "ocr_preview": "OCR processing would happen here"
    }

if __name__ == "__main__":
    
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)