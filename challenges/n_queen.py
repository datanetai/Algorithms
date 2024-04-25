def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]. This function checks the column and both diagonals."""
    # Check this column on the upper side
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, row):
    """Place queens on the board starting from the given row."""
    if row == len(board):
        return True  # All queens are placed

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = True  # Place queen
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = False  # Backtrack

    return False

def print_board(board):
    """Print the board."""
    for row in board:
        print(' '.join(['Q' if col else '.' for col in row]))

# solve column wise
def is_safe_col(board,row,col):
    for i in range(col):
        if board[row][i] == True:
            return False
    
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==True:
            return False
        
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):  
        if board[i][j]:
            return False
        
    return True 
    
def solve_n_queen_col(board,col):
    if col == len(board):
        return True
    
    for row in range(len(board)):
        if is_safe_col(board,row,col):
            board[row][col] = True
            if solve_n_queen_col(board,col+1):
                return True 
            board[row][col] = False

    return False


def main(n):
    """Setup and solve the N-Queens problem."""
    board = [[False] * n for _ in range(n)]
    if solve_n_queens(board, 0):
        print_board(board)
    else:
        print("No solution exists")

    board = [[False] * n for _ in range(n)]
    if solve_n_queen_col(board, 0):  # Call the column-wise function
        print_board(board)
    else:
        print("No solution exists")

# Run the algorithm for a 4x4 board
main(4)
