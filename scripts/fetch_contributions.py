from pathlib import Path
import json
import re
from datetime import date, timedelta

import requests
from bs4 import BeautifulSoup


USERNAME = "Hrishikesh-Girnekar"

URL = f"https://github.com/users/{USERNAME}/contributions"

OUTPUT_FILE = Path("data/contributions.json")


print("Fetching GitHub contributions...")
print(f"User: {USERNAME}")

response = requests.get(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

response.raise_for_status()

print("GitHub page downloaded successfully.")

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

days = []

for rect in soup.select("td.ContributionCalendar-day"):
    contribution_date = rect.get("data-date")
    level = rect.get("data-level")

    if not contribution_date or level is None:
        continue

    days.append(
        {
            "date": contribution_date,
            "level": int(level),
        }
    )


if not days:
    raise RuntimeError(
        "No contribution data found. "
        "GitHub may have changed its HTML structure."
    )


print(f"Found {len(days)} contribution days.")


# --------------------------------------------------
# Contribution totals
# --------------------------------------------------

total_contributions = 0

for day in days:
    label = day["level"]

    # GitHub levels represent contribution intensity.
    # We keep the level itself for the heatmap.
    total_contributions += label


# --------------------------------------------------
# Current streak
# --------------------------------------------------

contribution_dates = {
    day["date"]
    for day in days
    if day["level"] > 0
}


today = date.today()

current_streak = 0
check_date = today

while check_date.isoformat() in contribution_dates:
    current_streak += 1
    check_date -= timedelta(days=1)


# --------------------------------------------------
# Longest streak
# --------------------------------------------------

longest_streak = 0
running_streak = 0

for day in days:
    if day["level"] > 0:
        running_streak += 1
        longest_streak = max(
            longest_streak,
            running_streak
        )
    else:
        running_streak = 0


# --------------------------------------------------
# Best day
# --------------------------------------------------

best_day = max(
    days,
    key=lambda day: day["level"]
)


# --------------------------------------------------
# Monthly totals
# --------------------------------------------------

monthly_totals = {}

for day in days:
    month = day["date"][:7]

    monthly_totals.setdefault(
        month,
        0
    )

    monthly_totals[month] += day["level"]


# --------------------------------------------------
# Save data
# --------------------------------------------------

output = {
    "username": USERNAME,
    "days": days,
    "stats": {
        "current_streak": current_streak,
        "longest_streak": longest_streak,
        "best_day": best_day,
        "monthly_totals": monthly_totals,
    },
}


OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

OUTPUT_FILE.write_text(
    json.dumps(
        output,
        indent=2
    ),
    encoding="utf-8"
)


print()
print("Done!")
print(f"Created: {OUTPUT_FILE}")
print(f"Current streak: {current_streak}")
print(f"Longest streak: {longest_streak}")
print(f"Best contribution level: {best_day['level']}")