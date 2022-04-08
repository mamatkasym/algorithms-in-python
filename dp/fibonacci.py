"""
Implementation of computing fibonacci N`th fibonacci number
"""


def memoization(n: int) -> int:
    def fib_mem(n):
        if not mem[n]:
            if n < 2:
                result = n
            else:
                result = fib_mem(n - 2) + fib_mem(n - 1)
            mem[n] = result
        return mem[n]

    mem = [0] * (n + 1)
    return fib_mem(n)


def tabulation(n: int) -> int:
    mem = [0] * (n + 1)
    mem[0] = 0
    mem[1] = 1
    for i in range(2, n + 1):
        mem[i] = mem[i - 2] + mem[i - 1]
    return mem[n]
