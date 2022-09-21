#!/usr/bin/env python3
import timeit
from sys import argv
from functools import reduce


def loop_sum(n):
    res = 0
    for i in range(0, n + 1):
        res += i * i
    return res


def reduce_sum(n):
    return reduce(lambda i, j: i + j * j, range(0, n + 1))


def benchmark(name, num, n_sum):
    stmt = f'{name}({n_sum})'
    code = f'from __main__ import {name}'
    times = timeit.timeit(stmt=stmt, setup=code, number=num)
    return times


def main(function, num, sqrt_sum):
    name_function = ['loop', 'reduce']

    if function in name_function:
        print(benchmark(function + '_sum', int(num), int(sqrt_sum)))
    else:
        raise Exception(f'Function {function} not found!')
        # print(function, "not found!")


if __name__ == '__main__':
    if len(argv) == 4 and argv[2].isdigit() and argv[3].isdigit():
        main(argv[1], argv[2], argv[3])
    else:
        print("Usage: python3 ./benchmark.py function_name[loop, reduce] positive_num, sqrt_num")
