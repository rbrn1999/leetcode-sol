# link: https://leetcode.com/problems/longest-increasing-subsequence/

'''
Dynamic Programming
Time Complexity: O(nlogn)
Space Complexity: O(n)
'''
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        memo = [1] * len(nums)
        for i, num in enumerate(nums):
            curLen = 1
            for j in range(i):
                if num > nums[j]:
                    curLen = max(curLen, memo[j] + 1)
            memo[i] = curLen
        
        return max(memo)

'''
Greedy with Binary Search
Time Complexity: O(nlogn)
Space Complexity: O(n)
solution reference: https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308
'''
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        sub = []
        for num in nums:
            if not sub or sub[-1] < num:
                sub.append(num)
            else:
                idx = bisect_left(sub, num)
                sub[idx] = num
        return len(sub)