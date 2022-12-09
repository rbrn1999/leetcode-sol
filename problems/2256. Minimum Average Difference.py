# link: https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        n = len(nums)
        minimum = float('inf')
        index = -1

        for i in range(n):
            leftSum += nums[i]
            rightSum -= nums[i]
            if i != n-1:
                diff = abs(leftSum // (i+1) - rightSum // (n-(i+1)))
            else:
                diff = abs(leftSum // (i+1))

            if diff < minimum:
                minimum = diff
                index = i


        return index

