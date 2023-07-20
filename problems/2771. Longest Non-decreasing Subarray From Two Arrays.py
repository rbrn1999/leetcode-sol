# link: https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

# space: O(n)
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[1]*n for _ in range(2)] 
        # dp[0][i] the max sub sequence ends at nums1[i]
        # dp[1][i] the max sub sequence ends at nums2[i]
        for i in range(1, n):
            if nums1[i] >= nums1[i-1]:
                dp[0][i] = max(dp[0][i], dp[0][i-1]+1)
            if nums1[i] >= nums2[i-1]:
                dp[0][i] = max(dp[0][i], dp[1][i-1]+1)
            if nums2[i] >= nums1[i-1]:
                dp[1][i] = max(dp[1][i], dp[0][i-1]+1)
            if nums2[i] >= nums2[i-1]:
                dp[1][i] = max(dp[1][i], dp[1][i-1]+1)
        
        return max(max(l) for l in dp)

# space: O(1)
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        answer = 1
        dp1 = 1 # prev length ends at nums1 
        dp2 = 1 # prev length ends at nums1 
        for i in range(1, n):
            temp11 = dp1 + 1 if nums1[i] >= nums1[i-1] else 1
            temp21 = dp2 + 1 if nums1[i] >= nums2[i-1] else 1
            temp12 = dp1 + 1 if nums2[i] >= nums1[i-1] else 1
            temp22 = dp2 + 1 if nums2[i] >= nums2[i-1] else 1
            dp1 = max(temp11, temp21)
            dp2 = max(temp12, temp22)
            answer = max(answer, dp1, dp2)
        
        return answer
            