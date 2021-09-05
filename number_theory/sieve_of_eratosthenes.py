"""
Time complexity: O(n*log(log(n)))
Memory: O(n)
"""


N = 10 ** 2
is_prime = [True] * N
primes = []

for i in range(2, N):
    if is_prime[i]:
        primes.append(i)
        j = i + i
        while j < N:
            is_prime[j] = False
            j += i

print(primes)
