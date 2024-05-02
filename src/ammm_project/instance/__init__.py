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

    # Parse the arguments, and call the appropriate function
    args, rest = parser.parse_known_args()

    if args.generator == InstanceGenerator.KNAPSACK:
        instance = generate_knapsack_instance(int(rest[0]))
    elif args.generator == InstanceGenerator.BIN_PACKING:
        raise NotImplementedError("Bin packing instances are not implemented")
    elif args.generator == InstanceGenerator.MIX:
        raise NotImplementedError("Mixed instances are not implemented")

    print(serialize(instance))

    sys.exit(0)
