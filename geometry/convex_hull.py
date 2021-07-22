"""
An algorithm to construct a convex hull from a set of points.
Consider N points given on a plane, and the objective is to generate a convex hull, i.e.
the smallest convex polygon that contains all the given points.
"""
from typing import List, Tuple


def is_in_upper(left: Tuple, right: Tuple, point: Tuple):
    if point[1] >= left[1] * (right[0] - point[0]) / (right[0] - left[0]) + right[1] * (point[0] - left[0]) / (
            right[0] - left[0]):
        return True
    return False


def vector(point1: Tuple, point2: Tuple):
    return [point2[0] - point1[0], point2[1] - point1[1]]


def clockwise(a: Tuple, b: Tuple, c: Tuple):
    return a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]) < 0


def counter_clockwise(a: Tuple, b: Tuple, c: Tuple):
    return a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]) > 0


def convex_hull(points: List[Tuple]):
    """
    Time complexity: O(n*log(n))
    """
    points = list(set(points))
    if len(points) == 1:
        return points

    points.sort(key=lambda z: (z[0], z[1]))
    p1 = points[0]
    p2 = points[-1]
    up = [p1]
    down = [p1]

    for i in range(1, len(points)):
        p = points[i]
        if i == len(points) - 1 or clockwise(p1, p, p2):
            while len(up) >= 2 and not clockwise(up[-2], up[-1], p):
                up.pop()
            up.append(p)
        if i == len(points) - 1 or counter_clockwise(p1, p, p2):
            while len(down) >= 2 and not counter_clockwise(down[-2], down[-1], p):
                down.pop()
            down.append(p)
    ans = []
    for x in down:
        ans.append(x)
    for x in reversed(up[1:-1]):
        ans.append(x)
    return ans


def main():
    # points = [(4, 1), (6, 1), (2, 2), (6, 2), (9, 2), (11, 2), (5, 3), (7, 4), (12, 4), (5, 5), (3, 6), (9, 6), (6, 7), (7, 1)]
    while True:
        n = int(input())
        if not n:
            break
        points = []
        for i in range(n):
            a, b = map(int, input().split())
            points.append((a, b))
        ans = convex_hull(points)
        print(len(ans))
        for point in ans:
            print(point[0], point[1])


if __name__ == '__main__':
    main()
