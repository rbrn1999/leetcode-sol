# link: https://leetcode.com/problems/maximum-width-ramp/

class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        # i: 0
        # i+1: 1
        # we will always choose index i as the starting point instead of index i+1

        stack = [] # strictly decreasing of (index's value)
        max_width = 0

        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)


        for i in range(len(nums)-1, 0, -1):
            width = 0
            while stack and nums[stack[-1]] <= nums[i]:
                width = i - stack.pop()
            
            max_width = max(max_width, width)
            
        
        return max_width