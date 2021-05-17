"""
Time complexity: O(min(a, b))
"""


def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


print('Enter two integers:')
x, y = map(int, input().split())
print(gcd(x, y))

