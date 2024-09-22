L, N1, N2 = map(int, input().split())

c1 = []
for _ in range(N1):
    v, l = map(int, input().split())
    c1.append((v, l))

c2 = []
for _ in range(N2):
    v, l = map(int, input().split())
    c2.append((v, l))

i, j, p, q = 0, 0, 0, 0

ans = 0

while p < len(c1) and q < len(c2):
    a, b = c1[p]
    c, d = c2[q]
    if a == c:
        ans += min(b + i, d + j) - max(i, j)

    if i + b < j + d:
        p += 1
        i += b
    else:
        q += 1
        j += d

print(ans)

