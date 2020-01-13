#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
