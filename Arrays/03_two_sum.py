"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/

Time Complexity: O(N)
Space Complexity: O(N)
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {} # val -> index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []
