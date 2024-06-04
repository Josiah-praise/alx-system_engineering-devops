#!/usr/bin/python3
'''
Gets the title of all hot articles of a subreddit
'''


def recurse(
    subreddit: str,
    hot_list: list = [],
    after: str | None = ''
) -> list:
    '''
    returns a list of all the titles of all hot posts of a subreddit
    '''

    import requests

    if not isinstance(subreddit, str) or not isinstance(hot_list, list):
        return None

    if after is None:
        return hot_list
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?after='
        header = {'User-Agent': 'Praise chromium engine'}
        response = requests.get(
            url=url+after,
            headers=header,
            allow_redirects=False
            ).json()

        try:
            after = response['data']['after']

            for post in response['data']['children']:
                hot_list.append(post['data']['title'])
            return recurse(subreddit, hot_list, after)
        except Exception as e:
            return None
