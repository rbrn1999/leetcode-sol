# link: https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        results = [[]]
        for num in nums:
            results += [[num] + r for r in results]
        return results
        