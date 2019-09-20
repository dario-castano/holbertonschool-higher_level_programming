#!/usr/bin/python3
def isa_roman_character(character):
    romans = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
    for roman in romans:
        if character == roman:
            return True
    return False


def isa_roman_number(word):
    return True if all([isa_roman_character(x) for x in word]) else False


def roman_to_int(roman_string):
    if isa_roman_number(roman_string):
        i = 0
        answer = []
        menu = {'I': {'val': 1, 'type': 1},
                'V': {'val': 5, 'type': 5},
                'X': {'val': 10, 'type': 1},
                'L': {'val': 50, 'type': 5},
                'C': {'val': 100, 'type': 1},
                'D': {'val': 500, 'type': 5},
                'M': {'val': 1000, 'type': 1}}

        while i < len(roman_string):
            val1 = menu[roman_string[i]]['val']
            if i + 1 < len(roman_string):
                val2 = menu[roman_string[i+1]]['val']
                if val1 >= val2:
                    answer.append(val1)
                    i += 1
                else:
                    answer.append(val2)
                    answer.append((-1) * val1)
                    i += 2
            else:
                answer.append(val1)
                i += 1
        return sum(answer)
    else:
        return 0
