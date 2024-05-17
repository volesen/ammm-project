# ammm-project

Solving a 2D bin packing and knapsack problem using MILP and metahuristic algorithms.

## Project structure

The project is structured as follows:

- `ammm_project/`: Python package containing the implementation of the project.
- `tests/`: Unit tests for the project.
- `notebooks/`: Jupyter notebooks used for the development of the project.
- `scripts/`: Scripts used for running the project.
- `reference/`: Reference instances used for testing and benchmarking.
- `instances/`: Generated instances of the problem.
- `opl/`: OPL models used for the project.
- `results/`: Results of the project.

## Quick start

Prior to running the project, you need to install the required dependencies.
You can do so by running the following command:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

To run the notebooks, you should additionally install the development dependencies:
```bash
pip install -r requirements-dev.txt
```

Then you should be able to run the following two commands:
- `ammm-project` which solves a given instance of the problem - see the `--help` flag for more information.
- `generate-instance` which generates a random instance of the problem - see the `--help` flag for more information.

## Replicating the results

To replicate the results, you can run the commands in the `scripts/` folder and additionally run the notebooks in the `notebooks/` folder to generate the plots.

## References

- https://stackoverflow.com/questions/44427012/find-the-biggest-square-in-numpy-array
- https://github.com/secnot/rectpack
- https://github.com/rougier/freetype-gl/tree/master/doc
