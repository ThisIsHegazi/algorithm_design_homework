class Item:
    def __init__(self, value, weight) -> None:
        self.value = value
        self.weight = weight
        self.ratio = value / weight


class Knapsack:
    def __init__(self, max_capacity) -> None:
        self.max_capacity = max_capacity
        self.current_capacity = 0
        self.items: list[Item] = []
        self.total_value = 0
        self.to_full = self.max_capacity - self.current_capacity

    def add_item(self, item: Item):
        if item.weight > self.to_full:
            item.weight = self.to_full
            item.value = self.to_full * item.ratio
        self.items.append(item)
        self.total_value += item.value
        self.current_capacity += item.weight
        self.to_full = self.max_capacity - self.current_capacity

    def is_full(self):
        return self.to_full == 0


def create_items(values, weights):
    items = []
    for i in range(len(values)):
        items.append(Item(values[i], weights[i]))
    items.sort(key=lambda x: x.ratio, reverse=True)
    return items


def fill_knapsack(max_weight, values, weights):
    knap = Knapsack(max_weight)
    items = create_items(values, weights)
    for item in items:
        if knap.is_full():
            return knap
        knap.add_item(item)
    return knap


values = [4, 9, 12, 11, 6, 5]
weights = [1, 2, 10, 4, 3, 5]

print(fill_knapsack(12, values, weights).total_value)
