def primes(n: int) -> list[int]:
    """
    Returns prime numbers less than n
    Time complexity is O(n*log(log(n)))
    Memory complexity is O(n)
    """

    is_prime = [True] * n
    prime_numbers = []

    for i in range(2, n):
        if is_prime[i]:
            prime_numbers.append(i)
            j = i * i
            while j < n:
                is_prime[j] = False
                j += i
    return prime_numbers


def primes_optimized(n: int) -> list[int]:
    """Needs fewer operations than previous function"""
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    i = 0
    while i * i < n:
        if is_prime[i]:
            j = i * i
            while j < n:
                is_prime[j] = False
                j += i
        i += 1
    return [i for i in range(n) if is_prime[i]]


def test():
    assert primes_optimized(14) == primes(14) == [2, 3, 5, 7, 11, 13]
