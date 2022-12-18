"""
Properties:
    1. calculates the value of function F in the given range [L,R] (i.e. F(A[L], A[L+1],...,A[R])) in O(log(n)) time;
    2. updates the value of an element of A in O(log(n)) time;
    3. requires O(N) memory, or in other words, exactly the same memory required for A;
    4. is easy to use and code, especially, in the case of multidimensional arrays.
"""


class FenwickTreeSum:
    def __init__(self, n):
        self.ft = [] * n

    def add(self, idx: int, val: int):
