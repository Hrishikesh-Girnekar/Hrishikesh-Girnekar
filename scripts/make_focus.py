from pathlib import Path

OUTPUT_FILE = Path("focus.svg")

WIDTH = 1000
HEIGHT = 390

focus_items = [
    ("01", "Spring Boot", "Building secure and scalable REST APIs"),
    ("02", "Microservices", "Learning service-based architecture and communication"),
    ("03", "System Design", "Understanding scalable backend architecture"),
    ("04", "DSA", "Improving problem solving and coding fundamentals"),
    ("05", "Docker + AWS", "Learning containerization and cloud deployment"),
    ("06", "Production Projects", "Turning ideas into complete applications"),
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

        .number {{
            font-family: monospace;
            font-size: 12px;
            fill: #3fb950;
            font-weight: bold;
        }}

        .title {{
            font-family: monospace;
            font-size: 14px;
            fill: #f0f6fc;
            font-weight: bold;
        }}

        .description {{
            font-family: monospace;
            font-size: 11px;
            fill: #8b949e;
        }}

        .line {{
            stroke: #30363d;
            stroke-width: 1;
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

        05 / CURRENTLY BUILDING

    </text>


    <text
        x="42"
        y="82"
        class="heading fade"
        style="animation-delay: 0.2s">

        What I'm focused on

    </text>


    <line
        x1="42"
        y1="105"
        x2="958"
        y2="105"
        class="line"/>

'''

for index, (number, title, description) in enumerate(focus_items):

    column = index % 2
    row = index // 2

    x = 42 if column == 0 else 520
    y = 140 + row * 72

    delay = 0.35 + index * 0.12

    svg += f'''
    <g
        class="fade"
        style="animation-delay: {delay:.2f}s">

        <text
            x="{x}"
            y="{y}"
            class="number">

            {number}

        </text>

        <text
            x="{x + 38}"
            y="{y}"
            class="title">

            {title}

        </text>

        <text
            x="{x + 38}"
            y="{y + 22}"
            class="description">

            {description}

        </text>

    </g>
    '''


svg += '''
    <line
        x1="42"
        y1="355"
        x2="958"
        y2="355"
        class="line"/>

    <text
        x="42"
        y="378"
        class="description fade"
        style="animation-delay: 1.2s">

        Learn → Build → Ship → Improve

    </text>

</svg>
'''


OUTPUT_FILE.write_text(
    svg,
    encoding="utf-8"
)

print(f"Done! Created: {OUTPUT_FILE}")