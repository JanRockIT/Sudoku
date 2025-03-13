# Input: unsolved board
board: list[list[str]] = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solved_board: list[list[str]] = [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]

board: list[list[int]] = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 1, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def get_col(board: list[list[int]], i: int) -> list[int]:
    col: list[int] = []
    for row in board:
        field: int = row[i]
        col.append(field)
    return col

def get_block(board: list[list[int]], j: int, i: int) -> list[list[int]]:
    block: list[list[int]] = []
    start_j: int = get_nearest(val=j, targets=[0, 3, 6])
    start_i: int = get_nearest(val=i, targets=[0, 3, 6])
    for j, row in enumerate(board):
        if j >= start_j and j <= start_j + 2:
            block_row: list[int] = []
            for i, field in enumerate(row):
                if i >= start_i and i <= start_i + 2:
                    block_row.append(field)
            block.append(block_row)
    
    return block


def get_nearest(val: int, targets: list[int]) -> int:
    nearest_target: int
    nearest_abs: int = 10
    for target in targets:
        current_abs: int = abs((val-1) - target)
        if current_abs < nearest_abs:
            nearest_abs = current_abs
            nearest_target = target
    return nearest_target

    
def is_valid(board: list[list[int]]) -> None:
    for j1, row in enumerate(board):
        for i, field in enumerate(row):
            if field == 0:
                continue
            row_copy: list[int] = row
            row_copy[i] = 0
            col: list[int] = get_col(board=board, i=i)
            col[j1] = 0
            block: list[list[int]] = get_block(board=board, j=j1, i=i)
            for j2, block_row1 in enumerate(block):
                if field in block_row1:
                    block[j2][block_row1.index(field)] = 0
            if field in row_copy:
                return False
            if field in col:
                return False
            for block_row2 in block:
                if field in block_row2:
                    return False
            print(block, j1, i, field)
    return True


print(
    is_valid(board=board)
)