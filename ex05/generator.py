#!/usr/bin/env python3
from sys import argv
import psutil


def generator(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            yield line


def main(filepath):
    try:
        for line in generator(filepath):
            pass
    except FileNotFoundError as err:
        print(err)

    mem = psutil.Process().memory_info().vms / (10 ** 9)
    cpu = psutil.Process().cpu_times()
    print(f'Peak Memory Usage = {mem} Gb')
    print(f'User Time + System Time = {cpu.user + cpu.system}s')


if __name__ == '__main__':
    if len(argv) == 2:
        main(argv[1])
    else:
        print('Usage: python3 ./generator.py filepath')
