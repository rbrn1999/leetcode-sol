# link: https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        min_len = float('inf')
        cur_sum = 0
        l = 0
        for r in range(0, n):
            cur_sum += nums[r]
            while l <= r and cur_sum >= target:
                min_len = min(min_len, r - l + 1)
                cur_sum -= nums[l]
                l += 1

        return min_len if min_len < float('inf') else 0

