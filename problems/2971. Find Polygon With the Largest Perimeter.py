# link: https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        p = sum(nums)
        nums.sort(reverse=True)
        for num in nums[:-2]:
            if p - num > num:
                return p
            else:
                p -= num
        
        return -1