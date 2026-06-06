import os
import subprocess

problems = [
    # Two Pointers
    {
        "folder": "Two_Pointers",
        "filename": "03_3sum.py",
        "title": "3Sum",
        "code": 'class Solution:\n    def threeSum(self, nums: list[int]) -> list[list[int]]:\n        res = []\n        nums.sort()\n        for i, a in enumerate(nums):\n            if i > 0 and a == nums[i - 1]:\n                continue\n            l, r = i + 1, len(nums) - 1\n            while l < r:\n                threeSum = a + nums[l] + nums[r]\n                if threeSum > 0:\n                    r -= 1\n                elif threeSum < 0:\n                    l += 1\n                else:\n                    res.append([a, nums[l], nums[r]])\n                    l += 1\n                    while nums[l] == nums[l - 1] and l < r:\n                        l += 1\n        return res\n'
    },
    {
        "folder": "Two_Pointers",
        "filename": "04_container_with_most_water.py",
        "title": "Container With Most Water",
        "code": 'class Solution:\n    def maxArea(self, heights: list[int]) -> int:\n        res = 0\n        l, r = 0, len(heights) - 1\n        while l < r:\n            area = (r - l) * min(heights[l], heights[r])\n            res = max(res, area)\n            if heights[l] < heights[r]:\n                l += 1\n            else:\n                r -= 1\n        return res\n'
    },
    {
        "folder": "Two_Pointers",
        "filename": "05_trapping_rain_water.py",
        "title": "Trapping Rain Water",
        "code": 'class Solution:\n    def trap(self, heights: list[int]) -> int:\n        if not heights:\n            return 0\n        l, r = 0, len(heights) - 1\n        leftMax, rightMax = heights[l], heights[r]\n        res = 0\n        while l < r:\n            if leftMax < rightMax:\n                l += 1\n                leftMax = max(leftMax, heights[l])\n                res += leftMax - heights[l]\n            else:\n                r -= 1\n                rightMax = max(rightMax, heights[r])\n                res += rightMax - heights[r]\n        return res\n'
    },
    # Sliding Window
    {
        "folder": "Sliding_Window",
        "filename": "01_best_time_to_buy_and_sell_stock.py",
        "title": "Best Time to Buy and Sell Stock",
        "code": 'class Solution:\n    def maxProfit(self, prices: list[int]) -> int:\n        l, r = 0, 1\n        maxP = 0\n        while r < len(prices):\n            if prices[l] < prices[r]:\n                profit = prices[r] - prices[l]\n                maxP = max(maxP, profit)\n            else:\n                l = r\n            r += 1\n        return maxP\n'
    },
    {
        "folder": "Sliding_Window",
        "filename": "02_longest_substring_without_repeating_characters.py",
        "title": "Longest Substring Without Repeating Characters",
        "code": 'class Solution:\n    def lengthOfLongestSubstring(self, s: str) -> int:\n        charSet = set()\n        l = 0\n        res = 0\n        for r in range(len(s)):\n            while s[r] in charSet:\n                charSet.remove(s[l])\n                l += 1\n            charSet.add(s[r])\n            res = max(res, r - l + 1)\n        return res\n'
    },
    {
        "folder": "Sliding_Window",
        "filename": "03_longest_repeating_character_replacement.py",
        "title": "Longest Repeating Character Replacement",
        "code": 'class Solution:\n    def characterReplacement(self, s: str, k: int) -> int:\n        count = {}\n        res = 0\n        l = 0\n        maxf = 0\n        for r in range(len(s)):\n            count[s[r]] = 1 + count.get(s[r], 0)\n            maxf = max(maxf, count[s[r]])\n            while (r - l + 1) - maxf > k:\n                count[s[l]] -= 1\n                l += 1\n            res = max(res, r - l + 1)\n        return res\n'
    },
    {
        "folder": "Sliding_Window",
        "filename": "04_permutation_in_string.py",
        "title": "Permutation in String",
        "code": 'class Solution:\n    def checkInclusion(self, s1: str, s2: str) -> bool:\n        if len(s1) > len(s2):\n            return False\n        s1Count, s2Count = [0] * 26, [0] * 26\n        for i in range(len(s1)):\n            s1Count[ord(s1[i]) - ord("a")] += 1\n            s2Count[ord(s2[i]) - ord("a")] += 1\n        matches = 0\n        for i in range(26):\n            matches += (1 if s1Count[i] == s2Count[i] else 0)\n        l = 0\n        for r in range(len(s1), len(s2)):\n            if matches == 26:\n                return True\n            index = ord(s2[r]) - ord("a")\n            s2Count[index] += 1\n            if s1Count[index] == s2Count[index]:\n                matches += 1\n            elif s1Count[index] + 1 == s2Count[index]:\n                matches -= 1\n            index = ord(s2[l]) - ord("a")\n            s2Count[index] -= 1\n            if s1Count[index] == s2Count[index]:\n                matches += 1\n            elif s1Count[index] - 1 == s2Count[index]:\n                matches -= 1\n            l += 1\n        return matches == 26\n'
    },
    {
        "folder": "Sliding_Window",
        "filename": "05_minimum_window_substring.py",
        "title": "Minimum Window Substring",
        "code": 'class Solution:\n    def minWindow(self, s: str, t: str) -> str:\n        if t == "":\n            return ""\n        countT, window = {}, {}\n        for c in t:\n            countT[c] = 1 + countT.get(c, 0)\n        have, need = 0, len(countT)\n        res, resLen = [-1, -1], float("infinity")\n        l = 0\n        for r in range(len(s)):\n            c = s[r]\n            window[c] = 1 + window.get(c, 0)\n            if c in countT and window[c] == countT[c]:\n                have += 1\n            while have == need:\n                if (r - l + 1) < resLen:\n                    res = [l, r]\n                    resLen = r - l + 1\n                window[s[l]] -= 1\n                if s[l] in countT and window[s[l]] < countT[s[l]]:\n                    have -= 1\n                l += 1\n        l, r = res\n        return s[l : r + 1] if resLen != float("infinity") else ""\n'
    },
    {
        "folder": "Sliding_Window",
        "filename": "06_sliding_window_maximum.py",
        "title": "Sliding Window Maximum",
        "code": 'import collections\nclass Solution:\n    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:\n        output = []\n        q = collections.deque()\n        l = r = 0\n        while r < len(nums):\n            while q and nums[q[-1]] < nums[r]:\n                q.pop()\n            q.append(r)\n            if l > q[0]:\n                q.popleft()\n            if (r + 1) >= k:\n                output.append(nums[q[0]])\n                l += 1\n            r += 1\n        return output\n'
    },
    # Stack
    {
        "folder": "Stack",
        "filename": "01_valid_parentheses.py",
        "title": "Valid Parentheses",
        "code": 'class Solution:\n    def isValid(self, s: str) -> bool:\n        stack = []\n        closeToOpen = {")": "(", "]": "[", "}": "{"}\n        for c in s:\n            if c in closeToOpen:\n                if stack and stack[-1] == closeToOpen[c]:\n                    stack.pop()\n                else:\n                    return False\n            else:\n                stack.append(c)\n        return True if not stack else False\n'
    },
    {
        "folder": "Stack",
        "filename": "02_min_stack.py",
        "title": "Min Stack",
        "code": 'class MinStack:\n    def __init__(self):\n        self.stack = []\n        self.minStack = []\n    def push(self, val: int) -> None:\n        self.stack.append(val)\n        val = min(val, self.minStack[-1] if self.minStack else val)\n        self.minStack.append(val)\n    def pop(self) -> None:\n        self.stack.pop()\n        self.minStack.pop()\n    def top(self) -> int:\n        return self.stack[-1]\n    def getMin(self) -> int:\n        return self.minStack[-1]\n'
    },
    {
        "folder": "Stack",
        "filename": "03_evaluate_reverse_polish_notation.py",
        "title": "Evaluate Reverse Polish Notation",
        "code": 'class Solution:\n    def evalRPN(self, tokens: list[str]) -> int:\n        stack = []\n        for c in tokens:\n            if c == "+":\n                stack.append(stack.pop() + stack.pop())\n            elif c == "-":\n                a, b = stack.pop(), stack.pop()\n                stack.append(b - a)\n            elif c == "*":\n                stack.append(stack.pop() * stack.pop())\n            elif c == "/":\n                a, b = stack.pop(), stack.pop()\n                stack.append(int(b / a))\n            else:\n                stack.append(int(c))\n        return stack[0]\n'
    },
    {
        "folder": "Stack",
        "filename": "04_generate_parentheses.py",
        "title": "Generate Parentheses",
        "code": 'class Solution:\n    def generateParenthesis(self, n: int) -> list[str]:\n        stack = []\n        res = []\n        def backtrack(openN, closedN):\n            if openN == closedN == n:\n                res.append("".join(stack))\n                return\n            if openN < n:\n                stack.append("(")\n                backtrack(openN + 1, closedN)\n                stack.pop()\n            if closedN < openN:\n                stack.append(")")\n                backtrack(openN, closedN + 1)\n                stack.pop()\n        backtrack(0, 0)\n        return res\n'
    },
    {
        "folder": "Stack",
        "filename": "05_daily_temperatures.py",
        "title": "Daily Temperatures",
        "code": 'class Solution:\n    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:\n        res = [0] * len(temperatures)\n        stack = []\n        for i, t in enumerate(temperatures):\n            while stack and t > stack[-1][0]:\n                stackT, stackInd = stack.pop()\n                res[stackInd] = i - stackInd\n            stack.append((t, i))\n        return res\n'
    },
    {
        "folder": "Stack",
        "filename": "06_car_fleet.py",
        "title": "Car Fleet",
        "code": 'class Solution:\n    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:\n        pair = [(p, s) for p, s in zip(position, speed)]\n        pair.sort(reverse=True)\n        stack = []\n        for p, s in pair:\n            stack.append((target - p) / s)\n            if len(stack) >= 2 and stack[-1] <= stack[-2]:\n                stack.pop()\n        return len(stack)\n'
    },
    {
        "folder": "Stack",
        "filename": "07_largest_rectangle_in_histogram.py",
        "title": "Largest Rectangle in Histogram",
        "code": 'class Solution:\n    def largestRectangleArea(self, heights: list[int]) -> int:\n        maxArea = 0\n        stack = [] # pair: (index, height)\n        for i, h in enumerate(heights):\n            start = i\n            while stack and stack[-1][1] > h:\n                index, height = stack.pop()\n                maxArea = max(maxArea, height * (i - index))\n                start = index\n            stack.append((start, h))\n        for i, h in stack:\n            maxArea = max(maxArea, h * (len(heights) - i))\n        return maxArea\n'
    },
    # Binary Search
    {
        "folder": "Binary_Search",
        "filename": "01_binary_search.py",
        "title": "Binary Search",
        "code": 'class Solution:\n    def search(self, nums: list[int], target: int) -> int:\n        l, r = 0, len(nums) - 1\n        while l <= r:\n            m = l + ((r - l) // 2)\n            if nums[m] > target:\n                r = m - 1\n            elif nums[m] < target:\n                l = m + 1\n            else:\n                return m\n        return -1\n'
    },
    {
        "folder": "Binary_Search",
        "filename": "02_search_a_2d_matrix.py",
        "title": "Search a 2D Matrix",
        "code": 'class Solution:\n    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:\n        ROWS, COLS = len(matrix), len(matrix[0])\n        top, bot = 0, ROWS - 1\n        while top <= bot:\n            row = (top + bot) // 2\n            if target > matrix[row][-1]:\n                top = row + 1\n            elif target < matrix[row][0]:\n                bot = row - 1\n            else:\n                break\n        if not (top <= bot):\n            return False\n        row = (top + bot) // 2\n        l, r = 0, COLS - 1\n        while l <= r:\n            m = (l + r) // 2\n            if target > matrix[row][m]:\n                l = m + 1\n            elif target < matrix[row][m]:\n                r = m - 1\n            else:\n                return True\n        return False\n'
    },
    {
        "folder": "Binary_Search",
        "filename": "03_koko_eating_bananas.py",
        "title": "Koko Eating Bananas",
        "code": 'import math\nclass Solution:\n    def minEatingSpeed(self, piles: list[int], h: int) -> int:\n        l, r = 1, max(piles)\n        res = r\n        while l <= r:\n            k = (l + r) // 2\n            totalTime = 0\n            for p in piles:\n                totalTime += math.ceil(float(p) / k)\n            if totalTime <= h:\n                res = min(res, k)\n                r = k - 1\n            else:\n                l = k + 1\n        return res\n'
    },
    {
        "folder": "Binary_Search",
        "filename": "04_find_minimum_in_rotated_sorted_array.py",
        "title": "Find Minimum in Rotated Sorted Array",
        "code": 'class Solution:\n    def findMin(self, nums: list[int]) -> int:\n        res = nums[0]\n        l, r = 0, len(nums) - 1\n        while l <= r:\n            if nums[l] < nums[r]:\n                res = min(res, nums[l])\n                break\n            m = (l + r) // 2\n            res = min(res, nums[m])\n            if nums[m] >= nums[l]:\n                l = m + 1\n            else:\n                r = m - 1\n        return res\n'
    },
    {
        "folder": "Binary_Search",
        "filename": "05_search_in_rotated_sorted_array.py",
        "title": "Search in Rotated Sorted Array",
        "code": 'class Solution:\n    def search(self, nums: list[int], target: int) -> int:\n        l, r = 0, len(nums) - 1\n        while l <= r:\n            mid = (l + r) // 2\n            if target == nums[mid]:\n                return mid\n            if nums[l] <= nums[mid]:\n                if target > nums[mid] or target < nums[l]:\n                    l = mid + 1\n                else:\n                    r = mid - 1\n            else:\n                if target < nums[mid] or target > nums[r]:\n                    r = mid - 1\n                else:\n                    l = mid + 1\n        return -1\n'
    },
    {
        "folder": "Binary_Search",
        "filename": "06_time_based_key_value_store.py",
        "title": "Time Based Key-Value Store",
        "code": 'class TimeMap:\n    def __init__(self):\n        self.store = {} # key: list of [val, timestamp]\n    def set(self, key: str, value: str, timestamp: int) -> None:\n        if key not in self.store:\n            self.store[key] = []\n        self.store[key].append([value, timestamp])\n    def get(self, key: str, timestamp: int) -> str:\n        res = ""\n        values = self.store.get(key, [])\n        l, r = 0, len(values) - 1\n        while l <= r:\n            m = (l + r) // 2\n            if values[m][1] <= timestamp:\n                res = values[m][0]\n                l = m + 1\n            else:\n                r = m - 1\n        return res\n'
    },
    {
        "folder": "Binary_Search",
        "filename": "07_median_of_two_sorted_arrays.py",
        "title": "Median of Two Sorted Arrays",
        "code": 'class Solution:\n    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:\n        A, B = nums1, nums2\n        total = len(nums1) + len(nums2)\n        half = total // 2\n        if len(B) < len(A):\n            A, B = B, A\n        l, r = 0, len(A) - 1\n        while True:\n            i = (l + r) // 2\n            j = half - i - 2\n            Aleft = A[i] if i >= 0 else float("-infinity")\n            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")\n            Bleft = B[j] if j >= 0 else float("-infinity")\n            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")\n            if Aleft <= Bright and Bleft <= Aright:\n                if total % 2:\n                    return min(Aright, Bright)\n                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2\n            elif Aleft > Bright:\n                r = i - 1\n            else:\n                l = i + 1\n'
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
