"""
A modular multiplicative inverse of an integer a is an integer x such that a⋅x is congruent to 1 modular some modulus m
"""
import random
from typing import Optional

from algebra.power import power_modulo
from number_theory import gcd_extended, sieve_of_eratosthenes


def using_extended_euclidean_algorithm(a: int, m: int) -> Optional[int]:
    """
    This algorithm is efficient to find inverse of single number, which works in O(log(min(a, m)))
    If you need to find all the inverses of numbers till a then following method works well
    """
    g, x, y = gcd_extended.extended_euclidean_algorithm(a, m)
    if g > 1:
        print("No solution")
        return None
    else:
        return (x % m + m) % m


def using_binary_exponentiation(a: int, m: int) -> Optional[int]:
    """
    a ^ (m-1) = 1 mod m, if m is prime by Fermat's little theorem
    => a * a ^ (m-2) = 1 mod m => a^(m-2) mod m if a's inverse
    """
    i = 2
    while i * i <= m:
        if not m % i:
            print(f"m = {m} must be prime number")
            return None
        i += 1
    return power_modulo(a, m - 2, m)


def inverses(n: int, m: int) -> list[int]:
    """
    Return all inverses modulo m until n
    TC: O(n)
    """
    inv = [0] * n
    inv[1] = 1
    for i in range(2, n):
        inv[i] = m - (m // i) * inv[m % i] % m

    return inv


# ----------------------- TESTS ------------------------------


def test_using_extended_euclidean_algorithm():
    N = 10**9
    a, m = random.randint(1, N), random.randint(1, N)
    inverse = using_extended_euclidean_algorithm(a, m)
    if inverse is not None:
        assert a * inverse % m == 1


def test_using_binary_exponentiation():
    N = 10**9
    a, m = random.randint(1, N), random.randint(1, N)
    inverse = using_binary_exponentiation(a, m)
    if inverse is not None:
        assert a * inverse % m == 1


def test_inverses():
    N = 10**6
    primes = sieve_of_eratosthenes.primes(N)
    m = random.choice(primes)
    n = random.randint(1, m)
    inv = inverses(n, m)
    for i in range(1, n):
        try:
            assert (inv[i] * i) % m == 1
        except AssertionError:
            print(i * inv[i])
