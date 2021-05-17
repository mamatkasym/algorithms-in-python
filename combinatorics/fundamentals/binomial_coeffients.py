

def naive(n, k):
    res = 1
    for i in range(n - k + 1, n+1):
        res *= i
    for i in range(2, k+1):
        res //= i
    return res


def improved(n, k):
    res = 1.0
    for i in range(1, k+1):
        res = res * (n-k+i) / i
    return int(res + 0.01)