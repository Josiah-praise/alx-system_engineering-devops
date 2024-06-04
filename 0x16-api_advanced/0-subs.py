import requests

def get_subreddit_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; SubredditSubscriberCounter/1.0)"}

    response = requests.get(url, headers=headers)

    data = response.json()
    if 'subsribers' in data['data']:
        return data['data']['subscribers']
    else:
        return 0
