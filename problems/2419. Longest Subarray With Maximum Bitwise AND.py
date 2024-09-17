# link: https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_num = 0
        max_length = 0
        i = 0
        while i < len(nums):
            if nums[i] < max_num:
                i += 1
                continue
            if nums[i] > max_num:
                max_num = nums[i]
                max_length = 0

            j = i + 1
            while j < len(nums) and nums[j] == max_num:
                j += 1

            max_length = max(max_length, j-i)
            i = j

        return max_length
