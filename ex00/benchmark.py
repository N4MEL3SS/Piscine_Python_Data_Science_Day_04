#!/usr/bin/env python3
import timeit


def email_data():
    return 5 * ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']


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


def time_loop(n):
    stmt = 'loop_email()'
    code = 'from __main__ import loop_email'
    times = timeit.timeit(stmt=stmt, setup=code, number=n)
    # 90000000
    return times


def time_comprehension(n):
    stmt = 'list_comprehension_email()'
    code = 'from __main__ import list_comprehension_email'
    times = timeit.timeit(stmt=stmt, setup=code, number=n)
    # 90000000
    return times


def main():
    n = 90000000
    loop_time = time_loop(n)
    comprehension_time = time_comprehension(n)

    time_sorted = sorted([loop_time, comprehension_time])
    if time_sorted[0] == comprehension_time:
        print('it is better to use a list comprehension')
    else:
        print('it is better to use a loop')
    print(*time_sorted, sep=' vs ')


if __name__ == '__main__':
    main()
