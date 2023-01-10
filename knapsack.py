"""Knapsack 0/1 Approaches"""


class Item:

    def __init__(self, name: str, value: float, weight: float):
        self.name = name
        self.value = value
        self.weight = weight

    def inverse_weight(self) -> float:
        return 1.0 / self.weight

    def value_density(self) -> float:
        return self.value / self.weight


def greedy(items: list[Item], capacity: float, key: function):
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
    result = []
    total_value, total_weight = 0.0, 0.0
    for i in range(len(items_sorted)):
        if total_weight + items_sorted[i].weight <= capacity:
            result.append(items_sorted[i])
            total_weight += items_sorted.weight
            total_value += items_sorted[i].value

    return (result, total_value)
