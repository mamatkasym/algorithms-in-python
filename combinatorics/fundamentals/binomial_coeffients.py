

def timer(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        start_time = perf_counter()
        to_execute = fn(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print('{0} took {1:.8f}s to execute'.format(fn.__name__, execution_time))
        return to_execute

    return inner


@timer
def naive(n, k):
    res = 1
    for i in range(n - k + 1, n+1):
        res *= i
    for i in range(2, k+1):
        res //= i
    return res


@timer
def improved(n, k):
    res = 1.0
    for i in range(1, k+1):
        res = res * (n-k+i) / i
    return int(res + 0.01)


if __name__ == '__main__':
    naive(2000, 1000)
    improved(2000, 1000)
