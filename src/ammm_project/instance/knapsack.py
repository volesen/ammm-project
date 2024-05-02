import random


def generate(num_items: int):
    prices = [random.randint(1, 100) for _ in range(num_items)]
    weights = [random.randint(1, 100) for _ in range(num_items)]
    sides = [1 for _ in range(num_items)]

    capacity_fraction = random.uniform(0.5, 0.9)

    max_weight = int(sum(weights) * capacity_fraction)

    return {
        "x": 1,
        "y": num_items,
        "n": num_items,
        "c": max_weight,
        "w": weights,
        "p": prices,
        "s": sides,
    }
