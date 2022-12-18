"""
You are given two numbers n and k. Find the largest power of k x such that n! is divisible by k^x.

Answer is ⌊n/k⌋ + ⌊n/k2⌋ + … + ⌊n/ki⌋ + …
"""


def fact_pow(n, k):
    res = 0
    while n:
        n /= k
        res += n
    return res
