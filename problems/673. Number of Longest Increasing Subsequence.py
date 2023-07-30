# link: https://leetcode.com/problems/number-of-longest-increasing-subsequence/
class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        lengths = [1] * n
        ways = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                if lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
                    ways[i] = ways[j]
                elif lengths[i] == lengths[j] + 1:
                    ways[i] += ways[j]
                
        max_length = max(lengths)
        return sum(ways[i] for i in range(n) if lengths[i] == max_length)