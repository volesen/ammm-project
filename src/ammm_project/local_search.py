from .problem import Problem, Suitcase


def repack_suitcase(problem: Problem, suitcase: Suitcase):
    """
    Repacks the suitcase by removing all squares and adding them again in a different order.

    We order the squares by side length in descending order, and we try to add them to the suitcase in that order.
    """

    repacked_suitcase = Suitcase(problem.width, problem.height)

    squares = sorted(suitcase, key=lambda s: s.side, reverse=True)

    for square in squares:
        for x, y in repacked_suitcase.free_cells:
            if repacked_suitcase.can_fit_square(square, x, y):
                repacked_suitcase = repacked_suitcase.add_square(square, x, y)
                break

    return repacked_suitcase

def neighbourhood_solutions(problem: Problem, suitcase: Suitcase, repack: bool = False):
    for square_to_remove in suitcase.content:
        neighbour_suitcase = suitcase.remove_square(square_to_remove)

        # Repack the suitcase (optimizing for space)
        if repack:
            neighbour_suitcase = repack_suitcase(problem, suitcase)

        # Try to add a new square
        for square in problem.squares:
            # Skip the square if it is already in the suitcase
            if square in neighbour_suitcase:
                continue

            # Skip the square if it is too heavy
            if neighbour_suitcase.weight + square.weight > problem.max_weight:
                continue

            # Now we try to find a free cell where the square fits
            for x, y in neighbour_suitcase.free_cells:
                if neighbour_suitcase.can_fit_square(square, x, y):
                    yield neighbour_suitcase.add_square(square, x, y)
                    break


def local_search(problem: Problem, suitcase: Suitcase, repack: bool = False):
    # First improvement local search
    while True:
        for neighbour in neighbourhood_solutions(problem, suitcase, repack=repack):
            if neighbour.value > suitcase.value:
                suitcase = neighbour
                break

        # If no neighbour is better, we have reached a local optimum
        else:
            break

    return suitcase

