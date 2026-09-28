import requests
import json
import os
import time
from datetime import datetime

# Hacker News API headers
headers = {
    "User-Agent": "TrendPulse/1.0"
}

# Categories and their keywords
categories = {
    "technology": ["AI", "software", "tech", "code", "computer",
                   "data", "cloud", "API", "GPU", "LLM"],

    "worldnews": ["war", "government", "country", "president",
                  "election", "climate", "attack", "global"],

    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team",
               "player", "league", "championship"],

    "science": ["research", "study", "space", "physics", "biology",
                "discovery", "NASA", "genome"],

    "entertainment": ["movie", "film", "music", "Netflix", "game",
                      "book", "show", "award", "streaming"]
}


# Find a category by checking keywords in the title
def find_category(title):
    title = title.lower()

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword.lower() in title:
                return category

    return None


# Step 1: Get top 500 story IDs
try:
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    story_ids = response.json()[:500]

except requests.RequestException as error:
    print("Error fetching story IDs:", error)
    exit()


# Keep track of how many stories we have in each category
category_count = {
    "technology": 0,
    "worldnews": 0,
    "sports": 0,
    "science": 0,
    "entertainment": 0
}

stories = []


# Step 2: Fetch individual stories
for story_id in story_ids:

    # Stop when we have 25 stories in every category
    if all(count == 25 for count in category_count.values()):
        break

    story_url = (
        f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    )

    try:
        response = requests.get(
            story_url,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()

        story = response.json()

    except requests.RequestException as error:
        print(f"Failed to fetch story {story_id}: {error}")
        continue

    # Ignore deleted stories and non-story items
    if not story or story.get("type") != "story":
        continue

    title = story.get("title", "")

    # Find the category using the title
    category = find_category(title)

    # Ignore stories that don't match any category
    if category is None:
        continue

    # Maximum 25 stories per category
    if category_count[category] >= 25:
        continue

    # Store the required fields
    story_data = {
        "post_id": story.get("id"),
        "title": title,
        "category": category,
        "score": story.get("score", 0),
        "num_comments": story.get("descendants", 0),
        "author": story.get("by", ""),
        "collected_at": datetime.now().isoformat()
    }

    stories.append(story_data)

    category_count[category] += 1

    print(
        f"{category}: "
        f"{category_count[category]}/25 - {title}"
    )

    # Wait 2 seconds when a category reaches 25 stories
    if category_count[category] == 25:
        print(f"Finished collecting {category}.")
        time.sleep(2)


# Step 3: Create data folder
os.makedirs("data", exist_ok=True)


# Step 4: Create today's JSON filename
date = datetime.now().strftime("%Y%m%d")
filename = f"data/trends_{date}.json"


# Step 5: Save stories to JSON
with open(filename, "w", encoding="utf-8") as file:
    json.dump(stories, file, indent=4, ensure_ascii=False)


# Step 6: Print final result
print()
print("=" * 50)
print(f"Collected {len(stories)} stories.")
print(f"Saved to {filename}")
print("=" * 50)