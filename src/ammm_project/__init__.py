import argparse
import sys
import time
from enum import Enum

import ammm_project.grasp
import ammm_project.greedy
import ammm_project.local_search
import ammm_project.parsers.dat
import ammm_project.pretty
import ammm_project.problem

from .runner import run


class Algorithm(Enum):
    GREEDY = "greedy"
    GREEDY_WITH_LOCAL_SEARCH = "greedy_with_local_search"
    GRASP = "grasp"


def main() -> int:
    parser = argparse.ArgumentParser(description="AMMM project")
    # Verbosity
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Increase output verbosity",
    )
    parser.add_argument("dat", type=str, help="The .dat file to solve")
    parser.add_argument(
        "--algorithm",
        type=Algorithm,
        choices=list(Algorithm),
        default=Algorithm.GREEDY,
        help="Algorithm to use",
    )
    parser.add_argument(
        "--alpha",
        type=float,
        default=0.5,
        help="Alpha parameter for GRASP algorithm",
    )

    args = parser.parse_args()

    with open(args.dat, "r") as f:
        dat = ammm_project.parsers.dat.parse(f)

    problem = ammm_project.problem.Problem.from_dat(dat)

    start_time = time.time()

    if args.algorithm == Algorithm.GREEDY:
        suitcase = ammm_project.greedy.greedy_search(problem)
        iterations = 1
    elif args.algorithm == Algorithm.GREEDY_WITH_LOCAL_SEARCH:
        suitcase = ammm_project.greedy.greedy_search(problem)

        suitcase = ammm_project.local_search.local_search(problem, suitcase)

        iterations = 1
    elif args.algorithm == Algorithm.GRASP:
        # Partially apply the alpha parameter
        def grasp_search(problem):
            return ammm_project.grasp.grasp_search(problem, alpha=args.alpha)

        suitcase, iterations = run(grasp_search, problem, max_time=60)

    end_time = time.time()

    # time elapsed, time pr. iteration, best value

    elapsed = end_time - start_time
    print(f"{elapsed},{elapsed / iterations},{suitcase.value}", file=sys.stderr)

    if args.verbose:
        print(ammm_project.pretty.pretty(problem, suitcase), file=sys.stdout)
        print(suitcase.content)

    print(suitcase)
    return 0
