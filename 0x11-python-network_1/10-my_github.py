#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import sys
import requests

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1] if sys.argv.__len__() >= 1 else ""
    password = sys.argv[2] if sys.argv.__len__() >= 2 else ""
    auth = (username, password)
    response = requests.get(url, auth=auth).json()
    if 'id' in response:
        print(response.get('id'))
    else:
        print('None')
