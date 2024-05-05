from dataclasses import dataclass

from sortedcontainers import SortedSet


@dataclass(frozen=True)
class Square:
    id: int
    side: int
    price: int
    weight: int


@dataclass(frozen=True)
class Problem:
    width: int
    height: int
    max_weight: int

    squares: list["Square"]

    @classmethod
    def from_dat(cls, dat: dict) -> "Problem":
        sides = dat["s"]
        prices = dat["p"]
        weights = dat["w"]
        num_squares = dat["n"]

        squares = [
            Square(
                id=i,
                side=sides[i],
                price=prices[i],
                weight=weights[i],
            )
            for i in range(num_squares)
        ]

        return cls(
            width=dat["x"],
            height=dat["y"],
            max_weight=dat["c"],
            squares=squares,
        )


class Suitcase:
    """
    A suitcase is a container that can hold squares.
    Can be used to represent a solution to the problem.
    """
    value: int
    weight: int
    free_cells: SortedSet[tuple[int, int]]
    content: dict[Square, tuple[int, int]]

    def __init__(
        self,
        value: int,
        weight: int,
        free_cells: SortedSet[tuple[int, int]],
        content: dict[Square, tuple[int, int]],
    ):
        self.value = value
        self.weight = weight
        self.free_cells = free_cells
        self.content = content

    # Empty suitcase
    @classmethod
    def empty(cls, width: int, height: int) -> "Suitcase":
        return cls(
            value=0,
            weight=0,
            free_cells=SortedSet((x, y) for x in range(width) for y in range(height)),
            content={},
        )


    def can_fit_square(self, square: Square, x: int, y: int) -> bool:
        """
        Check if the square can fit in the suitcase at position (x, y).
        """
        return all(
            (x + dx, y + dy) in self.free_cells
            for dx in range(square.side)
            for dy in range(square.side)
        )

    def add_square(self, square: Square, x: int, y: int):
        assert square not in self
        
        return Suitcase(
            value=self.value + square.price,
            weight=self.weight + square.weight,
            free_cells=self.free_cells.difference(
                {
                    (x + dx, y + dy)
                    for dx in range(square.side)
                    for dy in range(square.side)
                }
            ),
            content={**self.content, square: (x, y)},
        )

    def remove_square(self, square: Square):
        assert square in self, f"Square {square} is not in the suitcase. Content: {self.content}"
        
        # Extract the corner coordinates of the square
        (x, y) = self.content[square]

        return Suitcase(
            value=self.value - square.price,
            weight=self.weight - square.weight,
            free_cells=self.free_cells.union(
                {
                    (x + dx, y + dy)
                    for dx in range(square.side)
                    for dy in range(square.side)
                }
            ),
            content={k: v for k, v in self.content.items() if v != square},
        )

    def __contains__(self, square: Square) -> bool:
        return square in self.content

    def __iter__(self):
        return iter(self.content)

    def __repr__(self) -> str:
        return f"Suitcase(value={self.value}, weight={self.weight})"


