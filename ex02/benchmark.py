#!/usr/bin/env python3
import timeit
from sys import argv


def email_data():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    return 5 * emails


def loop_email():
    emails = email_data()
    gmail = []

    for email in emails:
        if email.endswith('@gmail.com'):
            gmail.append(email)

    return gmail


def list_comprehension_email():
    emails = email_data()
    return [gmail for gmail in emails if gmail.endswith('@gmail.com')]


def map_email():
    emails = email_data()
    return map(lambda x: x if x.endswith('@gmail.com') else None, emails)


def filter_email():
    emails = email_data()
    return filter(lambda x: x if x.endswith('@gmail.com') else None, emails)


def benchmark(name, num):
    stmt = f'{name}()'
    code = f'from __main__ import {name}'
    times = timeit.timeit(stmt=stmt, setup=code, number=num)
    return times


def main(function, num):
    name_function = ['loop', 'list_comprehension', 'map', 'filter']

    if function in name_function:
        print(benchmark(function + '_email', int(num)))
    else:
        raise Exception(f'Function {function} not found!')
        # print(function, "not found!")


if __name__ == '__main__':
    if len(argv) == 3 and argv[2].isdigit():
        main(argv[1], argv[2])
    else:
        print("Usage: python3 ./benchmark.py function_name[loop, list_comprehension, map, filter] positive_num")
