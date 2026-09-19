from pathlib import Path

OUTPUT_FILE = Path("projects.svg")

WIDTH = 1000
HEIGHT = 610

projects = [
    {
        "number": "01",
        "name": "Fisheries Management Platform",
        "description": "A scalable platform for managing fisheries operations, boats, fishermen, traders and buyers.",
        "stack": "Java  •  Spring Boot  •  React  •  PostgreSQL",
        "type": "Enterprise / Microservices",
    },
    {
        "number": "02",
        "name": "FoodDash",
        "description": "A full-stack food delivery application with authentication, restaurants, orders and payments.",
        "stack": "React  •  Node.js  •  Express  •  MongoDB",
        "type": "Full Stack Application",
    },
    {
        "number": "03",
        "name": "Wanderlust",
        "description": "An Airbnb-style platform for discovering, listing and managing travel properties.",
        "stack": "React  •  Node.js  •  Express  •  MongoDB",
        "type": "Full Stack Application",
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

        .project-number {{
            font-family: monospace;
            font-size: 12px;
            fill: #58a6ff;
            font-weight: bold;
        }}

        .project-name {{
            font-family: monospace;
            font-size: 17px;
            fill: #f0f6fc;
            font-weight: bold;
        }}

        .description {{
            font-family: monospace;
            font-size: 12px;
            fill: #8b949e;
        }}

        .stack {{
            font-family: monospace;
            font-size: 12px;
            fill: #f0f6fc;
        }}

        .type {{
            font-family: monospace;
            font-size: 11px;
            fill: #3fb950;
        }}

        .line {{
            stroke: #30363d;
            stroke-width: 1;
        }}

        @keyframes reveal {{
            from {{
                opacity: 0;
                transform: translateY(10px);
            }}

            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

    </style>


    <!-- Section heading -->

    <text
        x="42"
        y="42"
        class="label fade"
        style="animation-delay: 0.1s">

        03 / PROJECTS

    </text>

    <text
        x="42"
        y="82"
        class="heading fade"
        style="animation-delay: 0.2s">

        Things I've built

    </text>
'''


# --------------------------------------------------
# Project cards
# --------------------------------------------------

card_y_positions = [115, 275, 435]

for index, project in enumerate(projects):

    y = card_y_positions[index]

    delay = 0.35 + index * 0.2

    svg += f'''
    <g
        class="fade"
        style="animation-delay: {delay:.2f}s">

        <!-- Card -->

        <rect
            x="42"
            y="{y}"
            width="916"
            height="135"
            rx="12"
            fill="#161b22"
            stroke="#30363d"
            stroke-width="1"/>


        <!-- Project number -->

        <text
            x="62"
            y="{y + 27}"
            class="project-number">

            {project["number"]}

        </text>


        <!-- Project name -->

        <text
            x="105"
            y="{y + 27}"
            class="project-name">

            {project["name"]}

        </text>


        <!-- Project type -->

        <text
            x="925"
            y="{y + 26}"
            text-anchor="end"
            class="type">

            {project["type"]}

        </text>


        <!-- Description -->

        <text
            x="62"
            y="{y + 58}"
            class="description">

            {project["description"]}

        </text>


        <!-- Stack -->

        <text
            x="62"
            y="{y + 91}"
            class="stack">

            {project["stack"]}

        </text>


        <!-- Project command -->

        <text
            x="62"
            y="{y + 117}"
            class="description">

            $ project.status → completed / evolving

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