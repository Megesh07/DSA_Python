class Solution:
    def trap(self, heights: list[int]) -> int:
        if not heights:
            return 0
        l, r = 0, len(heights) - 1
        leftMax, rightMax = heights[l], heights[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, heights[l])
                res += leftMax - heights[l]
            else:
                r -= 1
                rightMax = max(rightMax, heights[r])
                res += rightMax - heights[r]
        return res
