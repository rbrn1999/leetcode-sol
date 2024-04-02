# link: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

from collections import defaultdict
class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        target = max(nums)
        less_than_k = 0
        l = 0
        freq = 0
        for r in range(n):
            if nums[r] == target:
                freq += 1
            while freq >= k:
                if nums[l] == target:
                    freq -= 1
                l += 1

            less_than_k += (r - l + 1)

        return n * (n-1) // 2 + n - less_than_k
