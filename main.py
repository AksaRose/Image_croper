from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from PIL import Image, ImageDraw  # Fix: Import ImageDraw
import io

app = FastAPI()

def crop_to_circle(image):
    """Crop the image to a circular shape."""
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)  # Fix: Use ImageDraw.Draw instead of Image.Draw
    draw.ellipse((0, 0, size, size), fill=255)

    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(image.crop((0, 0, size, size)), (0, 0), mask)

    return result

@app.post("/crop")
async def crop_image(
    shape: str = Form(...),  # Accept shape as form data
    file: UploadFile = File(...)
):
    image = Image.open(io.BytesIO(await file.read())).convert("RGBA")
    
    if shape == "circle":
        cropped_image = crop_to_circle(image)
    else:
        return {"error": "Shape not supported yet"}
    
    img_byte_arr = io.BytesIO()
    cropped_image.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)
    
    return StreamingResponse(img_byte_arr, media_type="image/png", headers={"Content-Disposition": "inline; filename=cropped.png"})
