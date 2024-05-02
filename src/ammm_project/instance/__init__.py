import enum
import sys
import argparse

from .serialize import serialize
from .knapsack import generate as generate_knapsack_instance


class InstanceGenerator(enum.Enum):
    KNAPSACK = "knapsack"
    BIN_PACKING = "bin_packing"
    MIX = "mix"


def main():
    parser = argparse.ArgumentParser(
        description="Generate instances for the AMMM project"
    )
    parser.add_argument(
        "generator",
        type=InstanceGenerator,
        choices=list(InstanceGenerator),
        help="The instance generator to use",
    )

    # num_items is only required for the knapsack generator
    parser.add_argument(
        "num_items",
        type=int,
        nargs="?",
        help="The number of items to generate",
    )

    # Parse the arguments, and call the appropriate function
    args = parser.parse_args()

    if args.generator == InstanceGenerator.KNAPSACK:
        instance = generate_knapsack_instance(args.num_items)
    elif args.generator == InstanceGenerator.BIN_PACKING:
        raise NotImplementedError("Bin packing instances are not implemented")
    elif args.generator == InstanceGenerator.MIX:
        raise NotImplementedError("Mixed instances are not implemented")

    print(serialize(instance))

    sys.exit(0)
