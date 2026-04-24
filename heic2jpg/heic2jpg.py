import os
from PIL import Image
import pillow_heif

# Register HEIC support
pillow_heif.register_heif_opener()

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define input and output folders
heic_folder = os.path.join(script_dir, "heic")
jpg_folder = os.path.join(script_dir, "jpg")

# Create jpg folder if it doesn't exist
os.makedirs(jpg_folder, exist_ok=True)

# Loop through all files in the heic folder
if os.path.exists(heic_folder):
    for filename in os.listdir(heic_folder):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(heic_folder, filename)

            # Define output .jpg path in jpg folder
            jpg_filename = os.path.splitext(filename)[0] + ".jpg"
            jpg_path = os.path.join(jpg_folder, jpg_filename)

            try:
                with Image.open(heic_path) as img:
                    img.convert("RGB").save(jpg_path, "JPEG")
                    print(f"Converted: {filename} → {jpg_filename}")
                
                # Delete the original heic file after successful conversion
                os.remove(heic_path)
                print(f"Deleted original: {filename}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")
else:
    print(f"Directory '{heic_folder}' does not exist.")
