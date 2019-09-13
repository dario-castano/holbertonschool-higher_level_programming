#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    argc = len(argv)
    opers=["+", "-", "*", "/"]
    if argc < 4 or argc > 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        operator = argv[2]
        b = int(argv[3])

        if operator is "+":
            print(add(a, b))
        elif operator is "-":
            print(sub(a, b))
        elif operator is "*":
            print(mul(a, b))
        elif operator is "/":
            print(div(a, b))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
