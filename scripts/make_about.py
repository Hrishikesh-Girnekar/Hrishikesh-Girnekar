from pathlib import Path

OUTPUT_FILE = Path("about.svg")

WIDTH = 1000
HEIGHT = 300

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
            animation:
                reveal 0.6s ease-out forwards;
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

        .text {{
            font-family: monospace;
            font-size: 14px;
            fill: #8b949e;
        }}

        .value {{
            font-family: monospace;
            font-size: 14px;
            fill: #f0f6fc;
        }}

        .accent {{
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


    <!-- Section label -->

    <text
        x="42"
        y="42"
        class="label fade"
        style="animation-delay: 0.1s">

        01 / ABOUT

    </text>


    <!-- Heading -->

    <text
        x="42"
        y="82"
        class="heading fade"
        style="animation-delay: 0.2s">

        Who I am

    </text>


    <!-- Introduction -->

    <text
        x="42"
        y="120"
        class="text fade"
        style="animation-delay: 0.35s">

        I'm a backend-focused developer who enjoys turning

    </text>

    <text
        x="42"
        y="145"
        class="text fade"
        style="animation-delay: 0.4s">

        real-world problems into clean, reliable applications.

    </text>


    <!-- Focus -->

    <text
        x="42"
        y="190"
        class="label fade"
        style="animation-delay: 0.55s">

        CURRENT FOCUS

    </text>

    <text
        x="42"
        y="216"
        class="value fade"
        style="animation-delay: 0.65s">

        Java  •  Spring Boot  •  REST APIs  •  SQL  •  System Design

    </text>


    <!-- Approach -->

    <text
        x="42"
        y="260"
        class="label fade"
        style="animation-delay: 0.8s">

        APPROACH

    </text>

    <text
        x="130"
        y="260"
        class="text fade"
        style="animation-delay: 0.9s">

        Learn → Build → Break → Improve

    </text>


    <!-- Status indicator -->

    <circle
        cx="905"
        cy="254"
        r="5"
        class="accent fade"
        style="animation-delay: 1s"/>

    <text
        x="920"
        y="259"
        class="text fade"
        style="animation-delay: 1s">

        BUILDING

    </text>

</svg>
'''

OUTPUT_FILE.write_text(
    svg,
    encoding="utf-8"
)

print(f"Done! Created: {OUTPUT_FILE}")