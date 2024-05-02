import enum
import sys
import argparse

from .serialize import serialize
from .knapsack import generate as generate_knapsack_instance
from .bin_packing import generate as generate_bin_packing_instance
from .suitcase import generate as generate_suitcase_instance

class InstanceGenerator(enum.Enum):
    KNAPSACK = "knapsack"
    BIN_PACKING = "bin_packing"
    MIX = "mix"
    SUITCASE = "suitcase"


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

 
    # size of the grid is only required for the mix generator
    parser.add_argument(
        "size",
        type=int,
        nargs="?",
        help="The size of the grid",
    )

    # Parse the arguments, and call the appropriate function
    args = parser.parse_args()

    if args.generator == InstanceGenerator.KNAPSACK:
        instance = generate_knapsack_instance(args.size)
    elif args.generator == InstanceGenerator.BIN_PACKING:
        instance = generate_bin_packing_instance(args.size, capacity=1.0)
    elif args.generator == InstanceGenerator.MIX:
        instance = generate_bin_packing_instance(args.size)
    elif args.generator == InstanceGenerator.SUITCASE:
        instance = generate_suitcase_instance(args.size)

    print(serialize(instance))

    return 0