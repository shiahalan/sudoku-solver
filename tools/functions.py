from tools.board import board


def display_board():  # Prints the board row by row
    for rows in board:
        new = []
        for element in rows:
            new.append(str(element))
        print("  ".join(new))


def valid(n, row, col):  # Constraints / Bounding function for recursion
    if n in board[row]:
        return False

    for r in range(9):
        if board[r][col] == n:
            return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for row in range(row_start, row_start + 3):
        for col in range(col_start, col_start + 3):
            if board[row][col] == n:
                return False

    return True


def next_space():  # Finds next available space on the board
    global board

    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return 'No Spaces', 'No Spaces'


def sudoku_solver(row, col):  # Uses recursion backtracking
    global board
    row, col = next_space()
    if row == 'No Spaces' and col == 'No Spaces':  # End of puzzle
        return True

    for n in range(1, 10):
        if valid(n, row, col):
            board[row][col] = n
            if sudoku_solver(row, col):  # Never true until end of puzzle
                return True
    board[row][col] = 0  # Return previous valid answer to 0 since forward answer is false
    return False


if __name__ == '__main__':
    sudoku_solver(0, 0)
