import sys
import time

from .problem import Problem


def run(
    search_algorithm,
    problem: Problem,
    max_time: float = 5 * 60,
    max_time_without_improvement: float | None = None,
):
    """
    Run the search algorithm for a maximum amount of time
    """

    best_solution = None
    best_value = 0

    # Start the timer
    start_time = time.time()

    # Time since the last improvement
    improvement_time = start_time

    iterations = 1

    while True:
        current_time = time.time()

        # Check if we have reached the maximum time
        if current_time - start_time > max_time:
            break

        # Check if we have reached the maximum time without improvement
        if max_time_without_improvement and (
            current_time - improvement_time > max_time_without_improvement
        ):
            break

        # Run the search algorithm
        solution = search_algorithm(problem)

        # Check if the solution is better
        if solution.value > best_value:
            best_solution = solution
            best_value = solution.value

            improvement_time = current_time

            elapsed = current_time - start_time
            print(f"{elapsed},{elapsed / iterations},{solution.value}", file=sys.stdout)

        iterations += 1

    return best_solution, iterations
