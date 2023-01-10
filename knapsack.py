"""Knapsack 0/1 Approaches.

An item has value and weight. Knapsack seeks to find a solution which maximises value under capacity/weight constraint.

TODO:
    - Implement brute force
    
"""


from typing import Callable


class Item:

    def __init__(self, name: str, value: float, weight: float):
        self.name = name
        self.value = value
        self.weight = weight

    def value_density(self) -> float:
        return self.value / self.weight

    def __str__(self) -> str:
        return f'(name={self.name}, value={self.value}, weight: {self.weight}'


def greedy(items: list[Item], capacity: float, key: Callable):
    """Greedy approach to knapsack. 

    Running Time: O(n log n) - due to sorted()


    Args:
        items - list of Item objects
        capacity - maximum carrying capacity constraint
        key - custom function to map items to numbers
    """

    if capacity <= 0:
        raise ValueError('capacity must be greater than 0.')
    if len(items) == 0:
        raise ValueError('items must contain an item.')

    items_sorted = sorted(items, key=key, reverse=True)
    selected = []
    total_value, total_weight = 0.0, 0.0
    for i in range(len(items_sorted)):
        if total_weight + items_sorted[i].weight <= capacity:
            selected.append(items_sorted[i])
            total_weight += items_sorted[i].weight
            total_value += items_sorted[i].value

    return (selected, total_value)


if __name__ == '__main__':
    items = [
        Item('a', 100, 10),
        Item('b', 80, 9),
        Item('c', 20, 5),
        Item('d', 75, 4)
    ]
    selected, total_value = greedy(items, 35, lambda x: x.value_density())

    print('Selected')
    for s in selected:
        print(s)

    print(f'Total value: {total_value}')
