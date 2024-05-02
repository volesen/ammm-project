import random
from typing import NamedTuple


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


def split_into_squares(width: int, height: int):
    # Split the rectangle into squares
    squares = []

    while width != height:
        if width > height:
            squares.append(Square(height))
            width -= height
        else:
            squares.append(Square(width))
            height -= width

    squares.append(Square(width))

    return squares


def generate(size: int, num_splits: int | None = None):
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

    return {
        "x": size,
        "y": 2 * size,
        "n": len(squares),
        "c": sum(s.area for s in squares),
        "w": [s.area for s in squares],
        "p": [s.area for s in squares],
        "s": [s.size for s in squares],
    }
