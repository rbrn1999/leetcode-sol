# link: https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        result = 0
        minVal = float('inf')
        maxVal = -float('inf')
        for array in arrays:
            result = max(result, maxVal-array[0], array[-1]-minVal)
            minVal = min(minVal, array[0])
            maxVal = max(maxVal, array[-1])

        return result if type(result) is int else 0
