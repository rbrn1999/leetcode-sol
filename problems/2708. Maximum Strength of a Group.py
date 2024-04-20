class Solution:
    def maxStrength(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        result = 1
        negCount = 0
        maxNeg = -float('inf')
        zeros = 0
        for num in nums:
            if num > 0:
                result *= num
            elif num < 0:
                result *= num
                negCount += 1
                maxNeg = max(maxNeg, num)
            else:
                zeros += 1

        if negCount == 1 and zeros == len(nums) - 1 or zeros == len(nums):
            return 0

        if negCount % 2 == 1:
            result //= maxNeg

        return result
