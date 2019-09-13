#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        try:
            a = int(argv[1])
            operator = argv[2]
            b = int(argv[3])
        except ValueError:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)

        if ord(operator) == 43:
            print(add(a, b))
        elif ord(operator) == 45:
            print(sub(a, b))
        elif ord(operator) == 42:
            print(mul(a, b))
        elif ord(operator) == 47:
            print(div(a, b))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
