#!/usr/bin/python3


def number_of_lines(filename=""):
    """returns the number of lines of a text file"""
    with open(filename, 'r') as f:
        return len(f.readlines())


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file (UTF8) and prints it to stdout"""
    file_lines = number_of_lines(filename)
    with open(filename, 'r', encoding='utf-8') as file:
        if nb_lines <= 0 or nb_lines > file_lines:
            print(file.read(), end="")
        else:
            for i in range(nb_lines):
                print(file.readline(), end="")
