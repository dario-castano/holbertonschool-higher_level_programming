#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        ans = a / b
    except (ZeroDivisionError, TypeError, ValueError):
        return None
    finally:
        if b == 0:
            ans = None
        else:
            ans = a / b
        print("Inside result: {}".format(ans))
    return ans
