#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

my_square_4 = Square(0, (0, 0))
my_square_4.my_print()

print("--")

my_square_5 = Square(0, (3, 1))
my_square_5.my_print()

print("--")

my_square_6 = Square(0, (5, 5))
my_square_6.my_print()

print("--")

my_square_7 = Square(0, (0, 7))
my_square_7.my_print()

print("--")

my_square_7 = Square(2, (4, 4))
my_square_7.my_print()

print("--")