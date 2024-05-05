import random

from .local_search import local_search
from .problem import Problem, Suitcase


def q(square, suitcase):
    """
    Greedy function, higher is better
    """

    # Why not use the area of the square?
    # Because we want to pack the largest squares first
    return square.price / square.side


def candidate_list(problem: Problem, suitcase: Suitcase):
    # Select the first random square that fits
    for square in problem.squares:
        # Skip the square if it is already in the suitcase
        if square in suitcase:
            continue

        # Skip the square if it is too heavy
        if suitcase.weight + square.weight > problem.max_weight:
            continue

        # We exploit the fact lexigraphical order is the same as
        # top-leftmost order to find a free cell where the square fits
        for x, y in suitcase.free_cells:
            if suitcase.can_fit_square(square, x, y):
                yield (square, x, y)
                break


def grasp_search(problem: Problem, q=q, alpha=0.5):
    """
    Greedy search
    """

    # Constructive phase
    suitcase = Suitcase(problem.width, problem.height)

    while True:
        candidates = list(candidate_list(problem, suitcase))

        if not candidates:
            break

        # Calculate RCL
        q_min = min(q(square, suitcase) for square, _, _ in candidates)
        q_max = max(q(square, suitcase) for square, _, _ in candidates)

        rcl_max = [
            (square, x, y)
            for square, x, y in candidates
            if q(square, suitcase) >= q_max - alpha * (q_max - q_min)
        ]

        # Select a random square from the RCL
        (square, x, y) = random.choice(rcl_max)

        # Add the square to the suitcase
        suitcase = suitcase.add_square(square, x, y)

    # Run local search
    suitcase = local_search(problem, suitcase)

    return suitcase
