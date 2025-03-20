from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from PIL import Image, ImageDraw
import io
import math

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

def crop_to_star(image):
    """Crop the image to a star shape."""
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)

    num_points = 5  # 5-point star
    center_x, center_y = size // 2, size // 2
    outer_radius = size * 0.45
    inner_radius = outer_radius * 0.5
    angle = math.pi / num_points

    points = []
    for i in range(num_points * 2):
        r = outer_radius if i % 2 == 0 else inner_radius
        theta = i * angle - math.pi / 2
        x = center_x + r * math.cos(theta)
        y = center_y + r * math.sin(theta)
        points.append((x, y))

    draw.polygon(points, fill=255)

    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(image.crop((0, 0, size, size)), (0, 0), mask)
    return result

def crop_to_heart(image):
    """Crop the image to a heart shape."""
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)

    # Define heart shape points
    points = [
        (size * 0.5, size * 0.2),  # Top center
        (size * 0.8, size * 0.05), # Right bump
        (size * 1.0, size * 0.3),  # Right curve
        (size * 0.9, size * 0.6),  # Right bottom curve
        (size * 0.5, size * 1.0),  # Bottom point
        (size * 0.1, size * 0.6),  # Left bottom curve
        (size * 0.0, size * 0.3),  # Left curve
        (size * 0.2, size * 0.05), # Left bump
    ]
    draw.polygon(points, fill=255)

    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(image.crop((0, 0, size, size)), (0, 0), mask)
    return result
def crop_to_circle(image):
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(image.crop((0, 0, size, size)), (0, 0), mask)
    return result

def crop_to_speech_bubble(image):
    """Crop image into a speech bubble shape."""
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)

    # Speech bubble main oval
    draw.ellipse((size * 0.1, size * 0.1, size * 0.9, size * 0.8), fill=255)

    # Speech tail
    draw.polygon([(size * 0.4, size * 0.75), (size * 0.6, size * 0.75), (size * 0.5, size * 0.95)], fill=255)

    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(image.crop((0, 0, size, size)), (0, 0), mask)
    return result

def crop_to_cloud(image):
    """Crop image into a cloud shape."""
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)

    # Cloud main circles
    draw.ellipse((size * 0.15, size * 0.3, size * 0.75, size * 0.8), fill=255)
    draw.ellipse((size * 0.4, size * 0.2, size * 0.85, size * 0.7), fill=255)
    draw.ellipse((size * 0.1, size * 0.4, size * 0.6, size * 0.85), fill=255)

    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(image.crop((0, 0, size, size)), (0, 0), mask)
    return result
def crop_to_flower(image):
    """Crop the image to an eight-petal flower shape."""
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)

    center_x, center_y = size // 2, size // 2
    petal_radius = size // 3  # Adjust petal size
    roundness = 0.6  # Control petal fatness
    petals = 8

    for i in range(petals):
        angle = math.radians((i / petals) * 360)  # Convert to radians
        x = center_x + petal_radius * math.cos(angle)
        y = center_y + petal_radius * math.sin(angle)
        draw.ellipse(
            (x - petal_radius * roundness, y - petal_radius * roundness,
             x + petal_radius * roundness, y + petal_radius * roundness),
            fill=255
        )

    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(image.crop((0, 0, size, size)), (0, 0), mask)
    return result

def crop_to_lightning_bolt(image):
    """Crop the image to a lightning bolt shape using two distinct triangles."""
    # Use the minimum dimension to ensure a square working area
    size = min(image.size)
    
    # Create a transparent mask
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    
    # Define the two triangles that form the lightning bolt
    # First triangle (upper part of bolt)
    triangle1 = [
        (size * 0.5, 0),        # Top
        (size * 0.3, size * 0.5),  # Bottom left
        (size * 0.6, size * 0.5)   # Bottom right
    ]
    
    # Second triangle (lower part of bolt)
    triangle2 = [
        (size * 0.4, size * 0.5),  # Top left
        (size * 0.7, size * 0.5),  # Top right
        (size * 0.5, size)         # Bottom center
    ]
    
    # Draw the two triangles
    draw.polygon(triangle1, fill=255)
    draw.polygon(triangle2, fill=255)
    
    # Create a new transparent image for the result
    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    
    # Paste the original image using the mask
    result.paste(image.crop((0, 0, size, size)), (0, 0), mask)
    
    return result

def crop_to_crescent_moon(image):
    """Crop the image to a crescent moon shape."""
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)

    # Outer circle
    draw.ellipse((0, 0, size, size), fill=255)

    # Inner circle (to create crescent effect)
    draw.ellipse((size * 0.3, 0, size * 1.3, size), fill=0)

    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(image.crop((0, 0, size, size)), (0, 0), mask)
    return result

def crop_to_diamond(image):
    """Crop the image to a diamond shape."""
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)

    points = [
        (size * 0.5, 0), (size, size * 0.5),
        (size * 0.5, size), (0, size * 0.5)
    ]
    draw.polygon(points, fill=255)

    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(image.crop((0, 0, size, size)), (0, 0), mask)
    return result

def crop_to_butterfly(image):
    """Crop the image to a butterfly shape (simple symmetrical shape)."""
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)

    # Rough butterfly shape
    points = [
        (size * 0.2, size * 0.5), (size * 0.4, size * 0.1),
        (size * 0.6, size * 0.1), (size * 0.8, size * 0.5),
        (size * 0.6, size * 0.9), (size * 0.4, size * 0.9)
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
    elif shape == "star":
        cropped_image = crop_to_star(image)
    elif shape == "heart":
        cropped_image = crop_to_heart(image)
    elif shape == "speech_bubble":
        cropped_image = crop_to_speech_bubble(image)
    elif shape == "cloud":
        cropped_image = crop_to_cloud(image)
    elif shape == "flower":
        cropped_image = crop_to_flower(image)
    elif shape == "lightning_bolt":
        cropped_image = crop_to_lightning_bolt(image)
    elif shape == "crescent_moon":
        cropped_image = crop_to_crescent_moon(image)
    elif shape == "diamond":
        cropped_image = crop_to_diamond(image)
    elif shape == "butterfly":
        cropped_image = crop_to_butterfly(image)
    else:
        return {"error": f"Shape '{shape}' is not supported. Try: circle, square, triangle, hexagon, star, heart."}
    
    img_byte_arr = io.BytesIO()
    cropped_image.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)
    
    return StreamingResponse(img_byte_arr, media_type="image/png", headers={"Content-Disposition": "inline; filename=cropped.png"})
