#!/usr/bin/python3
character = 97

while(character < 123):
    if character == 101 or character == 113:
        pass
    else:
        print('{}'.format(chr(character)), end="")

    character += 1
