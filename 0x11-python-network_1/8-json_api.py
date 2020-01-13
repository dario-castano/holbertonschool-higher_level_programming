#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    data = {"q": sys.argv[1] if sys.argv.__len__() >= 2 else ""}
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data)
    try:
        json_data = response.json()
        if not json_data:
            print('No result')
        else:
            print('[{}] {}'.format(json_data.get('id'), json_data.get('name')))
    except ValueError:
        print('Not a valid JSON')
