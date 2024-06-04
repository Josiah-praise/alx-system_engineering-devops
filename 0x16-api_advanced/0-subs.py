'''
Gets the number of subscribers to a subreddit
'''

import requests


def get_subreddit_subscribers(subreddit: str) -> int:
    """Uses reddit api to get information about a subreddit

    Args:
        subreddit: name of subreddit

    Returns:
        int: number of subscribers to the given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = "Mozilla/5.0 (compatible; SubredditSubscriberCounter/1.0)"
    headers = {"User-Agent": user_agent}

    response = requests.get(url, headers=headers)

    data = response.json()
    if 'subsribers' in data['data']:
        return data['data']['subscribers']
    else:
        return 0
