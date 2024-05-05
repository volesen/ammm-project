from ammm_project.problem import Problem, Suitcase


def q(square, suitcase):
    """
    Greedy function
    """

    # Why not use the area of the square?
    # Because we want to pack the largest squares first
    return square.price / square.side


def greedy_search(problem: Problem, q=q):
    """
    Greedy search
    """

    suitcase = Suitcase(problem.width, problem.height)

    # Sort the squares by decreasing q
    squares = sorted(
        problem.squares,
        key=lambda square: q(square, suitcase),
        reverse=True,
    )

    # Add the squares to the suitcase
    for square in squares:
        # Skip the square if it is too heavy
        if suitcase.weight + square.weight > problem.max_weight: 
            continue

        # We exploit the fact lexigraphical order is the same as
        # top-leftmost order to find a free cell where the square fits
        for x, y in suitcase.free_cells:
            if suitcase.can_fit_square(square, x, y):
                suitcase = suitcase.add_square(square, x, y)
                break

    return suitcase
