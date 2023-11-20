# William Xia
# 10/29/23
# Assignment 4: Constraint Satisfaction Problems

# This program searches for the solution to a given sudoku board using constraint
# satisfaction algorithms, then returns the solution.

def is_valid(board, row, col, num, size):
    # Check if the num is not present in the same row and column
    if num in board[row] or num in [board[i][col] for i in range(size)]:
        return False

    # Check if the num is not present in the same box
    box_size = int(size**0.5)
    start_row, start_col = box_size * (row // box_size), box_size * (col // box_size)
    for i in range(start_row, start_row + box_size):
        for j in range(start_col, start_col + box_size):
            if board[i][j] == num:
                return False

    return True

def find_empty(board, size):
    # Find the first empty cell (with value 0)
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(board):
    size = len(board)

    # Find an empty cell
    row, col = find_empty(board, size)

    # If there are no empty cells, the puzzle is solved
    if row is None:
        return True

    # Try placing a number in the empty cell
    for num in range(1, size + 1):
        if is_valid(board, row, col, num, size):
            # Place the number if it satisfies the constraints
            board[row][col] = num

            # Recursively try to solve the rest of the puzzle
            if solve_sudoku(board):
                return True

            # If placing the number leads to an invalid solution, backtrack
            board[row][col] = 0

    # No valid number found, need to backtrack
    return False

def print_sudoku(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if j == 8:
                print(board[i][j])
            else:
                print(f"{board[i][j]} ", end="")


# Hard Board

initial_board = [
    [0, 7, 0, 0, 4, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 6, 1, 0],
    [3, 9, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 4, 0, 0, 9],
    [0, 0, 3, 0, 0, 0, 7, 0, 0],
    [5, 0, 0, 1, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 7, 6],
    [0, 5, 4, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 1, 0, 0, 5, 0]
]


# initial_board = [
#     [6, 0, 8, 7, 0, 2, 1, 0, 0],
#     [4, 0, 0, 0, 1, 0, 0, 0, 2],
#     [0, 2, 5, 4, 0, 0, 0, 0, 0],
#     [7, 0, 1, 0, 8, 0, 4, 0, 5],
#     [0, 8, 0, 0, 0, 0, 0, 7, 0],
#     [5, 0, 9, 0, 6, 0, 3, 0, 1],
#     [0, 0, 0, 0, 0, 6, 7, 5, 0],
#     [2, 0, 0, 0, 9, 0, 0, 0, 8],
#     [0, 0, 6, 8, 0, 5, 2, 0, 3]
# ]

print("Initial Sudoku Board:")
print_sudoku(initial_board)
print("")
print("Solving....")
print("")

if solve_sudoku(initial_board):
    print("Solution:")
    print_sudoku(initial_board)
else:
    print("No solution exists.")