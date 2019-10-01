#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        answer = fct(*args)
    except Exception as e:
        answer = None
        sys.stderr.write('Exception: ' + str(e) + '\n')
        return answer
