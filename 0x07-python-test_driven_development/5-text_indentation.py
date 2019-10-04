#!/usr/bin/python3
def text_indentation(text):
    """Function that prints a text with
     2 new lines after each of these characters:
      . ? and :"""
    if not (type(text) is str):
        raise TypeError("text must be a string")
    else:
        print(text
              .replace('.', '.\n\n')
              .replace('?', '?\n\n')
              .replace(':', ':\n\n')
              .replace('\n ', '\n'), end="")
