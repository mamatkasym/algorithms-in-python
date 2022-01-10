import math
import random


def power_modulo(n: int, k: int, m: int) -> int:
    """
    returns n^k mod m
    TC: log(k + m)
    """
    res = 1
    while k > 0:
        if k % 2:
            res = res * n % m
        k //= 2
        n = n * n % m

    return res


# ----------------- TESTS -----------------------------

def test_power_modulo():
    n, k, m = random.sample(range(1, 10), 3)
    assert power_modulo(n, k, m) == math.pow(n, k) % m
