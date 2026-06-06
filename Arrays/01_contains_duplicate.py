"""
Problem: Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Approach:
We can use a hash set to keep track of the numbers we have seen so far.
As we iterate through the array, if we encounter a number that is already in the set, we know there is a duplicate and we can return True.
If we finish iterating through the array without finding any duplicates, we return False.

Time Complexity: O(N) where N is the length of the array. We iterate through the array once.
Space Complexity: O(N) where N is the length of the array. In the worst case, all elements are unique and we store them all in the hash set.
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
