from collections import Counter
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board or len(board) != 9 or len(board[0]) != 9:
            return None
        s = set()
        for i in range(9):
            # each row
            for j in range(9):
                if board[i][j] != "." and board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])
            s.clear()
            # each column
            for k in range(9):
                if board[k][i] != "." and board[k][i] in s:
                    return False
                else:
                    s.add(board[k][i])
            s.clear()


        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for m in range(i, i + 3):
                    for n in range(j, j + 3):
                        if board[m][n] != '.' and board[m][n] in s:
                            return False
                        else:
                            s.add(board[m][n])
                s.clear()
        return True


so = Solution()
print(so.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                           , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                           , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                           , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                           , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                           , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                           , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                           , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                           , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

'''
Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


'''
