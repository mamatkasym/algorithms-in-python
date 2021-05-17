
def solve():
    n = int(input())
    c = list(map(int, input().split()))
    dp = [0] * n
    for i in range(n):
        for j in range(1, n-i):
            if c[j+i] - c[i] == j:
                dp[i+j] += 1
    # print(dp)
    ans = sum(dp)
    print(ans)


def main():
    for _ in range(int(input())):
        solve()


main()
