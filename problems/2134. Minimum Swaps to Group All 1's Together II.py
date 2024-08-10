# link: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        window_size = sum(nums)
        if window_size == len(nums) or window_size == 0:
            return 0

        one_count = sum(nums[:window_size])
        min_count = window_size - one_count

        for i in range(len(nums)):
            one_count -= nums[i]
            one_count += nums[(i+window_size) % len(nums)]
            min_count = min(min_count, window_size - one_count)

        return min_count
