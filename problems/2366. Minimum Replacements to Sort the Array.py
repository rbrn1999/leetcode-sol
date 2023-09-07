# link: https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

import math
class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        right = nums[-1]
        ops = 0
        for i in range(len(nums)-2, -1, -1):
            parts = math.ceil(nums[i]/right)
            right = nums[i] // parts # distribute as even as possible
            ops += parts - 1
        
        return ops