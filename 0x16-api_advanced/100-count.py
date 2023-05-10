#!/usr/bin/python3
"""
Queries the Reddit API and prints the
count of each word in the
titles of the top 100 hot posts of a
subreddit matching a given list of words
"""

import re
import requests
import sys


def count_words(subreddit: str, word_list: list[str],
                count_dict=None, after=None):
    """
    Counts the occurrence of each word in the titles
    of the top 100 hot posts
    of a subreddit that matches a given list of words

    Args:
        subreddit (str): Name of the subreddit to
        search
        word_list (list): List of words to search for
        in the titles
        count_dict (dict): Dictionary to store the
        word counts
        after (str): Value of the 'after' parameter
        in the Reddit API response

    Returns:
        None
    """

    if count_dict is None:
        count_dict = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}

    if after is not None:
        params['after'] = after

    response = requests.get(
        url, headers=headers, params=params)
    response.raise_for_status()

    titles = [
        post[
            'data'
            ][
                'title'
                ].lower() for post in response.json()[
                    'data'
                    ][
                        'children'
                        ]
        ]

    for title in titles:
        for word in count_dict:
            count_dict[word] += len(
                re.findall(rf"\b{word}\b", title))

    if len(response.json()['data']['children']) == 0:
        sorted_counts = sorted(
            count_dict.items(), key=lambda x: x[1], reverse=True)
        for word, count in sorted_counts:
            print(f"{word}: {count}")
        return

    after = response.json()['data']['after']
    count_words(subreddit, word_list, count_dict, after)


if __name__ == '__main__':
    count_words(sys.argv[1], sys.argv[2:])
