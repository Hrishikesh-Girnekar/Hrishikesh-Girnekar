from pathlib import Path
from xml.sax.saxutils import escape


OUTPUT_FILE = Path("info-card.svg")


# ---------------------------------------------------------
# Card content
# ---------------------------------------------------------

lines = [
    ("ROLE", "Java Backend Developer"),
    ("STACK", "Java • Spring Boot • React"),
    ("DATA", "MySQL • JPA • Hibernate"),
    ("BUILD", "REST APIs • Backend Systems"),
    ("PRACTICE", "DSA • SQL • System Design"),
    ("TOOLS", "Git • GitHub • Docker"),
    ("AI", "Gemini Integration"),
    ("STATUS", "Building & Learning 🚀"),
]


# ---------------------------------------------------------
# Card dimensions
# ---------------------------------------------------------

WIDTH = 490
HEIGHT = 430

LEFT = 28
TOP = 82

LINE_HEIGHT = 38


# ---------------------------------------------------------
# Build SVG
# ---------------------------------------------------------

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
    width="{WIDTH}"
    height="{HEIGHT}"
    viewBox="0 0 {WIDTH} {HEIGHT}">

    <rect
        x="1"
        y="1"
        width="{WIDTH - 2}"
        height="{HEIGHT - 2}"
        rx="14"
        fill="#0d1117"
        stroke="#30363d"
        stroke-width="2"/>

    <!-- Terminal dots -->

    <circle cx="22" cy="22" r="5" fill="#ff5f56"/>
    <circle cx="40" cy="22" r="5" fill="#ffbd2e"/>
    <circle cx="58" cy="22" r="5" fill="#27c93f"/>

    <!-- Terminal title -->

    <text
        x="82"
        y="27"
        fill="#8b949e"
        font-family="monospace"
        font-size="13">
        hrishi@github ~ $ whoami
    </text>

    <!-- Divider -->

    <line
        x1="22"
        y1="48"
        x2="{WIDTH - 22}"
        y2="48"
        stroke="#30363d"
        stroke-width="1"/>

    <!-- Command -->

    <text
        x="{LEFT}"
        y="70"
        fill="#58a6ff"
        font-family="monospace"
        font-size="12">
        &gt; developer.profile
    </text>
'''


# ---------------------------------------------------------
# Add information rows
# ---------------------------------------------------------

for index, (key, value) in enumerate(lines):

    y = TOP + index * LINE_HEIGHT

    delay = index * 0.12

    svg += f'''
    <g
        opacity="0"
        style="animation: showLine 0.5s ease-out {delay:.2f}s forwards;">

        <text
            x="{LEFT}"
            y="{y}"
            fill="#8b949e"
            font-family="monospace"
            font-size="12">
            &gt; {key}
        </text>

        <text
            x="145"
            y="{y}"
            fill="#f0f6fc"
            font-family="monospace"
            font-size="12">
            {escape(value)}
        </text>

    </g>
'''


# ---------------------------------------------------------
# Animation
# ---------------------------------------------------------

svg += '''
    <style>

        @keyframes showLine {

            from {
                opacity: 0;
                transform: translateX(-8px);
            }

            to {
                opacity: 1;
                transform: translateX(0);
            }

        }

    </style>

</svg>
'''


# ---------------------------------------------------------
# Save
# ---------------------------------------------------------

OUTPUT_FILE.write_text(
    svg,
    encoding="utf-8"
)

print(f"Done! Created: {OUTPUT_FILE}")