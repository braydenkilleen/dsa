
def merge_sort(l: list[int]):
    A = l.copy()

    if len(A) <= 1:
        return A

    # get middle element and split A into two subarrays
    mid = len(A) // 2
    l = A[:mid]
    r = A[mid:]

    return merge(merge_sort(l), merge_sort(r))
