from pathlib import Path

OUTPUT_FILE = Path("stack.svg")

WIDTH = 1000
HEIGHT = 430

categories = [
    (
        "LANGUAGES",
        ["Java", "JavaScript", "SQL"],
    ),
    (
        "BACKEND",
        ["Spring Boot", "Spring Security", "Hibernate", "REST APIs"],
    ),
    (
        "FRONTEND",
        ["React", "HTML", "CSS"],
    ),
    (
        "DATABASE",
        ["MySQL", "PostgreSQL", "MongoDB"],
    ),
    (
        "CLOUD / DEVOPS",
        ["AWS", "Docker", "Git", "GitHub"],
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
            animation: reveal 0.55s ease-out forwards;
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

        .item {{
            font-family: monospace;
            font-size: 13px;
            fill: #f0f6fc;
        }}

        .dot {{
            fill: #3fb950;
        }}

        .line {{
            stroke: #30363d;
            stroke-width: 1;
        }}

        @keyframes reveal {{
            from {{
                opacity: 0;
                transform: translateY(8px);
            }}

            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

    </style>


    <text
        x="42"
        y="42"
        class="label fade"
        style="animation-delay: 0.1s">

        02 / TECHNOLOGY

    </text>


    <text
        x="42"
        y="82"
        class="heading fade"
        style="animation-delay: 0.2s">

        What I work with

    </text>
'''

# Two-column layout
positions = [
    (42, 130),
    (520, 130),
    (42, 220),
    (520, 220),
    (42, 310),
]

for index, (category, technologies) in enumerate(categories):

    x, y = positions[index]
    delay = 0.35 + index * 0.12

    svg += f'''
    <g
        class="fade"
        style="animation-delay: {delay:.2f}s">

        <text
            x="{x}"
            y="{y}"
            class="label">

            {category}

        </text>
    '''

    for item_index, technology in enumerate(technologies):

        item_x = x + (item_index % 2) * 220
        item_y = y + 30 + (item_index // 2) * 27

        svg += f'''
        <circle
            cx="{item_x}"
            cy="{item_y - 4}"
            r="3"
            class="dot"/>

        <text
            x="{item_x + 12}"
            y="{item_y}"
            class="item">

            {technology}

        </text>
        '''

    svg += '''
    </g>
    '''


svg += '''
    <line
        x1="42"
        y1="390"
        x2="958"
        y2="390"
        class="line"/>

    <text
        x="42"
        y="415"
        class="item fade"
        style="animation-delay: 1s">

        Java → Spring Boot → REST → Database → Cloud

    </text>

</svg>
'''


OUTPUT_FILE.write_text(
    svg,
    encoding="utf-8"
)

print(f"Done! Created: {OUTPUT_FILE}")