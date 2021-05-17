def solve():
    n, m, x = map(int, input().split())
    h = list(map(int, input().split()))
    i = 0

    b = [0] * m
    ind = [-1] * n
    hai = [(h[i], i) for i in range(n)]
    hai.sort(key=lambda z: -z[0])
    # print(hai)
    i = 0
    j = 0
    while j < n:
        while b[i] <= b[(i+1) % m]:
            b[i] += hai[j][0]
            ind[hai[j][1]] = i+1
            j += 1
            if j >= n:
                break

        i += 1
        i %= m

    for i in range(1, m):
        if b[i] - b[i-1] > x:
            print('NO')
            return

    print('YES')
    for i in range(n):
        print(ind[i], end=' ')
    print()




def main():
    for _ in range(int(input())):
        solve()


main()
