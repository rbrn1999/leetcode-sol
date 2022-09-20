# link: https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# solution reference: https://leetcode.com/problems/maximum-length-of-repeated-subarray/discuss/1324248

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0]*(n) for _ in range(m)]
        result = 0
        
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[i][j] = (dp[i-1][j-1] if i>0 and j>0 else 0) + 1
                else:
                    dp[i][j] = 0
                result = max(result, dp[i][j])
        return result
