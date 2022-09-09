# link: https://leetcode.com/problems/longest-increasing-subsequence/
# solution reference: https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)

from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
#         dp
#         n = len(nums)
#         dp = [1] * n
#         for i in range(n):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j]+1)
        
#         return max(dp)

#       Greedy with Binary Search
        sub = []
        for num in nums:
            if not sub or sub[-1] < num:
                sub.append(num)
            else:
                idx = bisect_left(sub, num)
                sub[idx] = num
        return len(sub)