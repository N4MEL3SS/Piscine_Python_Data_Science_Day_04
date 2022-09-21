#!/usr/bin/env python3
import timeit
from random import randint
from collections import Counter


def num_generator(num_range):
    return [randint(0, 100) for i in range(num_range)]


def dict_loop(rand_list):
    dict_count = {}
    set_rand_lst = set(rand_list)

    for i in set_rand_lst:
        dict_count[i] = rand_list.count(i)

    return dict_count


def top_num_loop(rand_lst):
    return sorted(dict_loop(rand_lst).items(), key=lambda x: x[1], reverse=True)[:10]


def dict_counter(rand_list):
    return Counter(rand_list)


def top_num_counter(rand_list):
    return dict_counter(rand_list).most_common(10)


def benchmark(name, num, rand_list):
    stmt = f'{name}({rand_list})'
    code = f'from __main__ import {name}'
    times = timeit.timeit(stmt=stmt, setup=code, number=num)
    return times


def main():
    random_list = num_generator(1000000)
    print("Random list created.")

    print('Loop: ', benchmark('top_num_loop', 5, random_list))
    print('Counter: ', benchmark('top_num_counter', 5, random_list))


if __name__ == '__main__':
    main()
