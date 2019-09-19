#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        winner = {'name': '', 'score': 0}
        for key, value in a_dictionary.items():
            if value > winner['score']:
                winner.update({'name': key, 'score': value})
            else:
                pass
        return winner['name']
