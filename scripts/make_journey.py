from pathlib import Path

OUTPUT_FILE = Path("journey.svg")

WIDTH = 1000
HEIGHT = 390

journey = [
    (
        "2021",
        "Engineering Foundation",
        "B.Tech in Electronics &amp; Telecommunication",
    ),
    (
        "2023",
        "Full-Stack Development",
        "PG-DAC • React • Node.js • Express • MongoDB",
    ),
    (
        "2025",
        "Java Backend",
        "Java 17 • Spring Boot • REST APIs • JPA",
    ),
    (
        "2026",
        "Backend Engineering",
        "Microservices • System Design • Docker • AWS",
    ),
]

svg = f'''<svg
    xmlns="http://www.w3.org/2000/svg"
    width="{WIDTH}"
    height="{HEIGHT}"
    viewBox="0 0 {WIDTH} {HEIGHT}">

    <rect
        width="100%"
        height="100%"
        rx="20"
        fill="#0d1117"
        stroke="#30363d"
        stroke-width="2"/>

    <style>

        .fade {{
            opacity: 0;
            animation: reveal 0.6s ease-out forwards;
        }}

        .label {{
            font-family: monospace;
            font-size: 13px;
            fill: #58a6ff;
            font-weight: bold;
        }}

        .heading {{
            font-family: monospace;
            font-size: 24px;
            fill: #f0f6fc;
            font-weight: bold;
        }}

        .year {{
            font-family: monospace;
            font-size: 13px;
            fill: #3fb950;
            font-weight: bold;
        }}

        .title {{
            font-family: monospace;
            font-size: 15px;
            fill: #f0f6fc;
            font-weight: bold;
        }}

        .description {{
            font-family: monospace;
            font-size: 12px;
            fill: #8b949e;
        }}

        .line {{
            stroke: #30363d;
            stroke-width: 2;
        }}

        .dot {{
            fill: #3fb950;
        }}

        @keyframes reveal {{
            from {{
                opacity: 0;
                transform: translateX(-10px);
            }}

            to {{
                opacity: 1;
                transform: translateX(0);
            }}
        }}

    </style>


    <text
        x="42"
        y="42"
        class="label fade"
        style="animation-delay: 0.1s">

        07 / JOURNEY

    </text>


    <text
        x="42"
        y="82"
        class="heading fade"
        style="animation-delay: 0.2s">

        How I got here

    </text>


    <!-- Timeline -->

    <line
        x1="75"
        y1="125"
        x2="75"
        y2="335"
        class="line"/>

'''

for index, (year, title, description) in enumerate(journey):

    y = 130 + index * 65
    delay = 0.35 + index * 0.15

    svg += f'''
    <g
        class="fade"
        style="animation-delay: {delay:.2f}s">

        <circle
            cx="75"
            cy="{y - 5}"
            r="6"
            class="dot"/>

        <text
            x="105"
            y="{y}"
            class="year">

            {year}

        </text>

        <text
            x="190"
            y="{y}"
            class="title">

            {title}

        </text>

        <text
            x="190"
            y="{y + 22}"
            class="description">

            {description}

        </text>

    </g>
    '''


svg += '''
    <text
        x="700"
        y="300"
        class="label fade"
        style="animation-delay: 1.1s">

        DIRECTION

    </text>

    <text
        x="700"
        y="330"
        class="title fade"
        style="animation-delay: 1.2s">

        Full Stack → Backend

    </text>

</svg>
'''


OUTPUT_FILE.write_text(
    svg,
    encoding="utf-8"
)

print(f"Done! Created: {OUTPUT_FILE}")