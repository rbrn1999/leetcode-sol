# link: https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

class Solution:
    def averageValue(self, nums: list[int]) -> int:
        nums = [num for num in nums if num % 6 == 0]
        return sum(nums)//len(nums) if len(nums) > 0 else 0