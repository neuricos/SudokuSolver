from typing import List

def validateBoard(board: List[List[int]]) -> bool:
    valid_values = tuple(range(1, 10))

    # Check each value
    for r in range(9):
        for c in range(9):
            if board[r][c] not in valid_values:
                return False

    # Check rows
    for r in range(9):
        seen_values = set(board[r])
        if len(seen_values) != 9:
            return False
    
    # Check columns
    for c in range(9):
        seen_values = set(board[r][c] for r in range(9))
        if len(seen_values) != 9:
            return False

    for i in range(3):
        for j in range(3):
            seen_values = set()

            rs = 3 * i
            cs = 3 * j

            for r in range(rs, rs + 3):
                for c in range(cs, cs + 3):
                    v = board[r][c]
                    if v in seen_values:
                        return False
                    seen_values.add(v)

    return True

