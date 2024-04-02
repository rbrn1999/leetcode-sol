# link: https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        n = len(nums)
        l = 0
        product = 1
        result = 0
        for r in range(n):
            product *= nums[r]
            while l <= r and product >= k:
                product //= nums[l]
                l += 1

            if l <= r:
                result += (r - l + 1)

        return result
