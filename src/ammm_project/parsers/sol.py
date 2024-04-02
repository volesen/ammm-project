from typing import TextIO


def parse(sol_file: TextIO) -> dict:
    objective = int(sol_file.readline().removeprefix("OBJECTIVE: "))

    # Skip empty line
    sol_file.readline()

    # Parse the rest of the file
    solution = []

    for line in sol_file:
        solution.append([letter for letter in line.split("\t") if letter != "\n"])

    return objective, solution
