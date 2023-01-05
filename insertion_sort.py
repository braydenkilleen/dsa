"""Insertion Sort - sorts a list of integers in ascending order.

Time: O(n^2)

Space: O(n) total space and O(1) auxiliary space

"""


def insertion_sort(l: list[int]):
    for i in range(1, len(l)):
        curr = l[i]

        # Insert current element into sorted sub-array l[0:i-1]
        j = i - 1
        while j >= 0 and l[j] > curr:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = curr


if __name__ == '__main__':
    l = [31, 41, 59, 26, 51, 58]
    insertion_sort(l)
    assert l == [26, 31, 41, 51, 58, 59]
