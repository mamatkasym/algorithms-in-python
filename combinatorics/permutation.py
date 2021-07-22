"""
Find all permutation of array [1, 2, 3, ..., n]
"""
from typing import List

result = []


def permute(pos: int, arr: List, n: int):
    if pos == n:
        result.append(arr.copy())
    else:
        for j in range(pos, n):
            arr[pos], arr[j] = arr[j], arr[pos]
            permute(pos+1, arr, n)
            arr[pos], arr[j] = arr[j], arr[pos]


def main():
    n = int(input())
    arr = [i+1 for i in range(n)]
    permute(0, arr, n)
    print(result)

class AllPermutations:
    result = []
    def permute(self, pos, arr, n):
        if pos == n:
            result.append(arr.copy())
        else:
            for j in range(pos, n):
                arr[pos], arr[j] = arr[j], arr[pos]
                permute(pos+1, arr, n)
                arr[pos], arr[j] = arr[j], arr[pos]
    def getAll(self, n):
        if not n:
            return []
        arr = [i+1 for i in range(n)]
        self.permute(0, arr, n)
        return result


if __name__ == '__main__':
    main()
