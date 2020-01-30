#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    if n < 0:  # baseline to check for negative since that can be caused by n-2 or n-3
        return 0
    elif n == 0:  # baseline to check if its zero
        return 1
    elif cache and cache[n] > 0:
        return cache[n]
    if not cache:
        cache = {}  # to check if cache has something in it.
    cache[n] = eating_cookies(
        n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]


print(eating_cookies(3))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
