# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.  

def isValidSudoku(board: list[list[str]]) -> bool:
    for row in board:
        if not isValidRow(row):
            return False
    for col in zip(*board):
        if not isValidRow(col):
            return False
    return isValidSq(board)

# same as /challenges/arrays/contain_duplicate.py
def isValidRow(row: list[str]) -> bool:
    s = set()
    for n in row:
        if n in s:
            return False
        elif n != '.':
            s.add(n)
    return True
 # for each 3x3 square check if each row and column has no duplicates
def isValidSq(board: list[list[str]]) -> bool:
   

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            s = set()
            for k in range(i, i+3):
                for l in range(j, j+3):
                    if board[k][l] in s:
                        return False
                    elif board[k][l] != '.':
                        s.add(board[k][l])
    return True

board =[[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
print(isValidSudoku(board))

        