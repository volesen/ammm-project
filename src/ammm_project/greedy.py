from ammm_project.problem import Square, Suitcase


def q(square, suitcase):
    """
    Greedy function
    """
    return square.price / (square.side**2 * square.weight)


def greedy_search(suitcase: Suitcase, squares: list[Square]):
    """
    Greedy search
    """

    # Sort the squares by decreasing price
    squares.sort(key=lambda square: q(square, suitcase), reverse=True)

    # Add the squares to the suitcase
    for square in squares:
        if not suitcase.is_below_weight_limit(square):
            # We can remove this square from the list of squares
            # because it will never fit in the suitcase
            continue

        # We exploit the fact lexigraphical order is the same as
        # top-leftmost order to find a free cell where the square fits
        for x, y in sorted(suitcase.free_cells):
            if suitcase.can_fit_square(square, x, y):
                suitcase.add_square(square, x, y)
                break
        else:
            # We can remove this square from the list of squares
            # because it will never fit in the suitcase
            continue

    return suitcase
