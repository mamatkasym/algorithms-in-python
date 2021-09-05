"""
Roughly speaking, the elements in the an monotonous increase stack keeps an increasing order.
"""

from collections import deque

# Initialize the stack
ms = deque()

A = list()
for i in range(len(A)):
    while not ms and ms[-1] > A[i]:
        ms.pop()

    ms.append(A[i])
