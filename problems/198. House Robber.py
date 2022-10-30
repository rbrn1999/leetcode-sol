# link: https://leetcode.com/problems/house-robber/

'''
solution reference: https://youtu.be/73r3KWiEvyk
Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def rob(self, nums: list[int]) -> int:
        prev = [0, 0] # _, _, cur => prev records the max that "may" contain itself
        
        for num in nums:
            cur = max(prev[0] + num, prev[1])
            prev = [prev[1], cur]
        
        return prev[1]

'''
Time Complexity: O(n)
Space Complexity: O(n)
'''
# from functools import cache
# class Solution:
#     def rob(self, nums: list[int]) -> int:
#         @cache
#         def helper(i):
#             if i >= len(nums):
#                 return 0
#             return max(nums[i] + helper(i+2), helper(i+1))
#         return helper(0)