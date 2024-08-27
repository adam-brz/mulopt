# Mulopt

Utility for optimization of matrix multiplication order.

Order of multiplication can have significant influence on number of performed operations.
This program estimates the number of operations for all order possibilities and returns
order with lowest number of operations.

This program answers following question:

```
A*B*C*D <-- most optimal order? --> A*(B*C)*D
```

## Why?

Recently in some C++ code I've stumbled upon expression similar to this: P\*C\*D\*R\*K.
Where each symbol represents matrix of various shape.

My question was: what is most efficient way of grouping terms so that program would perform the least amount of operations.

I figured out brute-force algorithm to solve this problem, which is implemented in this tool.

## Installation

```bash
git clone https://github.com/adam-brz/mulopt
cd mulopt
pip install .
```

## Usage

Parse data from string:

```bash
python -m mulopt -d "A_2_2 B_2_6 C_6_1 D_1_2 E_2"
# result: ((A*(B*C))*(D*E))
```

Matrices can be specified as space separated list of items with following format: `<name>_<number_of_rows>[_<number_of_columns>]`.

For example: `A_2_3 B_3_2 C_2` is valid input and means that we would like to multiply A\*B\*C where A is 2x3 matrix, B is 3x2 matrix and C is 2x2 matrix.

For full program description see help:

```bash
python -m mulopt --help
```
