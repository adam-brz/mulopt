import re
import sys
from dataclasses import dataclass


@dataclass
class MatrixNode:
    name: str
    rows: int
    cols: int
    cost: float = 0

    MAT_REGEX = re.compile(r"(?P<name>[A-Za-z0-9]+)_(?P<rows>\d+)(_(?P<cols>\d+))?")

    @staticmethod
    def from_str(s: str):
        if match := MatrixNode.MAT_REGEX.match(s):
            name, rows, cols = match.group("name", "rows", "cols")
            return MatrixNode(name, int(rows), int(cols) if cols else int(rows))
        raise ValueError(f"Invalid matrix string: {s}")


@dataclass
class MatrixProduct:
    m1: MatrixNode
    m2: MatrixNode

    def to_matrix_node(self):
        assert (
            self.m1.cols == self.m2.rows
        ), f"Invalid matrix dimensions for multiplication {self.m1} vs {self.m2}"
        return MatrixNode(
            f"({self.m1.name}*{self.m2.name})",
            self.m1.rows,
            self.m2.cols,
            self._get_cost(),
        )

    def _get_cost(self):
        return (
            self.m1.cost
            + self.m2.cost
            + (self.m1.rows * self.m2.rows * (2 * self.m2.cols - 1))
        )


class MulOptimizer:
    def __init__(self, debug=False) -> None:
        self.debug = debug

    def reduce(self, matrices: list[MatrixNode]) -> MatrixNode:
        optimal = self._reduce(matrices)[0]
        self.log("Optimal: ", optimal)
        return optimal

    def _reduce(self, matrices: list[MatrixNode]) -> list[MatrixNode]:
        if len(matrices) < 2:
            return matrices

        min_path = matrices
        min_cost = float("inf")

        for i in range(1, len(matrices)):
            m = MatrixProduct(matrices[i - 1], matrices[i])
            new_path = matrices[: i - 1] + [m.to_matrix_node()] + matrices[i + 1 :]

            self.log(f"-- Checking --> {new_path}")
            reduced_path = self._reduce(new_path)

            cost = reduced_path[0].cost
            if cost < min_cost:
                min_cost = cost
                min_path = reduced_path

        self.log(f"-- Reduced --> {min_path}")
        return min_path

    def log(self, *args):
        if self.debug:
            print(*args, file=sys.stderr)
