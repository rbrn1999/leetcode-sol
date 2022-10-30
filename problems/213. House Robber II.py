# link: https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: list[int]) -> int:
        # first ~ last-1
        prev = [0, 0]
        for i in range(max(len(nums)-1, 1)):
            cur = max(nums[i] + prev[0], prev[1])
            prev = [prev[1], cur]
        res = max(prev)
        # second ~ last
        prev = [0, 0]
        for i in range(1, len(nums)):
            cur = max(nums[i] + prev[0], prev[1])
            prev = [prev[1], cur]
        return max(res, prev[1])


# from functools import cache
# class Solution:
#     def rob(self, nums: list[int]) -> int:
#         @cache
#         def helper(i, robFirst):
#             if i>= len(nums) or (robFirst and i == len(nums)-1):
#                 return 0
#             if robFirst and i == 0:
#                 return nums[i] + helper(i+2, robFirst)
#             else:
#                 return max(nums[i] + helper(i+2, robFirst), helper(i+1, robFirst))
        
#         return max(helper(0, True), helper(1, False)) if len(nums) > 1 else nums[0]