# link: https://leetcode.com/problems/subsets-ii/

from collections import Counter
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        numCounts = Counter(nums)
        result = [[]]
        for num in numCounts:
            n = len(result)
            for i in range(n):
                for count in range(1, numCounts[num]+1):
                    result.append(result[i] + [num]*count)

        return result

