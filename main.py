from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from PIL import Image, ImageDraw
import io

app = FastAPI()

def crop_to_circle(image):
    """Crop the image to a circular shape."""
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(image.crop((0, 0, size, size)), (0, 0), mask)

    return result

def crop_to_square(image):
    """Crop the image to a square."""
    size = min(image.size)
    return image.crop((0, 0, size, size))

def crop_to_triangle(image):
    """Crop the image to a triangular shape."""
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    points = [(size//2, 0), (0, size), (size, size)]
    draw.polygon(points, fill=255)

    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(image.crop((0, 0, size, size)), (0, 0), mask)

    return result

def crop_to_hexagon(image):
    """Crop the image to a hexagonal shape."""
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    points = [
        (size*0.25, 0), (size*0.75, 0), 
        (size, size*0.5), (size*0.75, size),
        (size*0.25, size), (0, size*0.5)
    ]
    draw.polygon(points, fill=255)

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
    elif shape == "square":
        cropped_image = crop_to_square(image)
    elif shape == "triangle":
        cropped_image = crop_to_triangle(image)
    elif shape == "hexagon":
        cropped_image = crop_to_hexagon(image)
    else:
        return {"error": f"Shape '{shape}' is not supported. Try: circle, square, triangle, hexagon."}
    
    img_byte_arr = io.BytesIO()
    cropped_image.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)
    
    return StreamingResponse(img_byte_arr, media_type="image/png", headers={"Content-Disposition": "inline; filename=cropped.png"})
