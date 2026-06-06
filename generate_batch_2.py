import os
import subprocess

problems = [
    {
        "folder": "Arrays",
        "filename": "07_valid_sudoku.py",
        "title": "Valid Sudoku",
        "code": '"""\nProblem: Valid Sudoku\nLink: https://leetcode.com/problems/valid-sudoku/\n\nTime Complexity: O(9^2) -> O(1)\nSpace Complexity: O(9^2) -> O(1)\n"""\nimport collections\nclass Solution:\n    def isValidSudoku(self, board: list[list[str]]) -> bool:\n        cols = collections.defaultdict(set)\n        rows = collections.defaultdict(set)\n        squares = collections.defaultdict(set)  # key = (r /3, c /3)\n        for r in range(9):\n            for c in range(9):\n                if board[r][c] == ".":\n                    continue\n                if (board[r][c] in rows[r] or\n                    board[r][c] in cols[c] or\n                    board[r][c] in squares[(r // 3, c // 3)]):\n                    return False\n                cols[c].add(board[r][c])\n                rows[r].add(board[r][c])\n                squares[(r // 3, c // 3)].add(board[r][c])\n        return True\n'
    },
    {
        "folder": "Arrays",
        "filename": "08_encode_and_decode_strings.py",
        "title": "Encode and Decode Strings",
        "code": '"""\nProblem: Encode and Decode Strings\nLink: https://leetcode.com/problems/encode-and-decode-strings/\n\nTime Complexity: O(N)\nSpace Complexity: O(1)\n"""\nclass Solution:\n    def encode(self, strs: list[str]) -> str:\n        res = ""\n        for s in strs:\n            res += str(len(s)) + "#" + s\n        return res\n\n    def decode(self, s: str) -> list[str]:\n        res, i = [], 0\n        while i < len(s):\n            j = i\n            while s[j] != "#":\n                j += 1\n            length = int(s[i:j])\n            res.append(s[j + 1 : j + 1 + length])\n            i = j + 1 + length\n        return res\n'
    },
    {
        "folder": "Arrays",
        "filename": "09_longest_consecutive_sequence.py",
        "title": "Longest Consecutive Sequence",
        "code": '"""\nProblem: Longest Consecutive Sequence\nLink: https://leetcode.com/problems/longest-consecutive-sequence/\n\nTime Complexity: O(N)\nSpace Complexity: O(N)\n"""\nclass Solution:\n    def longestConsecutive(self, nums: list[int]) -> int:\n        numSet = set(nums)\n        longest = 0\n        for n in nums:\n            # check if its the start of a sequence\n            if (n - 1) not in numSet:\n                length = 0\n                while (n + length) in numSet:\n                    length += 1\n                longest = max(length, longest)\n        return longest\n'
    },
    {
        "folder": "Two_Pointers",
        "filename": "01_valid_palindrome.py",
        "title": "Valid Palindrome",
        "code": '"""\nProblem: Valid Palindrome\nLink: https://leetcode.com/problems/valid-palindrome/\n\nTime Complexity: O(N)\nSpace Complexity: O(1)\n"""\nclass Solution:\n    def isPalindrome(self, s: str) -> bool:\n        l, r = 0, len(s) - 1\n        while l < r:\n            while l < r and not self.alphaNum(s[l]):\n                l += 1\n            while r > l and not self.alphaNum(s[r]):\n                r -= 1\n            if s[l].lower() != s[r].lower():\n                return False\n            l, r = l + 1, r - 1\n        return True\n    \n    def alphaNum(self, c):\n        return (ord("A") <= ord(c) <= ord("Z") or \n                ord("a") <= ord(c) <= ord("z") or \n                ord("0") <= ord(c) <= ord("9"))\n'
    },
    {
        "folder": "Two_Pointers",
        "filename": "02_two_sum_ii.py",
        "title": "Two Sum II",
        "code": '"""\nProblem: Two Sum II - Input Array Is Sorted\nLink: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/\n\nTime Complexity: O(N)\nSpace Complexity: O(1)\n"""\nclass Solution:\n    def twoSum(self, numbers: list[int], target: int) -> list[int]:\n        l, r = 0, len(numbers) - 1\n        while l < r:\n            curSum = numbers[l] + numbers[r]\n            if curSum > target:\n                r -= 1\n            elif curSum < target:\n                l += 1\n            else:\n                return [l + 1, r + 1]\n        return []\n'
    }
]

def run_git(args):
    subprocess.run(["git"] + args, check=True)

for p in problems:
    filepath = os.path.join(p["folder"], p["filename"])
    with open(filepath, "w") as f:
        f.write(p["code"])
    
    with open("progress.md", "a") as f:
        f.write(f"| 2026-06-06 | {p['folder']} | {p['title']} | Complete |\\n")
    
    run_git(["add", filepath])
    run_git(["add", "progress.md"])
    run_git(["commit", "-m", f"Solve {p['title']}"])

# Push all to remote
run_git(["push", "-u", "origin", "main"])
