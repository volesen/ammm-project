import argparse
import ammm_project.parsers.dat
import ammm_project.greedy
import ammm_project.problem


def main() -> int:
    parser = argparse.ArgumentParser(description="AMMM project")
    # .dat file
    parser.add_argument("dat", type=str, help="The .dat file to solve")
    args = parser.parse_args()

    with open(args.dat, "r") as f:
        dat = ammm_project.parsers.dat.parse(f)

    suitcase, squares = ammm_project.problem.from_dat(dat)

    suitcase = ammm_project.greedy.greedy_search(suitcase, squares)

    print(suitcase)

    return 0
