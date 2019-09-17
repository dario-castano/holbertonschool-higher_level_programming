#!/usr/bin/python3
def pad(tup):
    if len(tup) > 2:
        return tup[:2]
    elif len(tup) < 2:
        return tup + ((0,) * (2-len(tup)))
    else:
        return tup


def add_tuple(tuple_a=(), tuple_b=()):
    return tuple(map(sum, zip(pad(tuple_a), pad(tuple_b))))
