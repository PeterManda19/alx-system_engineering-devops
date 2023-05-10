#!/usr/bin/python3
"""
Queries the Reddit API and prints the count of each word in the
titles of the top 100 hot posts of a subreddit matching a given list of words
"""

import re
import requests
import sys


def count_words(subreddit: str, word_list: list[str]):
    """
    Counts the occurrence of each word in the titles of the top 100 hot posts
    of a subreddit that matches a given list of words

    Args:
        subreddit (str): Name of the subreddit to search
        word_list (list): List of words to search for in the titles

    Returns:
        None
    """
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    params = {
        'limit': 100
    }

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print("No results found")
        return

    titles = [post['data']['title'].lower() for post in response.json()['data']['children']]
    counts = {word.lower(): 0 for word in word_list}

    for title in titles:
        for word in counts:
            counts[word] += len(re.findall(rf"\b{word}\b", title))

    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    for word, count in sorted_counts:
        print(f"{word}: {count}")


if __name__ == '__main__':
    count_words(sys.argv[1], sys.argv[2:])
