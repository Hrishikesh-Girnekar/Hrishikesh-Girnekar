from pathlib import Path
from collections import Counter

import requests


USERNAME = "Hrishikesh-Girnekar"

OUTPUT_FILE = Path("languages.svg")

WIDTH = 1000
HEIGHT = 430

API_URL = (
    f"https://api.github.com/users/{USERNAME}/repos"
    "?per_page=100&sort=updated"
)


print("Fetching GitHub repositories...")

response = requests.get(
    API_URL,
    headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-profile-generator",
    },
    timeout=30,
)

response.raise_for_status()

repositories = response.json()

print(f"Found {len(repositories)} public repositories.")


# --------------------------------------------------
# Collect language bytes from every repository
# --------------------------------------------------

language_bytes = Counter()

for repository in repositories:

    if repository.get("fork"):
        continue

    repo_name = repository["name"]

    print(f"Reading languages: {repo_name}")

    language_url = repository["languages_url"]

    language_response = requests.get(
        language_url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "github-profile-generator",
        },
        timeout=30,
    )

    if language_response.status_code != 200:
        print(
            f"  Skipping {repo_name}: "
            f"HTTP {language_response.status_code}"
        )
        continue

    language_data = language_response.json()

    for language, byte_count in language_data.items():
        language_bytes[language] += byte_count


if not language_bytes:
    raise RuntimeError(
        "No language data was found in your repositories."
    )


# --------------------------------------------------
# Convert bytes to percentages
# --------------------------------------------------

total_bytes = sum(language_bytes.values())

languages = []

for language, byte_count in language_bytes.most_common():

    percentage = (
        byte_count
        / total_bytes
        * 100
    )

    languages.append(
        {
            "name": language,
            "percentage": percentage,
        }
    )


print()
print("Languages detected:")

for language in languages:
    print(
        f"  {language['name']}: "
        f"{language['percentage']:.1f}%"
    )


# --------------------------------------------------
# Generate SVG
# --------------------------------------------------

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

        .name {{
            font-family: monospace;
            font-size: 14px;
            fill: #f0f6fc;
            font-weight: bold;
        }}

        .percentage {{
            font-family: monospace;
            font-size: 12px;
            fill: #8b949e;
        }}

        .bar-background {{
            fill: #161b22;
        }}

        .bar {{
            fill: #3fb950;
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

        06 / LANGUAGES

    </text>


    <text
        x="42"
        y="82"
        class="heading fade"
        style="animation-delay: 0.2s">

        Languages I've worked with

    </text>
'''


# Show the top 8 languages.
display_languages = [
    language
    for language in languages
    if language["name"] != "Dockerfile"
][:7]

bar_x = 230
bar_width = 500
row_height = 38
start_y = 125

for index, language in enumerate(display_languages):

    y = start_y + index * row_height

    delay = 0.35 + index * 0.08

    percentage = language["percentage"]

    filled_width = (
        bar_width
        * percentage
        / 100
    )

    svg += f'''
    <g
        class="fade"
        style="animation-delay: {delay:.2f}s">

        <text
            x="52"
            y="{y + 10}"
            class="name">

            {language["name"]}

        </text>


        <rect
            x="{bar_x}"
            y="{y}"
            width="{bar_width}"
            height="12"
            rx="6"
            class="bar-background"/>


        <rect
            x="{bar_x}"
            y="{y}"
            width="{filled_width:.1f}"
            height="12"
            rx="6"
            class="bar"/>


        <text
            x="755"
            y="{y + 10}"
            class="percentage">

            {percentage:.1f}%

        </text>

    </g>
    '''


svg += '''
    <line
        x1="42"
        y1="425"
        x2="958"
        y2="425"
        class="line"/>

</svg>
'''


OUTPUT_FILE.write_text(
    svg,
    encoding="utf-8"
)

print()
print(f"Done! Created: {OUTPUT_FILE}")