import argparse
import sys
from argparse import ArgumentParser

from mulopt.optimizer import MatrixNode, MulOptimizer

if __name__ == "__main__":
    description = """
    Utility for optimization of matrix multiplication order.

    Order of multiplication can have significant influence on number of performed operations. This program estimates
    the number of operations for all order possibilities and returns order with lowest number of operations.

    Matrices can be specified as space separated list of items with following format: "<name>_<number_of_rows>[_<number_of_columns>]".
    For example: "A_2_3 B_3_2 C_2" is valid input and means that we would like to multiply A*B*C and A is 2x3 matrix, B is 3x2 matrix and C is 2x2 matrix.
    """

    parser = ArgumentParser(description=description)
    parser.add_argument(
        "--debug",
        help="enable debug output to stderr",
        required=False,
        default=False,
        action=argparse.BooleanOptionalAction,
    )
    parser.add_argument(
        "--stdin",
        help="read input data from stdin",
        required=False,
        default=False,
        action=argparse.BooleanOptionalAction,
    )
    parser.add_argument(
        "--data",
        "-d",
        help="data to parse in string format (otherwise will read from stdin)",
        required=False,
        default=None,
    )

    args = parser.parse_args()

    if not args.stdin and not args.data:
        parser.error(
            "No data specified (--data is empty) and reading from stdin is disabled (--no-stdin). Aborting"
        )

    data = sys.stdin.read() if not args.data else args.data
    mats = [MatrixNode.from_str(m) for m in data.split()]

    if mats:
        optimal = MulOptimizer(args.debug).reduce(mats)
        print(optimal.name)
