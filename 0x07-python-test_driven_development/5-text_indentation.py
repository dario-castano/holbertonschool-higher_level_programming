#!/usr/bin/python3
def text_indentation(text):
    if not (type(text) is str):
        raise TypeError("text must be a string")
    else:
        print(text
              .replace('.', '.\n\n')
              .replace('?', '?\n\n')
              .replace(':', ':\n\n')
              .replace('\n ', '\n'), end="")
