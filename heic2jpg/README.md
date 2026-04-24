# HEIC to JPG Converter

This script automates the conversion of Apple's High-Efficiency Image Container (HEIC) files into standard JPEG (JPG) format.

## Features

- **Batch Conversion**: Converts all `.heic` files within the designated `heic` input folder.
- **Auto-organization**: Automatically creates a `jpg` folder for the output images.
- **Space Saving**: Deletes the original `.heic` files automatically after a successful conversion.

## Prerequisites

Before running the script, ensure you have Python installed along with the required libraries.

1. Ensure Python 3.x is installed on your system.
2. Install the necessary Python packages using pip:

```bash
pip install Pillow pillow-heif
```

## How to Use

1. **Setup Folders**: In the same directory as the `heic2jpg.py` script, ensure there is a folder named `heic`.
2. **Add Files**: Place all the `.heic` images you want to convert into the `heic` folder.
3. **Run the Script**: Execute the script from your terminal or command prompt:

   ```bash
   python heic2jpg.py
   ```

4. **Retrieve Images**: Once the script finishes running, you will find your converted `.jpg` images inside the `jpg` folder. The script will automatically create this folder if it does not already exist.

## Important Note
The script is designed to **delete** the original `.heic` files once they have been successfully converted to `.jpg`. If you need to keep your original files, please ensure you have a backup before running the script.
