# SudokuSolver

The code runs a non-recursive algorithm to solve the sudoku problem.

A sample usage of SudokuSolver is as follows:

```python3
ssolver = SudokuSolver()
# board is a 9 x 9 matrix
board = [
    [],
    ...,
    []
]
solutions = ssolver.solve(board, all=True)
```

Note that you can specify whether you want all possible solutions or just one of them by setting the `all` parameter to be `True` or `False`. The default is `False`. In order to get the correct result, the user must make sure that the values passed in to the solver is correct, i.e., values ranges from 0 to 9, inclusively, where 0 is used to indicate that the spot is not filled.
