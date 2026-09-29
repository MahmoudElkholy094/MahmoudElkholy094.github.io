import json
import requests

ORCID_ID = "0000-0003-3615-3714"

url = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"

headers = {
    "Accept": "application/json"
}

response = requests.get(url, headers=headers, timeout=30)
response.raise_for_status()

data = response.json()

publications = []

for item in data.get("group", []):
    work = item.get("work-summary", [{}])[0]

    title = (
        work.get("title", {})
        .get("title", {})
        .get("value", "Untitled")
    )

    year = (
        work.get("publication-date", {})
        .get("year", {})
        .get("value", "")
    )

    publications.append({
        "title": title,
        "year": year
    })


with open("publications.json", "w", encoding="utf-8") as f:
    json.dump(
        publications,
        f,
        indent=2,
        ensure_ascii=False
    )

print("Updated publications:", len(publications))
