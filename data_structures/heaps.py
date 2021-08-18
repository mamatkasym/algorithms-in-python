import heapq

d = [1, 4, 3, 3, 5]
t = [1, 4, 3, 5, 3]
heapq.heapify(d)
print(d)
heapq.heapify(t)
print(t)
print(t == d)