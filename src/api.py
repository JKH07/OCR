
from fastapi import FastAPI, File, UploadFile, HTTPException

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

    # --- YOUR OCR LOGIC GOES HERE ---
    # text_result = my_ocr_function(image_data)
    # --------------------------------

    return {
        "message": "Image received successfully",
        "filename": file.filename,
        "ocr_preview": "OCR processing would happen here"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)