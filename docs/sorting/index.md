
## Bubble sort

    def bubble_sort(arr: List[int]) -> None:
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]


## Merge Sort

    def merge(left: list[int], right: list[int]) -> list[int]:
    arr = []
    j = k = 0
    while j < len(left) and k < len(right):
        if left[j] < right[k]:
            arr.append(left[j])
            j += 1
        else:
            arr.append(right[k])
            k += 1

    arr += left[j:]
    arr += right[k:]
    return arr


    def merge_sort(arr: list[int]) -> list[int]:
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        b = merge_sort(arr[:mid])
        c = merge_sort(arr[mid:])
        return merge(b, c)


    def faster_merge(arr: list[int], aux: list[int], lo: int, mid: int, hi: int):
        for i in range(lo, mid + 1):
            aux[i] = arr[i]
    
        for i in range(mid + 1, hi + 1):
            aux[i] = arr[hi - i + mid + 1]
    
        i, j = lo, hi
        for k in range(lo, hi + 1):
            if aux[j] < aux[i]:
                arr[k] = aux[j]
                j -= 1
            else:
                arr[k] = aux[i]
                i += 1


    def faster_merge_sort(
        arr: list[int], aux: list[int], lo: int, hi: int
    ):  # Is not really fast, what is the source? TODO
        if lo == hi:
            return
        mid = (lo + hi) // 2
        faster_merge_sort(arr, aux, lo, mid)
        faster_merge_sort(arr, aux, mid + 1, hi)
        faster_merge(arr, aux, lo, mid, hi)
    
    
    def iterative_merge_sort(arr: list[int]):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_arr = arr[:mid]
            right_arr = arr[mid:]
    
            iterative_merge_sort(left_arr)
            iterative_merge_sort(right_arr)
    
            i = j = k = 0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1
    
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1
    
            while j < len(right_arr):
                arr[k] = right_arr[j]
                k += 1
                j += 1

## Quick sort

    def partition(A: List, p: int, r: int) -> int:
    # Select the last element in interval as a pivot element
    x = A[r]
    i = p - 1
    print("Partition:", A, p, "-->", r)
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            print("Partition step:", A)
    A[i + 1], A[r] = A[r], A[i + 1]
    print("Partition ends:", A)
    return i + 1


    def partition_increasing(A: List, p: int, r: int) -> int:
        # Select the last element in interval as a pivot element
        x = A[r]
        i = p - 1
        print("Partition:", A, p, "-->", r)
        for j in range(p, r):
            if A[j] >= x:
                i += 1
                A[i], A[j] = A[j], A[i]
                print("Partition step:", A)
        A[i + 1], A[r] = A[r], A[i + 1]
        print("Partition ends:", A)
        return i + 1
    
    
    def randomized_partition(A: List, p: int, r: int) -> int:
        i = random.randint(p, r)
        A[i], A[r] = A[r], A[i]
        return partition(A, p, r)
    
    
    def quicksort(A: List, p: int, r: int):
        if p < r:
            q = partition(A, p, r)
            print("Partitioned at", q)
            quicksort(A, p, q - 1)
            quicksort(A, q + 1, r)
    
    
    def randomized_quicksort(A: List, p: int, r: int):
        if p < r:
            q = randomized_partition(A, p, r)
            print("Partitioned at", q)
            quicksort(A, p, q - 1)
            quicksort(A, q + 1, r)


## Python STL `sort()`

Python lists have a built-in `sort()` method, which sorts the list of *comparable* objects in-place in ascending 
order by default.

`sort()` method has 2 optional keyword arguments:

- `reverse`. The default value is `False`. If it is set to `True` then the list will be sorted in descending order.

- `key`. Specifies the *key* for sorting.

    `list[str].sort(key=len)` sorts the list of strings by the lengths of the strings. If two strings have the same
    length then they preserve their actual order in thr list.

    `list[(int, int)].sort(key=lambda pair: pair[1])` sorts the list of pair if integers by the second element.