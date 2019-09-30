#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    k = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            k += 1
        except (TypeError, ValueError):
            i -= 1
    print()
    return k