class Item:

    def __init__(self, name: str, value: float, weight: float):
        self.name = name
        self.value = value
        self.weight = weight

    def inverse_weight(self) -> float:
        return 1.0 / self.weight

    def value_density(self) -> float:
        return self.value / self.weight
