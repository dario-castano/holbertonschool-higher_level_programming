#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

if last_digit > 5:
    tail_string = "and is greater than 5"
elif last_digit == 0:
    tail_string = "and is 0"
else:
    tail_string = "and is less than 6 and not 0"

print("Last digit of {} is {} {}".format(number, last_digit, tail_string))
