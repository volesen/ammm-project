import sys
import random
from functools import lru_cache
from typing import NamedTuple

sys.setrecursionlimit(10_000_000)


class Square(NamedTuple):
    size: int

    @property
    def area(self):
        return self.size**2


class Reactangle(NamedTuple):
    width: int
    height: int

    @property
    def is_square(self):
        return self.width == self.height

    @property
    def area(self):
        return self.width * self.height


def split(rect: Reactangle, x: int, horizontal: bool):
    if horizontal:
        return [Reactangle(rect.width, x), Reactangle(rect.width, rect.height - x)]
    else:
        return [Reactangle(x, rect.height), Reactangle(rect.width - x, rect.height)]


@lru_cache
def split_into_squares(width: int, height: int):
    # Split the rectangle into squares
    if width == height:
        return [Square(width)]
    elif width > height:
        return [Square(height)] + split_into_squares(width - height, height)
    else:
        return [Square(width)] + split_into_squares(width, height - width)


def generate(size: int, capacity: float | None = None, num_splits: int | None = None):
    if capacity is None:
        capacity_fraction = random.uniform(0, 1)

    if num_splits is None:
        num_splits = size // 4

    # We start with a single rectangle
    rects = [Reactangle(size, 2 * size)]

    for _ in range(num_splits):
        # Pick a random non-square rectangle
        r = random.choice([r for r in rects if not r.is_square])

        # Split the rectangle at a random position
        rects.remove(r)

        # Split the rectangle on the longest side
        horizontal = r.width < r.height

        split_position = random.randint(1, max(r.width, r.height))

        rects += split(r, split_position, horizontal)

    # Convert the rectangles into squares
    squares = []

    for r in rects:
        squares += split_into_squares(r.width, r.height)

    weight = sum(s.area for s in squares)
    max_weight = capacity_fraction * weight

    return {
        "x": size,
        "y": 2 * size,
        "n": len(squares),
        "c": max_weight,
        "w": [s.area for s in squares],
        "p": [s.area for s in squares],
        "s": [s.size for s in squares],
    }
