# link: https://leetcode.com/problems/missing-ranges/

class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        if not nums:
            return [[lower, upper]]
        result = []
        nums.sort()
        if lower < nums[0]:
            result.append([lower, nums[0]-1])

        for i in range(1, len(nums)):
            if nums[i] - 1 > nums[i-1]:
                result.append([nums[i-1]+1, nums[i]-1])

        if nums[-1] < upper:
            result.append([nums[-1]+1, upper])

        return result
