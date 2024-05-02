from .problem import Problem, Suitcase
from termcolor import colored



HIGHLIGHTS = [
    "on_black",
    #"on_grey",  # Actually black but kept for backwards compatibility
    "on_red",
    "on_green",
    "on_yellow",
    "on_blue",
    "on_magenta",
    "on_cyan",
    "on_light_grey",
    "on_dark_grey",
    "on_light_red",
    "on_light_green",
    "on_light_yellow",
    "on_light_blue",
    "on_light_magenta",
    "on_light_cyan",
    "on_white",
]

def highlighted(id: int) -> str:
    return colored(id_to_char(id), "white", HIGHLIGHTS[id % len(HIGHLIGHTS)])

def id_to_char(id: int) -> str:
    return chr(ord("A") + id)


def pretty(problem: Problem, suitcase: Suitcase) -> str:
    # Create a matrix to represent the suitcase
    suitcase_matrix = [
        ["." for _ in range(problem.width)] for _ in range(problem.height)
    ]

    for square, (x, y) in suitcase.content.items():
        for dx in range(square.side):
            for dy in range(square.side):
                suitcase_matrix[y + dy][x + dx] = highlighted(square.id)

    # Create a string to represent the suitcase
    suitcase_str = ""
    for row in suitcase_matrix:
        suitcase_str += "".join(row) + "\n"

    return suitcase_str
