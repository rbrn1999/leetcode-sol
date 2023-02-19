# link: https://leetcode.com/problems/minimum-impossible-or/

class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        nums = set(nums)
        if 1 not in nums:
            return 1

        num = 2

        while num in nums:
            num *= 2

        return num

