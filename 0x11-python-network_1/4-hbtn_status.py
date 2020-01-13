#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    ans = requests.get(url)
    print(ans.text)
    print('Body response:')
    print('\t- type: {}'.format(type(ans.text)))
    print('\t- content: {}'.format(ans.text))
