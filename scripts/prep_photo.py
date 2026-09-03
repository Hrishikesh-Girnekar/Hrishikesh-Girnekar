from pathlib import Path

import cv2
import numpy as np
from PIL import Image
from rembg import remove


# ---------------------------------------------------------
# 1. File locations
# ---------------------------------------------------------

INPUT_FILE = Path("source-photo.jpg")
OUTPUT_FILE = Path("source-prepped.png")


# ---------------------------------------------------------
# 2. Check that the input photo exists
# ---------------------------------------------------------

if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"Could not find {INPUT_FILE}. "
        "Make sure source-photo.jpg is in the project root."
    )


# ---------------------------------------------------------
# 3. Remove the background
# ---------------------------------------------------------

print("Removing background...")

input_image = Image.open(INPUT_FILE).convert("RGBA")

foreground = remove(input_image)


# ---------------------------------------------------------
# 4. Put the person on a pure white background
# ---------------------------------------------------------

print("Creating white background...")

white_background = Image.new(
    "RGBA",
    foreground.size,
    (255, 255, 255, 255)
)

white_background.alpha_composite(foreground)

white_background = white_background.convert("RGB")


# ---------------------------------------------------------
# 5. Convert image to grayscale
# ---------------------------------------------------------

print("Converting image to grayscale...")

image_array = np.array(white_background)

gray = cv2.cvtColor(
    image_array,
    cv2.COLOR_RGB2GRAY
)


# ---------------------------------------------------------
# 6. Improve local contrast using CLAHE
# ---------------------------------------------------------

print("Improving contrast...")

clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8, 8)
)

enhanced = clahe.apply(gray)


# ---------------------------------------------------------
# 7. Save the final prepared image
# ---------------------------------------------------------

print("Saving prepared image...")

cv2.imwrite(
    str(OUTPUT_FILE),
    enhanced
)

print(f"Done! Created: {OUTPUT_FILE}")