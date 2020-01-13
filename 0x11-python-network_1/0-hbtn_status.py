#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        ans = response.read()
        print('Body response:')
        print('    - type: {}'.format(type(ans)))
        print('    - content: {}'.format(ans))
        print('    - utf8 content: {}'.format(ans.decode('utf-8')))
