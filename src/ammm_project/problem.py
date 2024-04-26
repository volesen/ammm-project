class Square:
    id: int
    price: int
    weight: int
    side: int

    def __init__(self, id: int, price: int, weight: int, side: int):
        self.id = id
        self.price = price
        self.weight = weight
        self.side = side


class Suitcase:
    """
    A suitcase is a grid of WxH cells, where each cell can be either empty or occupied by a square.
    """

    # Immutable properties
    width: int
    height: int
    max_weight: int

    # Mutable properties
    free_cells: set[tuple[int, int]]

    weight: int
    value: int
    contents: dict[int, tuple[int, int]]

    def __init__(self, width: int, height: int, max_weight: int):
        self.width = width
        self.height = height
        self.max_weight = max_weight

        self.free_cells = {(x, y) for x in range(width) for y in range(height)}

        self.weight = 0
        self.value = 0
        self.contents = {}

    def can_fit_square(self, square: Square, x: int, y: int) -> bool:
        """
        Check if the square can fit in the suitcase at position (x, y).
        """
        return all(
            (x + dx, y + dy) in self.free_cells
            for dx in range(square.side)
            for dy in range(square.side)
        )

    def is_below_weight_limit(self, square: Square) -> bool:
        """
        Check if adding the square keeps the total weight below the maximum allowed weight.
        """
        return self.weight + square.weight <= self.max_weight

    def add_square(self, square: Square, x: int, y: int):
        self.contents[square.id] = (x, y)

        self.weight += square.weight
        self.value += square.price

        self.free_cells.difference_update(
            {(x + dx, y + dy) for dx in range(square.side) for dy in range(square.side)}
        )

    def remove_square(self, square: Square, x: int, y: int):
        self.contents.pop(square.id)

        self.weight -= square.weight
        self.value -= square.price

        self.free_cells.update(
            {(x + dx, y + dy) for dx in range(square.side) for dy in range(square.side)}
        )

    def __contains__(self, square: Square) -> bool:
        return square.id in self.contents

    def __str__(self) -> str:
        return f"Suitcase(width={self.width}, height={self.height}, max_weight={self.max_weight}, weight={self.weight}, value={self.value}, contents={self.contents})"


def from_dat(dat: dict):
    suitcase = Suitcase(
        width=dat["x"],
        height=dat["y"],
        max_weight=dat["c"],
    )

    squares = [
        Square(
            id=i,
            price=dat["p"][i],
            weight=dat["w"][i],
            side=dat["s"][i],
        )
        for i in range(dat["n"])
    ]

    return suitcase, squares
