def possible(p):
    return sum([min(n, p // i) for i in range(1, m + 1)]) >= k


n, m, k = map(int, input().split())
X, Y = [], []
for _ in range(n):
    s, w = map(int, input().split())
    c = 
    X.append()

for _ in range(n):
    Y.append(map(int, input().split()))

low, high = 1, m * n
while low < high:
    mid = low + (high - low) // 2
    if possible(mid):
        high = mid
    else:
        low = mid + 1

print(low)