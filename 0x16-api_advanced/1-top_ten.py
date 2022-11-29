#!/usr/bin/python3
'''prints titles of first 10 hot posts listed for a given subreddit'''
from requests import get


def top_ten(subreddit):
    '''
    Description:
        - queries Reddit API to print first 10 host posts
    Output:
        - Success: prints first 10 host posts listed
          for a given subreddit
        - Failure: print None
    '''
    endpoint = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'limit': 10}
    res = get(endpoint, headers=headers, allow_redirects=False, params=params)

    if res.status_code != 200:
        print(None)
        return

    top_10 = res.json()['data']['children']
    [print(post['data']['title']) for post in top_10]
