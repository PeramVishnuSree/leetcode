# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


class Solution:
    def isValidSudoku(self, board):

        for m in range(9):
            c = []
            r = []
            if m == 3 or m == 6 or m == 0:
                g1, g2, g3 = [], [], []
            for n in range(9):
                if board[n][m] != '.':
                    if int(board[n][m]) in c: return False
                    c.append(int(board[n][m]))
                if board[m][n] != '.':
                    if int(board[m][n]) in r: return False
                    r.append(int(board[m][n]))
                if n <= 2 and board[m][n] != '.':
                    if board[m][n] in g1: return False
                    g1.append(board[m][n])
                elif n > 2 and n <= 5 and board[m][n] != '.':
                    if board[m][n] in g2: return False
                    g2.append(board[m][n])
                elif n > 5 and board[m][n] != '.':
                    if board[m][n] in g3: return False
                    g3.append(board[m][n])

        return True


