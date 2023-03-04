# link: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        subArrayCount = 0
        leftBound = minInd = maxInd = -1
        for rightBound in range(len(nums)): # subarray range: (leftBound, rightBound]
            if nums[rightBound] < minK or nums[rightBound] > maxK:
                leftBound = rightBound
            if nums[rightBound] == minK:
                minInd = rightBound
            if nums[rightBound] == maxK:
                maxInd = rightBound

            left, right = min(minInd, maxInd), max(minInd, maxInd)
            if left > leftBound:
                subArrayCount += left - leftBound

        return subArrayCount

