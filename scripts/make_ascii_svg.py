from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image


# ---------------------------------------------------------
# Settings
# ---------------------------------------------------------

INPUT_FILE = Path("source-prepped.png")
OUTPUT_FILE = Path("avi-ascii.svg")

CHAR_WIDTH = 100

RAMP = " .`:-=+*cs#%@"

CHAR_ASPECT = 0.50

FONT_SIZE = 8
LINE_HEIGHT = 9

TEXT_COLOR = "#555555"

ANIMATION_DURATION = 0.08


# ---------------------------------------------------------
# Check input file
# ---------------------------------------------------------

if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"Could not find {INPUT_FILE}. "
        "Run prep_photo.py first."
    )


# ---------------------------------------------------------
# Load image
# ---------------------------------------------------------

print("Loading prepared image...")

image = Image.open(INPUT_FILE).convert("L")

original_width, original_height = image.size


# ---------------------------------------------------------
# Calculate ASCII dimensions
# ---------------------------------------------------------

char_width = CHAR_WIDTH

char_height = max(
    1,
    int(
        original_height
        / original_width
        * char_width
        * CHAR_ASPECT
    )
)

print(
    f"Original image: "
    f"{original_width} x {original_height}"
)

print(
    f"ASCII grid: "
    f"{char_width} x {char_height}"
)


# ---------------------------------------------------------
# Resize image
# ---------------------------------------------------------

image = image.resize(
    (char_width, char_height)
)

pixels = image.load()


# ---------------------------------------------------------
# Convert pixels to ASCII
# ---------------------------------------------------------

ascii_rows = []

for y in range(char_height):

    row = []

    for x in range(char_width):

        brightness = pixels[x, y]

        index = int(
            brightness
            / 255
            * (len(RAMP) - 1)
        )

        character = RAMP[index]

        row.append(character)

    ascii_rows.append("".join(row))


# ---------------------------------------------------------
# SVG dimensions
# ---------------------------------------------------------

svg_width = char_width * FONT_SIZE
svg_height = char_height * LINE_HEIGHT


# ---------------------------------------------------------
# Start SVG
# ---------------------------------------------------------

print("Creating animated SVG...")

svg_parts = []

svg_parts.append(
    f'''<svg xmlns="http://www.w3.org/2000/svg"
    width="{svg_width}"
    height="{svg_height}"
    viewBox="0 0 {svg_width} {svg_height}">

    <rect
        width="100%"
        height="100%"
        fill="white"/>

    <style>
        .ascii-row {{
            opacity: 0;
            animation: typeRow
                {ANIMATION_DURATION}s
                ease-out
                forwards;
        }}

        @keyframes typeRow {{
            from {{
                opacity: 0;
                transform: translateX(-8px);
            }}

            to {{
                opacity: 1;
                transform: translateX(0);
            }}
        }}
    </style>

    <g
        fill="{TEXT_COLOR}"
        font-family="monospace"
        font-size="{FONT_SIZE}px"
        xml:space="preserve">
'''
)


# ---------------------------------------------------------
# Add animated rows
# ---------------------------------------------------------

for row_number, row in enumerate(ascii_rows):

    y = (row_number + 1) * LINE_HEIGHT

    delay = row_number * 0.045

    svg_parts.append(
        f'''<text
            class="ascii-row"
            x="0"
            y="{y}"
            style="animation-delay: {delay:.3f}s">
            {escape(row)}
        </text>
'''
    )


# ---------------------------------------------------------
# Finish SVG
# ---------------------------------------------------------

svg_parts.append(
    """
    </g>
</svg>
"""
)


# ---------------------------------------------------------
# Save SVG
# ---------------------------------------------------------

OUTPUT_FILE.write_text(
    "".join(svg_parts),
    encoding="utf-8"
)

print(
    f"Done! Created animated SVG: {OUTPUT_FILE}"
)