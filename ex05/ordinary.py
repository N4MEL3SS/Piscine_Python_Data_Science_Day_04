#!/usr/bin/env python3
from sys import argv


def main(file):
    pass


if __name__ == '__main__':
    if len(argv) == 2:
        main(argv[1])
    else:
        print('Usage: python3 ordinary.py filepath')
