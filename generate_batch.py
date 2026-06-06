import os
import subprocess
import time

problems = [
    {
        "folder": "Arrays",
        "filename": "02_valid_anagram.py",
        "title": "Valid Anagram",
        "code": '"""\nProblem: Valid Anagram\nLink: https://leetcode.com/problems/valid-anagram/\n\nTime Complexity: O(S + T)\nSpace Complexity: O(S + T)\n"""\nclass Solution:\n    def isAnagram(self, s: str, t: str) -> bool:\n        if len(s) != len(t): return False\n        countS, countT = {}, {}\n        for i in range(len(s)):\n            countS[s[i]] = countS.get(s[i], 0) + 1\n            countT[t[i]] = countT.get(t[i], 0) + 1\n        for c in countS:\n            if countS[c] != countT.get(c, 0):\n                return False\n        return True\n'
    },
    {
        "folder": "Arrays",
        "filename": "03_two_sum.py",
        "title": "Two Sum",
        "code": '"""\nProblem: Two Sum\nLink: https://leetcode.com/problems/two-sum/\n\nTime Complexity: O(N)\nSpace Complexity: O(N)\n"""\nclass Solution:\n    def twoSum(self, nums: list[int], target: int) -> list[int]:\n        prevMap = {} # val -> index\n        for i, n in enumerate(nums):\n            diff = target - n\n            if diff in prevMap:\n                return [prevMap[diff], i]\n            prevMap[n] = i\n        return []\n'
    },
    {
        "folder": "Arrays",
        "filename": "04_group_anagrams.py",
        "title": "Group Anagrams",
        "code": '"""\nProblem: Group Anagrams\nLink: https://leetcode.com/problems/group-anagrams/\n\nTime Complexity: O(M * N)\nSpace Complexity: O(M * N)\n"""\nfrom collections import defaultdict\nclass Solution:\n    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:\n        res = defaultdict(list)\n        for s in strs:\n            count = [0] * 26\n            for c in s:\n                count[ord(c) - ord("a")] += 1\n            res[tuple(count)].append(s)\n        return list(res.values())\n'
    },
    {
        "folder": "Arrays",
        "filename": "05_top_k_frequent_elements.py",
        "title": "Top K Frequent Elements",
        "code": '"""\nProblem: Top K Frequent Elements\nLink: https://leetcode.com/problems/top-k-frequent-elements/\n\nTime Complexity: O(N)\nSpace Complexity: O(N)\n"""\nclass Solution:\n    def topKFrequent(self, nums: list[int], k: int) -> list[int]:\n        count = {}\n        freq = [[] for i in range(len(nums) + 1)]\n        for n in nums:\n            count[n] = 1 + count.get(n, 0)\n        for n, c in count.items():\n            freq[c].append(n)\n        res = []\n        for i in range(len(freq) - 1, 0, -1):\n            for n in freq[i]:\n                res.append(n)\n                if len(res) == k:\n                    return res\n'
    },
    {
        "folder": "Arrays",
        "filename": "06_product_of_array_except_self.py",
        "title": "Product of Array Except Self",
        "code": '"""\nProblem: Product of Array Except Self\nLink: https://leetcode.com/problems/product-of-array-except-self/\n\nTime Complexity: O(N)\nSpace Complexity: O(1)\n"""\nclass Solution:\n    def productExceptSelf(self, nums: list[int]) -> list[int]:\n        res = [1] * (len(nums))\n        prefix = 1\n        for i in range(len(nums)):\n            res[i] = prefix\n            prefix *= nums[i]\n        postfix = 1\n        for i in range(len(nums) - 1, -1, -1):\n            res[i] *= postfix\n            postfix *= nums[i]\n        return res\n'
    }
]

def run_git(args):
    subprocess.run(["git"] + args, check=True)

# Set remote origin
try:
    run_git(["remote", "add", "origin", "https://github.com/Megesh07/DSA_Python.git"])
except:
    pass

for p in problems:
    filepath = os.path.join(p["folder"], p["filename"])
    with open(filepath, "w") as f:
        f.write(p["code"])
    
    # Track progress
    with open("progress.md", "a") as f:
        f.write(f"| 2026-06-06 | {p['folder']} | {p['title']} | Complete |\\n")
    
    # Commit
    run_git(["add", filepath])
    run_git(["add", "progress.md"])
    run_git(["commit", "-m", f"Solve {p['title']}"])

# Commit first file that was made manually earlier
try:
    run_git(["add", "Arrays/01_contains_duplicate.py"])
    run_git(["commit", "-m", "Solve Contains Duplicate"])
except:
    pass

# Push all to remote
print("Pushing to GitHub...")
run_git(["branch", "-M", "main"])
run_git(["push", "-u", "origin", "main"])
print("Successfully pushed batch to GitHub.")
