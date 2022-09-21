#!/usr/bin/env python3
from sys import argv
import psutil


def ordinary(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    return lines


def main(filepath):
    try:
        for line in ordinary(filepath):
            pass
    except FileNotFoundError as err:
        print(err)

    mem_rss = psutil.Process().memory_info().rss / float(2 ** 30)
    mem_vms = psutil.Process().memory_info().vms / float(2 ** 30)
    cpu = psutil.Process().cpu_times()

    print(f'Peak Real Memory Usage = {mem_rss:0.3f} Gb')
    print(f'Peak Virtual Memory Usage = {mem_vms:0.3f} Gb')
    print(f'User Time + System Time = {cpu.user + cpu.system:0.2f}s')


if __name__ == '__main__':
    if len(argv) == 2:
        main(argv[1])
    else:
        print('Usage: python3 ./ordinary.py filepath')
