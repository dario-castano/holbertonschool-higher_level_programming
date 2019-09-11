#!/usr/bin/python3
for character in range(122, 96, -1):
    if character % 2 is not 0:
        character -= 32
    print('{}'.format(chr(character)), end="")
