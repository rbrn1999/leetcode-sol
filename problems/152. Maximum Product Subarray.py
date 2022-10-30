# link: https://leetcode.com/problems/maximum-product-subarray/
# solution reference: https://youtu.be/lXVy6YWFcRM
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        
        for num in nums:
            if num == 0:
                curMin = curMax = 1
                continue
            curMax, curMin = max(num*curMax, num*curMin, num), min(num*curMax, num*curMin, num)
            res = max(res, curMax)
        
        return res
    