#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hd4
    [print(x) for x in dir(hd4) if not x.startswith('__')]
