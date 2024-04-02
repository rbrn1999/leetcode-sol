# link: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        result = 0
        freq = defaultdict(int)
        l = 0
        for r in range(len(nums)):
            freq[nums[r]] += 1
            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        
        return result