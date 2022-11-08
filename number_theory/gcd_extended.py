"""
While the Euclidean algorithm calculates only the greatest common divisor (GCD) of two integers a and b,
the extended version also finds a way to represent GCD in terms of a and b, i.e. coefficients x and y for which:
    a⋅x+b⋅y=gcd(a,b)
"""
import math
import random


def extended_euclidean_algorithm(a: int, b: int) -> (int, int, int):
    if b == 0:
        gcd, x, y = a, 1, 0
        return gcd, x, y
    else:
        x2, y2, x1, y1 = 1, 0, 0, 1
        while b > 0:
            q = a // b
            r, x, y = (a - b * q), (x2 - q * x1), (y2 - q * y1)
            a, b, x2, y2, x1, y1 = b, r, x1, y1, x, y
        gcd, x, y = a, x2, y2
        return gcd, x, y


def test_extended_euclidean_algorithm():
    n = 10**9
    a, b = random.randint(1, n), random.randint(1, n)
    g, x, y = extended_euclidean_algorithm(a, b)
    assert a * x + b * y == g and math.gcd(a, b) == g
