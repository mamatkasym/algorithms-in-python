"""
Roughly speaking, the elements in the monotonous increase stack keeps an increasing order.
"""

from collections import deque
from typing import Any

ms: Any = deque()

A: Any = []
for i in range(len(A)):
    while not ms and ms[-1] > A[i]:
        ms.pop()

    ms.append(A[i])
