#!/usr/bin/python3
def best_score(a_dictionary):
    try:
        winner = {'name': '', 'score': 0}
        for key, value in a_dictionary.items():
            if value > winner['score']:
                winner.update({'name': key, 'score': value})
            else:
                pass
        return winner['name']
    except AttributeError:
        return None
