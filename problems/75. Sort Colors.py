# link: https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colorCount = [0] * 3
        for num in nums:
            colorCount[num] += 1
        i = 0
        for color in range(len(colorCount)):
            nums[i:i+colorCount[color]] = [color] * colorCount[color]
            i += colorCount[color]

