#!/usr/bin/python3
"""Fetch and compile a list of trending posts in a Reddit community."""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Retrieve and gather titles of trending posts from a specified subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "custom-reddit-trending-fetcher:v1.0.0 (by /u/your_username)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")
    for item in data.get("children"):
        hot_list.append(item.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
