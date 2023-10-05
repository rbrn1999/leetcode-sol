# link: https://leetcode.com/problems/132-pattern/


# Approach 23/09/30
class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        intervals = [[float('inf'), float('inf')]]
        for num in nums:
            if num < intervals[-1][0]:
                if intervals[-1][0] == intervals[-1][1]:
                    intervals[-1] = [num, num]
                else:
                    intervals.append([num, num])
            elif num > intervals[-1][0]:
                temp = [intervals[-1][0], num]
                while intervals and num > intervals[-1][0]:
                    first, second = intervals.pop()
                    if num < second:
                        return True
                intervals.append(temp)
            else:
                pass
        
        return False
    
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