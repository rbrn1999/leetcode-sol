# link: https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

class Solution:
    def findIndices(self, nums: list[int], indexDifference: int, valueDifference: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+indexDifference, n):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        
        return [-1, -1]