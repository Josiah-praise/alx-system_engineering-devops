#!/usr/bin/python3
'''
Gets the number of subscribers to a subreddit
'''

import requests


def number_of_subscribers(subreddit: str) -> int:
    """Uses reddit api to get information about a subreddit

    Args:
        subreddit: name of subreddit

    Returns:
        int: number of subscribers to the given subreddit
    """

    if subreddit is not None and isinstance(subreddit, str):
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        user_agent = "Mozilla/5.0 (compatible; SubredditSubscriberCounter/1.0)"
        headers = {"User-Agent": user_agent}

        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json()
        try:
            return data['data']['subscribers']
        except Exception as e:
            return 0
    return 0
