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
    start_j: int = (j // 3) * 3
    start_i: int = (j // 3) * 3
    for j, row in enumerate(board):
        for i, field in enumerate(row):
            if j >= start_j and j < start_j + 3:
                if i >= start_i and i < start_i + 3:
                    block.append(field)
    return block

def count_occurrences(val: int,  lst: list[int]) -> int:
    num_occurrences: int = 0
    for i in lst:
        if i == val:
            num_occurrences += 1
    return num_occurrences

def is_valid(board: list[list[int]]) -> bool:
    for j, row in enumerate(board):
        for i, field in enumerate(row):
            if not field:
                continue
            col: list[int] = get_col(board=board, i=i)
            block: lis[int] = get_block(board=board, j=j, i=i)
            if count_occurrences(val=field, lst=row) > 1:
                return False
            if count_occurrences(val=field, lst=col) > 1:
                return False
            if count_occurrences(val=field, lst=block) > 1:
                return False
    return True

print(
    is_valid(board=board)
)
