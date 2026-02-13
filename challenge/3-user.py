#!/usr/bin/python3
"""basic user script placeholder"""

class User:
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print(f"User: {sys.argv[1]}")
    else:
        print("No user provided")
