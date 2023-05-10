#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    if len(sys.argv) < 2:
        print("Please enter a subreddit name")
        return
    url = "https://www.reddit.com/r/{}/hot.json".format(
        subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get(
                'data').get('children')
            for i in range(10):
                print(children[i].get('data').get(
                    'title'))
        else:
            print("None")
    except Exception:
        print("None")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please enter a subreddit name")
    else:
        top_ten(sys.argv[1])
