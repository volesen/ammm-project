from dataclasses import dataclass
from functools import cached_property

import numpy as np


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

    width: int
    height: int
    content: dict[Square, tuple[int, int]]
    _matrix: np.ndarray

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.content = {}
        self._matrix = np.zeros((width, height), dtype=bool)

    def can_fit_square(self, square: Square, x: int, y: int) -> bool:
        """
        Check if the square can fit in the suitcase at position (x, y).
        """
        return (
            x + square.side <= self.width
            and y + square.side <= self.height
            and not np.any(self._matrix[x : x + square.side, y : y + square.side])
        )

    def add_square(self, square: Square, x: int, y: int):
        assert square not in self

        suitcase = Suitcase(self.width, self.height)

        # Add the square to the suitcase
        suitcase.content = {**self.content, square: (x, y)}

        # Copy the matrix
        suitcase._matrix = np.copy(self._matrix)

        # Mark the square as occupied
        suitcase._matrix[x : x + square.side, y : y + square.side] = True

        return suitcase

    def remove_square(self, square: Square):
        assert square in self

        suitcase = Suitcase(self.width, self.height)

        # Remove the square from the suitcase
        suitcase.content = {k: v for k, v in self.content.items() if k != square}

        # Copy the matrix
        suitcase._matrix = np.copy(self._matrix)

        # Mark the square as free
        x, y = self.content[square]

        suitcase._matrix[x : x + square.side, y : y + square.side] = False

        return suitcase

    @cached_property
    def value(self) -> int:
        return sum(square.price for square in self)

    @cached_property
    def weight(self) -> int:
        return sum(square.weight for square in self)

    @cached_property
    def free_cells(self):
        return np.argwhere(self._matrix == 0)

    def __contains__(self, square: Square) -> bool:
        return square in self.content

    def __iter__(self):
        return iter(self.content)

    def __repr__(self) -> str:
        return f"Suitcase(value={self.value}, weight={self.weight})"
