# link: https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

class Solution:
    def findIndices(self, nums: list[int], indexDifference: int, valueDifference: int) -> list[int]:
        m, M = (float('inf'), -1), (-float('inf'), -1)
        prefix = []
        for i, num in enumerate(nums):
            if num < m[0]:
                m = (num, i)
            if num > M[0]:
                M = (num, i)
            prefix.append((m, M))
        
        for j in range(indexDifference, len(nums)):
            k = j - indexDifference
            m, i = prefix[k][0]
            if abs(nums[j] - m) >= valueDifference:
                return [i, j]
            M, i = prefix[k][1]
            if abs(nums[j] - M) >= valueDifference:
                return [i, j]
        
        return [-1, -1]