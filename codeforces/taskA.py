def solve():
    n = int(input())
    s = input()
    a = [([s[i], i]) for i in range(n)]
    a.sort(key=lambda z: (z[0], z[1]))
    for i in range(1, n):
        if a[i][0] == a[i-1][0]:
            if a[i][1] - a[i-1][1] > 1:
                print('NO')
                return

    print('YES')


def main():
    for _ in range(int(input())):
        solve()


main()
