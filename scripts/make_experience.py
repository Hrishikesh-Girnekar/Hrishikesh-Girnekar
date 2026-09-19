from pathlib import Path

OUTPUT_FILE = Path("experience.svg")

WIDTH = 1000
HEIGHT = 360

experience = [
    {
        "period": "DEC 2025 — MAY 2026",
        "role": "Associate Software Engineer Intern",
        "company": "Thynktech India Pvt. Ltd.",
        "work": "Java 17  •  Spring Boot  •  REST APIs  •  Microservices",
    },
    {
        "period": "PREVIOUS EXPERIENCE",
        "role": "IT / Software Engineering",
        "company": "Technical &amp; software development experience",
        "work": "Backend development  •  Full-stack applications  •  Problem solving",
    },
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

        .period {{
            font-family: monospace;
            font-size: 11px;
            fill: #3fb950;
            font-weight: bold;
        }}

        .role {{
            font-family: monospace;
            font-size: 16px;
            fill: #f0f6fc;
            font-weight: bold;
        }}

        .company {{
            font-family: monospace;
            font-size: 12px;
            fill: #8b949e;
        }}

        .work {{
            font-family: monospace;
            font-size: 12px;
            fill: #f0f6fc;
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

        04 / EXPERIENCE

    </text>

    <text
        x="42"
        y="82"
        class="heading fade"
        style="animation-delay: 0.2s">

        Where I've worked

    </text>

    <!-- Timeline -->

    <line
        x1="72"
        y1="120"
        x2="72"
        y2="315"
        class="line"/>

'''

for index, item in enumerate(experience):

    y = 130 + index * 95
    delay = 0.4 + index * 0.2

    svg += f'''
    <g
        class="fade"
        style="animation-delay: {delay:.2f}s">

        <circle
            cx="72"
            cy="{y}"
            r="6"
            class="dot"/>

        <text
            x="100"
            y="{y - 8}"
            class="period">

            {item["period"]}

        </text>

        <text
            x="100"
            y="{y + 17}"
            class="role">

            {item["role"]}

        </text>

        <text
            x="100"
            y="{y + 39}"
            class="company">

            {item["company"]}

        </text>

        <text
            x="100"
            y="{y + 61}"
            class="work">

            {item["work"]}

        </text>

    </g>
    '''

svg += '''
</svg>
'''

OUTPUT_FILE.write_text(
    svg,
    encoding="utf-8"
)

print(f"Done! Created: {OUTPUT_FILE}")