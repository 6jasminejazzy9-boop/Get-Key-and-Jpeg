import os
from PIL import Image
import io

def save_data(filename, data):
    """Saves data to a local file."""
    try:
        with open(filename, "w") as f:
            f.write(str(data))
        print(f"Success: Saved to {filename}")
    except Exception as e:
        print(f"Error: Could not save file – {e}")

def save_jpeg(filename, image_data):
    """Saves image data as JPEG file."""
    try:
        if isinstance(image_data, bytes):
            img = Image.open(io.BytesIO(image_data))
        else:
            img = Image.open(image_data)
        
        img.convert('RGB').save(filename, 'JPEG')
        print(f"Success: Saved JPEG to {filename}")
    except Exception as e:
        print(f"Error: Could not save JPEG – {e}")

if __name__ == "__main__":
    # Logic goes here
    retrieved_key = "INSERT_KEY_HERE"
    retrieved_image_data = "INSERT_IMAGE_DATA_HERE"
    
    save_data("key.txt", retrieved_key)
    # save_jpeg("output.jpg", retrieved_image_data)
