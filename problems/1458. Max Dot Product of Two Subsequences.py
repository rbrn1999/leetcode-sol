# link: https://leetcode.com/problems/max-dot-product-of-two-subsequences/

# Top-Down
from functools import cache
class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        if all(num >= 0 for num in nums1) and all(num <= 0 for num in nums2):
            return min(nums1) * max(nums2)
        if all(num <= 0 for num in nums1) and all(num >= 0 for num in nums2):
            return max(nums1) * min(nums2)
        
        answer = -float('inf')

        @cache
        def dfs(i: int, j: int) -> int:
            if i == len(nums1) or j == len(nums2):
                return 0
            result = 0
            if nums1[i] * nums2[j] > 0:
                result = nums1[i] * nums2[j] + dfs(i+1, j+1)
            result = max(result, dfs(i+1, j), dfs(i, j+1))
            return result
        
        return dfs(0, 0)

# Bottom-Up
class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        if all(num >= 0 for num in nums1) and all(num <= 0 for num in nums2):
            return min(nums1) * max(nums2)
        if all(num <= 0 for num in nums1) and all(num >= 0 for num in nums2):
            return max(nums1) * min(nums2)
        
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        dp = [0] * (n+1)

        for row in range(m):
            prev = dp.copy()
            dp = [0] * (n+1)
            for col in range(n):
                dp[col+1] = max(max(nums1[row] * nums2[col], 0) + prev[col], dp[col], prev[col+1])
        
        return dp[-1]