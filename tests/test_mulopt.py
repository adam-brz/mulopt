import pytest

from mulopt.optimizer import MatrixNode, MulOptimizer


def test_throws_for_empty_input():
    with pytest.raises(Exception):
        MulOptimizer().reduce([])


def test_returns_valid_solution_for_one_item():
    assert MulOptimizer().reduce([MatrixNode.from_str("A_2")]).name == "A"


def test_returns_valid_solution_for_many_items():
    nodes = [
        MatrixNode.from_str(m) for m in ["A_2_2", "B_2_6", "C_6_1", "D_1_2", "E_2"]
    ]
    assert MulOptimizer().reduce(nodes).name == "((A*(B*C))*(D*E))"
