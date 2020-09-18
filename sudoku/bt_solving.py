import numpy as np

sudoku = np.array([
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
])

def assert_rules(column, row, value):
    if value in sudoku[row, :]:
        return False
    if value in sudoku[:, column]:
        return False

    if row < 3:
        row_lower_range = 0
        row_higher_range = 3
    elif row < 6:
        row_lower_range = 3
        row_higher_range = 6
    else:
        row_lower_range = 6
        row_higher_range = 9

    if column < 3:
        col_lower_range = 0
        col_higher_range = 3
    elif column < 6:
        col_lower_range = 3
        col_higher_range = 6
    else:
        col_lower_range = 6
        col_higher_range = 9

    if value in sudoku[row_lower_range:row_higher_range, col_lower_range:col_higher_range]:
        return False

    return True


def solve(column, row):
    if column >= 9 or row >= 9:
        return True

    if not sudoku[row, column]:
        for value in range(1, 10):
            if assert_rules(column, row, value):
                sudoku[row, column] = value
                attempt = solve(
                    (column + 1) % 9,
                    row if column < 8 else row + 1
                )
                if attempt:
                    return True
        sudoku[row, column] = 0
    else:
        attempt = solve(
            (column + 1) % 9,
            row if column < 8 else row + 1
        )
        if attempt:
            return True
    return False


if __name__ == '__main__':
    solve(0, 0)
    print(sudoku)
