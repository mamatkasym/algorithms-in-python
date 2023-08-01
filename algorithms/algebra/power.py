import math
import random


def power_modulo(base: int, power: int, mod: int) -> int:
    """
    returns n^k mod m
    TC: log(k + m)
    """
    res = 1
    while power > 0:
        if power % 2:
            res = res * base % mod
        power //= 2
        base = base * base % mod

    return res


# ----------------- TESTS -----------------------------


def test_power_modulo():
    n, k, m = random.sample(range(1, 10), 3)
    assert power_modulo(n, k, m) == math.pow(n, k) % m
