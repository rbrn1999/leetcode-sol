# link: https://leetcode.com/problems/132-pattern/

import math
class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        if len(nums)<3:
            return False
        second_num = -math.inf
        stack = []
        # Try to find nums[i] < second_num < stack[-1]
        for num in nums[::-1]:
            if num < second_num:
                return True
            # always ensure stack can be popped in increasing order
            while stack and stack[-1] < num:
                second_num = stack.pop()  # this will ensure second_num < stack[-1] for next iteration

            stack.append(num)
        return False