import math


def binary_search(l: list[int], target: int) -> int:
    left, right = 0, len(l)-1
    while left <= right:
        mid = (left + right) // 2
        if l[mid] < target:
            left += 1
        elif l[mid] > target:
            right -= 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6]
    assert binary_search(l, 1) == 0
    assert binary_search(l, 6) == 5
    assert binary_search(l, 3) == 2
    assert binary_search(l, 20) == -1
