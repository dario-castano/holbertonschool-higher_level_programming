#!/usr/bin/python3
"""
Advanced task 1
"""
import sys
import requests

if __name__ == "__main__":
    url = 'https://api.github.com'
    if sys.argv.__len__() >= 2:
        repo = sys.argv[1]
        owner = sys.argv[2]
        resource = '{}/repos/{}/{}/commits'.format(url, owner, repo)
        response = requests.get(resource).json()
        filtered = response[0:10]
        for elem in filtered:
            print('{} : {}'.format(elem['sha'], elem['commit']['author']['name']))
