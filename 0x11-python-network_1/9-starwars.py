#!/usr/bin/python3
"""
Python script that takes in a string and sends a search
request to the Star Wars API
"""
import sys
import requests

if __name__ == "__main__":
    data = {'search': sys.argv[1] if sys.argv.__len__() > 1 else None}
    url = 'https://swapi.co/api/people/'
    response = requests.get(url, data).json()
    print('Number of results: {}'.format(response.get('count')))
    if response.get('count') > 0:
        resultset = response.get('results')
        for result in resultset:
            print(result.get('name'))
