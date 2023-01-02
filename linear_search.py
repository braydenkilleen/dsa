"""Linear / Sequential Search 

Time:  O(n)
Space: O(1) """


def linear_search(l: list[any], target: any) -> int:
    for idx, el in enumerate(l):
        if el == target:
            return idx
    return -1


if __name__ == '__main__':
    l = [9, 2, 6, 1, 7, 4]
    res = linear_search(l, 9)
    assert res == 0

    res = linear_search(l, 6)
    assert res == 2
