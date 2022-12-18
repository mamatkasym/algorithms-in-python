from algorithms.algebra.modular_inverse import using_extended_euclidean_algorithm


def timer(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        start_time = perf_counter()
        to_execute = fn(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print("{0} took {1:.8f}s to execute".format(fn.__name__, execution_time))
        return to_execute

    return inner


@timer
def naive(n: int, k: int) -> int:
    """
    TC: O(n)
    MC: O(1)
    Inefficient or overflows for large n
    """
    res = 1
    for i in range(n - k + 1, n + 1):
        res *= i
    for i in range(2, k + 1):
        res //= i
    return res


@timer
def improved(n: int, k: int) -> int:
    """
    TC: O(k)
    MC: O(1)
    Inefficient or overflows for large n
    """
    res = 1.0
    for i in range(1, k + 1):
        res = res * (n - k + i) / i
    return int(res + 0.01)


def pascals_triangle(n: int, k: int) -> int:
    """
    TC: O(n*k)
    MC: O(n*k)
    """
    # dp[i][j] = C(i, j)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        dp[i][0] = dp[i][i] = 1
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

    return dp[n][k]


def binomial_coefficients_modulo_m(n: int, k: int, m: int) -> int:
    def binomial_coefficient(dn: int, dk: int) -> int:
        """TC: O(log(m))"""
        return (
            factorial[n]
            * using_extended_euclidean_algorithm(factorial[k] * factorial[n - k] % m, m)
            % m
        )

    # Pre compute factorials
    factorial = [0] * (n + 1)
    factorial[0] = 1
    for i in range(1, n + 1):
        factorial[i] = factorial[i - 1] * i % m

    return binomial_coefficient(n, k)
