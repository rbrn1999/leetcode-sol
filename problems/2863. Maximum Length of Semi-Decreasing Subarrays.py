# link: https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

class Solution:
    def maxSubarrayLength(self, nums: list[int]) -> int:
        starting_index = [] # monotonic increasing
        max_length = 0

        for i, num in enumerate(nums):
            if not starting_index or nums[starting_index[-1]] < num:
                starting_index.append(i)

        for end in range(len(nums)-1, 0, -1):
            while starting_index and nums[starting_index[-1]] > nums[end]:
                max_length = max(max_length, end - starting_index.pop() + 1)

        return max_length
