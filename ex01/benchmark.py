#!/usr/bin/env python3
import timeit


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


def time_map(n):
    stmt = 'map_email()'
    code = 'from __main__ import map_email'
    times = timeit.timeit(stmt=stmt, setup=code, number=n)
    # 90000000
    return times


def main():
    n = 90000000
    loop_time = time_loop(n)
    comprehension_time = time_comprehension(n)
    map_time = time_map(n)

    time_sorted = sorted([loop_time, comprehension_time, map_time])
    if time_sorted[0] == comprehension_time:
        print('it is better to use a list comprehension')
    elif time_sorted[0] == loop_time:
        print('it is better to use a loop')
    else:
        print('it is better to use a map')
    print(*time_sorted, sep=' vs ')


if __name__ == '__main__':
    main()
