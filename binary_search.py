"""Binary Search - search sorted list for target

Iterative:
    Time:  O(log n)
    Space: O(1)

Recursive:
    Space: O(log n) - Call stack
"""


def binary_search(l: list[int], target: int) -> int:
    left, right = 0, len(l)-1
    while left <= right:
        mid = (left + right) // 2
        if l[mid] < target:
            left = mid + 1
        elif l[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


def binary_search_recur(l: list[int], target: int) -> int:
    return _binary_search_recur(l, target, 0, len(l) - 1)


def _binary_search_recur(l: list[int], target: int, left: int, right: int) -> int:
    if left > right:
        return -1

    mid = (left + right) // 2
    if l[mid] < target:
        return _binary_search_recur(l, target, mid + 1, right)
    elif l[mid] > target:
        return _binary_search_recur(l, target, left, mid - 1)
    else:
        return mid


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6]

    # Test iterative implementation
    assert binary_search(l, 1) == 0
    assert binary_search(l, 6) == 5
    assert binary_search(l, 3) == 2
    assert binary_search(l, 20) == -1

    # Test recursive implementation
    assert binary_search_recur(l, 1) == 0
    assert binary_search_recur(l, 6) == 5
    assert binary_search_recur(l, 3) == 2
    assert binary_search_recur(l, 20) == -1
