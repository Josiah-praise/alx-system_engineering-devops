#!/usr/bin/python3
'''
Fetches the top 10 hot posts of a subreddit
'''


def top_ten(subreddit: str) -> list:
    import requests

    if subreddit is not None and isinstance(subreddit, str):
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        user_agent = "Mozilla/5.0 (compatible; SubredditSubscriberCounter/1.0)"
        headers = {"User-Agent": user_agent}

        response = requests.get(
            url=url,
            headers=headers,
            allow_redirects=False
            )

        try:
            posts = response.json()['data']['children']

            for post in posts[:10]:
                print(post['data']['title'])
        except Exception as e:
            print(None)
