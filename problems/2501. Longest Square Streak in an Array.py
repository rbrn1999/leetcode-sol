# link: https://leetcode.com/problems/longest-square-streak-in-an-array/

class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_streak = 0
        for num in nums:
            streak = 1
            while num * num in num_set:
                streak += 1
                num *= num
            max_streak = max(max_streak, streak)

        return max_streak if max_streak > 1 else -1


import math
class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        num_streak = {}
        nums = sorted(set(nums))
        for num in nums:
            temp = int(math.sqrt(num))
            if temp * temp == num and temp in num_streak:
               num_streak[num] = num_streak[temp] + 1
            else:
                num_streak[num] = 1

        max_streak = max(num_streak.values())
        return max_streak if max_streak > 1 else -1
