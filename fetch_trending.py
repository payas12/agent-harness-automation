import urllib.request
import json
import sys
from datetime import datetime, timedelta

# Find repositories created in the last 30 days, sorted by stars descending
date_30_days_ago = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
url = f"https://api.github.com/search/repositories?q=created:>{date_30_days_ago}&sort=stars&order=desc&per_page=5"

headers = {
    "User-Agent": "Python-Trending-Repos-Script",
    "Accept": "application/vnd.github.v3+json"
}

req = urllib.request.Request(url, headers=headers)

try:
    # Explicit timeout prevents indefinite hanging
    with urllib.request.urlopen(req, timeout=15) as response:
        data = json.loads(response.read().decode('utf-8'))
        
    items = data.get('items', [])
    
    trending_repos = []
    for item in items:
        repo_info = {
            "name": item.get("full_name"),
            "stars": item.get("stargazers_count"),
            "description": item.get("description") or "No description provided",
            "url": item.get("html_url")
        }
        trending_repos.append(repo_info)
        
    output_filename = "trending_repos.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(trending_repos, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully saved top {len(trending_repos)} trending repositories to '{output_filename}'.\n")
    
    print("| Repository | Stars | Description |")
    print("| --- | --- | --- |")
    for repo in trending_repos:
        desc = repo['description'].replace('|', '\\|').replace('\n', ' ')
        name_link = f"[{repo['name']}]({repo['url']})"
        print(f"| {name_link} | {repo['stars']:,} | {desc} |")

except Exception as e:
    print(f"Error fetching trending repositories: {e}", file=sys.stderr)
    sys.exit(1)
