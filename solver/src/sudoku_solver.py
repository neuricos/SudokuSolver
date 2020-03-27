from typing import List, Tuple, Dict
from copy import deepcopy

class SudokuSolver:
    def __init__(self):
        pass

    def solve(self, board: List[List[int]], all=False) -> List[List[List[int]]]:
        solutions = []
        board_copy = deepcopy(board)

        possible_values_map = self.getPossibleValuesMap(board_copy)

        if possible_values_map is None:
            raise ValueError("Invalid Board")

        if len(possible_values_map) == 0:
            # All values are filled
            solutions.append(board_copy)
            return solutions

        board_stack = []
        tgt_cell, tgt_possible_values = None, None

        for cell in possible_values_map:
            possible_values = possible_values_map[cell]
            if tgt_cell is None or len(tgt_possible_values) > len(possible_values):
                tgt_cell, tgt_possible_values = cell, possible_values

        cr, cc = tgt_cell

        for tgt_possible_value in tgt_possible_values:
            new_board = deepcopy(board_copy)
            new_board[cr][cc] = tgt_possible_value
            board_stack.append(new_board)

        while len(board_stack) != 0:
            next_board = board_stack.pop()
            possible_values_map = self.getPossibleValuesMap(next_board)

            if possible_values_map is None:
                continue

            if len(possible_values_map) == 0:
                solutions.append(next_board)
                if not all:
                    return solutions
                continue

            tgt_cell, tgt_possible_values = None, None

            for cell in possible_values_map:
                possible_values = possible_values_map[cell]

                if tgt_cell is None or len(tgt_possible_values) > len(possible_values):
                    tgt_cell, tgt_possible_values = cell, possible_values

            cr, cc = tgt_cell

            for tgt_possible_value in tgt_possible_values:
                new_board = deepcopy(next_board)
                new_board[cr][cc] = tgt_possible_value
                board_stack.append(new_board)

        return solutions

    def getPossibleValuesMap(self, board: List[List[int]]) -> Dict[Tuple[int, int], List[int]]:
        possible_values_map = dict()

        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    possible_values = [v for v in range(1, 10) if self.possible(board, (r, c), v)]

                    if len(possible_values) == 0:
                        return None

                    if len(possible_values) == 1:
                        board[r][c] = possible_values.pop()
                        return self.getPossibleValuesMap(board)

                    possible_values_map[(r, c)] = possible_values

        return possible_values_map

    def possible(self, board: List[List[int]], cell: Tuple[int, int], value: int) -> bool:
        cr, cc = cell

        for c in range(9):
            if board[cr][c] == value:
                return False

        for r in range(9):
            if board[r][cc] == value:
                return False

        rs = cr // 3 * 3
        cs = cc // 3 * 3

        for r in range(rs, rs + 3):
            for c in range(cs, cs + 3):
                if board[r][c] == value:
                    return False

        return True


