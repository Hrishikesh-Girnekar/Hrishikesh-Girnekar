from pathlib import Path
import json
from datetime import date, timedelta


INPUT_FILE = Path("data/contributions.json")
OUTPUT_FILE = Path("contrib-heatmap.svg")


WIDTH = 860
HEIGHT = 260

CELL_SIZE = 12
CELL_GAP = 3

LEFT = 40
TOP = 38

PALETTE = [
    "#161b22",
    "#0e4429",
    "#006d32",
    "#26a641",
    "#39d353",
    "#69f0a0",
]


if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"Could not find {INPUT_FILE}. "
        "Run fetch_contributions.py first."
    )


print("Loading contribution data...")

data = json.loads(
    INPUT_FILE.read_text(
        encoding="utf-8"
    )
)

days = data["days"]
stats = data["stats"]


contributions = {
    item["date"]: item["level"]
    for item in days
}


# --------------------------------------------------
# Build the last 53 weeks
# --------------------------------------------------

today = date.today()

# Move backwards to Sunday.
start = today - timedelta(
    days=(today.weekday() + 1) % 7
)

start -= timedelta(
    weeks=52
)


weeks = []

for week in range(53):
    current_week = []

    for day in range(7):
        current_date = (
            start
            + timedelta(
                weeks=week,
                days=day
            )
        )

        current_week.append(
            (
                current_date,
                contributions.get(
                    current_date.isoformat(),
                    0
                )
            )
        )

    weeks.append(current_week)


print("Creating animated heatmap...")


svg = f'''<svg
    xmlns="http://www.w3.org/2000/svg"
    width="{WIDTH}"
    height="{HEIGHT}"
    viewBox="0 0 {WIDTH} {HEIGHT}">

    <rect
        width="100%"
        height="100%"
        rx="14"
        fill="#0d1117"
        stroke="#30363d"
        stroke-width="2"/>

    <style>

        .cell {{
            opacity: 0;
            animation:
                appear 0.35s ease-out
                forwards;
        }}

        @keyframes appear {{

            from {{
                opacity: 0;
                transform: scale(0.4);
            }}

            to {{
                opacity: 1;
                transform: scale(1);
            }}

        }}

        .title {{
            font-family: monospace;
            font-size: 14px;
            fill: #f0f6fc;
            font-weight: bold;
        }}

        .subtitle {{
            font-family: monospace;
            font-size: 11px;
            fill: #8b949e;
        }}

        .stat {{
            font-family: monospace;
            font-size: 11px;
            fill: #8b949e;
        }}

    </style>

    <text
        x="20"
        y="24"
        class="title">
        hrishi@github ~ $ ./contributions.sh
    </text>

    <text
        x="{WIDTH - 20}"
        y="24"
        text-anchor="end"
        class="subtitle">
        {stats["current_streak"]} day streak
    </text>
'''


# --------------------------------------------------
# Draw contribution cells
# --------------------------------------------------

for week_index, week in enumerate(weeks):

    for day_index, (current_date, level) in enumerate(week):

        x = (
            LEFT
            + week_index
            * (CELL_SIZE + CELL_GAP)
        )

        y = (
            TOP
            + day_index
            * (CELL_SIZE + CELL_GAP)
        )

        # Stagger animation diagonally.
        delay = (
            week_index * 0.025
            + day_index * 0.035
        )

        fill = PALETTE[
            min(level, len(PALETTE) - 1)
        ]

        svg += f'''
        <rect
            class="cell"
            x="{x}"
            y="{y}"
            width="{CELL_SIZE}"
            height="{CELL_SIZE}"
            rx="2"
            fill="{fill}"
            style="
                animation-delay:
                {delay:.3f}s;
            ">
            <title>
                {current_date.isoformat()}
                — level {level}
            </title>
        </rect>
        '''


# --------------------------------------------------
# Stats footer
# --------------------------------------------------

footer_y = 145

svg += f'''
    <line
        x1="20"
        y1="150"
        x2="{WIDTH - 20}"
        y2="150"
        stroke="#30363d"
        stroke-width="1"/>

    <text
        x="20"
        y="{footer_y + 25}"
        class="stat">
        CURRENT STREAK
    </text>

    <text
        x="20"
        y="{footer_y + 42}"
        class="title">
        {stats["current_streak"]} days
    </text>


    <text
        x="190"
        y="{footer_y + 25}"
        class="stat">
        LONGEST STREAK
    </text>

    <text
        x="190"
        y="{footer_y + 42}"
        class="title">
        {stats["longest_streak"]} days
    </text>


    <text
        x="360"
        y="{footer_y + 25}"
        class="stat">
        BEST DAY
    </text>

    <text
        x="360"
        y="{footer_y + 42}"
        class="title">
        level {stats["best_day"]["level"]}
    </text>


    <text
        x="530"
        y="{footer_y + 25}"
        class="stat">
        CONTRIBUTION DAYS
    </text>

    <text
        x="530"
        y="{footer_y + 42}"
        class="title">
        {sum(1 for d in days if d["level"] > 0)}
    </text>


    <text
        x="20"
        y="220"
        class="subtitle">
        Less
    </text>
'''


# --------------------------------------------------
# Legend
# --------------------------------------------------

legend_x = 58

for level in range(6):

    x = (
        legend_x
        + level
        * (CELL_SIZE + CELL_GAP)
    )

    svg += f'''
    <rect
        x="{x}"
        y="211"
        width="{CELL_SIZE}"
        height="{CELL_SIZE}"
        rx="2"
        fill="{PALETTE[level]}"/>
    '''


svg += f'''
    <text
        x="{legend_x + 95}"
        y="220"
        class="subtitle">
        More
    </text>

</svg>
'''


OUTPUT_FILE.write_text(
    svg,
    encoding="utf-8"
)


print(
    f"Done! Created: {OUTPUT_FILE}"
)