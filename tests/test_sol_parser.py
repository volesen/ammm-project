from ammm_project.parsers.sol import parse


def test_parse_sol():
    with open("tests/project.2.sol") as sol_file:
        objective, solution = parse(sol_file)

    assert objective == 11
    assert solution == [["", "C", "E"], ["B", "A", "A"], ["D", "A", "A"]]
