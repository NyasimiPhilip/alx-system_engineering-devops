#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            children = data.get("data", {}).get("children", [])
            for child in children:
                title = child.get("data", {}).get("title", "")
                if title:
                    print(title)
        elif response.status_code == 404:
            return
    except requests.RequestException:
        return