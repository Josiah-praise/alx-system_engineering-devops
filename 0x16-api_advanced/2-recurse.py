#!/usr/bin/python3
'''
Gets the title of all hot articles of a subreddit
'''
import requests


def recurse(subreddit: str, hot_list: list = [], after: str = None) -> list:
    '''
    returns a list of all the titles of all hot posts of a subreddit
    '''
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Praise chromium engine'}
    params = {'after': after} if after else {}

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            after = data.get('after')
            for post in data.get('children', []):
                hot_list.append(post['data']['title'])
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
    return None
