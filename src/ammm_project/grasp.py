import random

from ammm_project.local_search import local_search

from .problem import Problem, Suitcase


def q(square, suitcase):
    """
    Greedy function
    """

    # Why not use the area of the square?
    # Because we want to pack the largest squares first
    return square.price / square.side


def grasp_search(problem: Problem, q=q, alpha=0.5):
    """
    Greedy search
    """

    suitcase = Suitcase.empty(problem.width, problem.height)

    # NOTE: As the RCL does not depend on the suitcase, we can calculate it
    # outside the loop.

    # Calculate the q value of a square
    squares = [(square, q(square, suitcase)) for square in problem.squares]

    # Calculate RCL
    q_min = min(q for _, q in squares)
    q_max = max(q for _, q in squares)

    rcl = [
        square
        for square, q_value in squares
        if q_value <= q_min + alpha * (q_max - q_min)
    ]

    # Shuffle the RCL
    random.shuffle(rcl)

    # Select the first random square that fits
    for square in rcl:
        # Skip the square if it is too heavy
        if suitcase.weight + square.weight > problem.max_weight:
            continue

        # We exploit the fact lexigraphical order is the same as
        # top-leftmost order to find a free cell where the square fits
        for x, y in suitcase.free_cells:
            if suitcase.can_fit_square(square, x, y):
                suitcase = suitcase.add_square(square, x, y)
                break

    # Run local search
    suitcase = local_search(problem, suitcase)

    return suitcase
