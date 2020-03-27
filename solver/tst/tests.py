import unittest

from ..src.sudoku_solver import SudokuSolver
from .validate import validateBoard
from ..src.utils import printBoard

class TestSudokuSolver(unittest.TestCase):

    def testValidity(self):
        ssolver = SudokuSolver()

        # board = [
        #     [9, 0, 0, 8, 3, 0, 1, 5, 7],
        #     [5, 0, 3, 1, 0, 6, 2, 8, 0],
        #     [1, 0, 0, 7, 4, 0, 0, 9, 0],
        #     [0, 0, 0, 0, 5, 0, 8, 3, 0],
        #     [3, 0, 1, 0, 0, 4, 6, 7, 2],
        #     [2, 0, 0, 0, 1, 3, 0, 0, 9],
        #     [0, 0, 2, 0, 7, 0, 0, 1, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 6, 0],
        #     [0, 3, 4, 0, 6, 0, 9, 2, 0]
        # ]

        board = [
            [9, 2, 6, 3, 4, 0, 0, 0, 1],
            [0, 0, 1, 7, 0, 0, 3, 0, 9],
            [0, 0, 3, 8, 0, 0, 2, 0, 6],
            [0, 0, 0, 0, 0, 7, 0, 0, 0],
            [0, 6, 0, 9, 1, 0, 4, 2, 0],
            [0, 9, 7, 2, 0, 0, 6, 0, 3],
            [0, 8, 0, 4, 7, 0, 1, 0, 2],
            [7, 0, 4, 1, 6, 2, 0, 0, 8],
            [0, 0, 0, 5, 3, 0, 0, 0, 0]
        ]

        solutions = ssolver.solve(board, all=True)
        for solution in solutions:
            self.assertTrue(validateBoard(solution))
            printBoard(solution)


if __name__ == '__main__':
    unittest.main()
