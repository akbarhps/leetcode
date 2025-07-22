from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowindex = 0
        for i in range(0, len(board)):
            cache = {}
            for j in range(0, len(board[0])):
                col = board[i][j]
                if col == '.': continue
                if col in cache:
                    return False
                else:
                    cache[col] = True

            cache = {}
            for j in range(0, len(board[0])):
                col = board[j][i]
                if col == '.': continue
                if col in cache:
                    return False
                else:
                    cache[col] = True

            if i > 0 and i % 3 == 0:
                rowindex += 1

            cache = {}
            colindex = (i % 3) * 3
            for j in range(rowindex * 3, (rowindex * 3) + 3):
                for k in range(colindex, colindex + 3):
                    col = board[j][k]
                    if col == '.': continue
                    if col in cache:
                        return False
                    else:
                        cache[col] = True

        return True


board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
         [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."],
         [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]
print(Solution().isValidSudoku(board))

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(Solution().isValidSudoku(board))
