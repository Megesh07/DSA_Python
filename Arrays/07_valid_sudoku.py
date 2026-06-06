"""
Problem: Valid Sudoku
Link: https://leetcode.com/problems/valid-sudoku/

Time Complexity: O(9^2) -> O(1)
Space Complexity: O(9^2) -> O(1)
"""
import collections
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
