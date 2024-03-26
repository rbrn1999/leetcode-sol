# link: https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] >= n+1:
                nums[i] = 0

        for i in range(n):
            num = abs(nums[i])
            if num > 0:
                 # not modify if nums[num-1] is already negative
                if nums[num-1] == 0:
                    nums[num-1] = -num
                elif nums[num-1] > 0:
                    nums[num-1] = -nums[num-1]

        for i in range(n):
            if nums[i] >= 0:
                return i + 1

        return n+1
