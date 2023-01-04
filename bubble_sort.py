"""Bubble Sort - sorts a list of integers in ascending order.

Time: O(n^2) for both swaps and comparisons

Space: O(n) total and O(1) aux. n is the length of list.
"""


def bubble_sort(l: list[int]) -> None:
    """Basic in-place bubble sort"""
    for i in range(0, len(l)):
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]


def bubble_sort_opt(l: list[int]) -> None:
    """Optimised in-place bubble sort."""
    swapped = False
    while not swapped:
        swapped = True
        for i in range(1, len(l)):
            if l[i] < l[i-1]:
                l[i], l[i-1] = l[i-1], l[i]
                swapped = False


if __name__ == '__main__':
    l1 = [2, 7, 6, 3, 7, 9, 5]
    bubble_sort(l1)
    assert l1 == [2, 3, 5, 6, 7, 7, 9]

    l2 = [2, 7, 6, 3, 7, 9, 5]
    bubble_sort_opt(l2)
    assert l2 == [2, 3, 5, 6, 7, 7, 9]
