"""
Time complexity: O(n*log(log(n)))
Memory: O(n)
"""


def primes(n):
    """ Return prime numbers until n """

    is_prime = [True] * n
    prime_numbers = []

    for i in range(2, n):
        if is_prime[i]:
            prime_numbers.append(i)
            j = i + i
            while j < n:
                is_prime[j] = False
                j += i
    return prime_numbers
