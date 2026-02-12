#!/usr/bin/python3
"""
Task 2: Consuming and processing data from an API using Python
"""

import csv
import requests


POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts and print status code + titles."""
    try:
        response = requests.get(POSTS_URL, timeout=10)
    except requests.RequestException:
        # If network error happens, still print something predictable
        print("Status Code: 0")
        return

    print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        return

    try:
        posts = response.json()
    except ValueError:
        return

    for post in posts:
        title = post.get("title", "")
        print(title)


def fetch_and_save_posts():
    """Fetch posts and save selected fields to posts.csv."""
    try:
        response = requests.get(POSTS_URL, timeout=10)
    except requests.RequestException:
        return

    if response.status_code != 200:
        return

    try:
        posts = response.json()
    except ValueError:
        return

    rows = []
    for post in posts:
        rows.append({
            "id": post.get("id"),
            "title": post.get("title"),
            "body": post.get("body"),
        })

    fieldnames = ["id", "title", "body"]
    with open("posts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
