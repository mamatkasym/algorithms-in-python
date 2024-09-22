from collections import Counter, deque

n = int(input())
counter = Counter()
q = deque()
for _ in range(n):
    s, c = map(int, input().split())
    while s % 2 == 0:
        c += 1
        s //= 2

    t = 1
    while t < c:
        t *= 2

    while t:
        if c >= t:
            counter[(s, t)] += 1
            c -= t
        t //= 2

print(counter)
print(len(counter))

