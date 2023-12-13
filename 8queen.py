def solveNQueens(board, col):
    if col == N:
        print_board(board)
        return True
    
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQueens(board, col + 1):
                return True
            board[i][col] = 0
    return False

def isSafe(board, row, col):
    for prev_col in range(col):
        if board[row][prev_col] == 1:
            return False
        if (row - col + prev_col >= 0 and board[row - col + prev_col][prev_col] == 1) or \
           (row + col - prev_col < N and board[row + col - prev_col][prev_col] == 1):
            return False
    return True

def print_board(board):
    for row in board:
        print(*row)
    print()
N = 8
board = [[0] * N for _ in range(N)]
if not solveNQueens(board, 0):
    print("No solution found")