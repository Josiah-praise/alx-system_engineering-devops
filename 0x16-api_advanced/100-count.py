#!/usr/bin/python3
'''

'''

import requests
from typing import Any


def do_keyword_count(word_to_count: dict[str, int], title: str) -> None:
    '''
    counts the occurences of the keys from word_to_dict in title
    and updates word_to_dict accordingly
    '''
    list_of_words = [word.lower() for word in title.split()]
    for each in list_of_words:
        if each in word_to_count:
            word_to_count[each] += 1


def getWordCount(posts: list[dict[Any, Any]],
                 word_to_count: dict[str, int]) -> None:
    '''
    calculates the word count for a given post
    '''

    for post in posts:
        do_keyword_count(word_to_count, post['data']['title'])


def printWordCount(count: int, wordCount: dict[str, int]) -> None:
    '''
    prints out result as <word> <count>
    results are printed in descending order, by the count,
    and if the count is the same for separate keywords,
    they are sorted alphabetically (ascending, from A to Z).
    Words with no matches are skipped and not printed.
    Words are printed in lowercase.
    '''
    if count == 0:
        # Filter out words with no matches
        filtered_word_count = {word: cnt for word,
                               cnt in wordCount.items() if cnt > 0}

        # Sort the dictionary by values in descending order
        # and by keys in ascending order if values are the same
        sorted_word_count = sorted(
            filtered_word_count.items(), key=lambda item: (-item[1], item[0]))

        # Print the sorted words with their counts
        for word, cnt in sorted_word_count:
            print(f"{word} {cnt}")


def count_words(subreddit: str,
                word_list: list[str],
                after: str | None = None,
                count: int = 0) -> dict[str, int]:
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {"after": after} if after else {}
    header = {"User-Agent": "Praise Chromium Engine Lol"}

    # default dict of keyword list
    wordCount: dict[str, int] = {key.lower(): 0 for key in word_list}

    response = requests.get(url=url, params=params,
                            headers=header, allow_redirects=False)

    # check for successful json response
    if response.status_code == 200:
        after = response.json().get('data').get('after')
        posts: list[dict[Any, Any]] = response.json().get(
            'data').get('children')
        getWordCount(posts, wordCount)

        otherPagesWordCount = None

        # check if there's a next page
        if after:
            otherPagesWordCount = count_words(
                subreddit, word_list, after, count=count + 1)
        else:
            return wordCount

        if otherPagesWordCount:
            for key, value in otherPagesWordCount.items():
                wordCount[key] += value
        printWordCount(count, wordCount)
        return wordCount
    return {}
