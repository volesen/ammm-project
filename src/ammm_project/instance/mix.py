import random
from ..problem import Suitcase, Square


def shuffled(iterable):
    items = list(iterable)
    random.shuffle(items)
    return items


def generate(size: int):
    # Start by generating random squares that fill the entire grid
    suitcase = Suitcase.empty(size, size)

    squares = []

    capacity_fraction = random.uniform(0, 1)

    id = 1

    max_size = size // 2

    while suitcase.free_cells:
        random_side = random.randint(1, max_size)

        # Generate a random square
        square = Square(
            id=id,
            price=random_side**2,
            weight=random_side**2,
            side=random_side,
        )

        for x, y in shuffled(suitcase.free_cells):
            if suitcase.can_fit_square(square, x, y):
                suitcase = suitcase.add_square(square, x, y)
                squares.append(square)
                id += 1
                break
        else:
            # The size is too big, reduce it
            max_size -= 1

    max_weight = int(sum(square.weight for square in squares) * capacity_fraction)

    return {
        "x": size,
        "y": size,
        "n": len(squares),
        "c": max_weight,
        "w": [square.weight for square in squares],
        "p": [square.price for square in squares],
        "s": [square.side for square in squares],
    }
