"""
Problem: Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Time Complexity: O(N)
Space Complexity: O(N)
"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
