from ammm_project.problem import Problem, Square, Suitcase


def test_problem():
    problem = Problem(
        width=1,
        height=1,
        max_weight=1,
        squares=[
            Square(id=0, side=1, price=1, weight=1),
        ],
    )

    suitcase = Suitcase.empty(problem.width, problem.height)

    assert suitcase.value == 0

    suitcase = suitcase.add_square(problem.squares[0], 0, 0)

    assert problem.squares[0] in suitcase.content

    assert suitcase.value == 1

    suitcase = suitcase.remove_square(problem.squares[0])

    assert problem.squares[0] not in suitcase.content

    assert suitcase.value == 0

