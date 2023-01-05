def insertion_sort(l: list[int]):
    for i in range(2, len(l)):
        key = l[i]
        j = i - 1
        while j > 0 and l[j] > key:
            l[j+1] = l[j]
            j = j - 1
        l[j+1] = key
