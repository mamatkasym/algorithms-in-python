
def solve():
    n = int(input())
    res = 0
    for i in range(1, 10):
        t = i
        while t <= n:
            res += 1
            t *= 10
            t += i

    print(res)


def main():
    for _ in range(int(input())):
        solve()


main()
