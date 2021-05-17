
def bfs(root, e, order, cnt, vis, a, x, n):
    print(order)
    vis[root] = True
    cnt += 1

    if cnt >= n-1:
        print('YES')
        for i in range(len(order)):
            print(order[i])
    while True:
        if not e[root]:
            break
        e[root].sort(key=lambda z: z[0])
        last = e[root].pop()
        print('last', last)
        first = last[0]
        second = last[1]
        if not vis[first]:
            if a[first-1] + a[root-1] < x:
                print('NO')
                return

            a[first-1] = a[first-1] + a[root-1] - x
            order.append(second)
            bfs(first, e, order, cnt, vis, a, x, n)

            break


def solve():
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))

    e = [[]] * (n+1)
    for i in range(m):
        u, v = map(int, input().split())
        e[u].append((v, i+1))
        e[v].append((u, i+1))

    root = 1
    upper = 0
    for i in range(n):
        if a[i] > upper:
            upper = a[i]
            root = i + 1

    vis = [False] * (n+1)
    print('root', root)
    bfs(root, e, [], 0, vis, a, x, n)


def main():
    solve()


main()
