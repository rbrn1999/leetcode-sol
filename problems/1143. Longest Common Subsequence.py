# link: https://leetcode.com/problems/longest-common-subsequence/

'''
top-bottom dynamic programming
Time Complexity: O(m*n)
Space Complexity: O(m*n)
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = {}
        def helper(i, j):
            if i < 0 or j < 0:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            length = 0
            if text1[i] == text2[j]:
                length = helper(i-1, j-1) + 1
            else:
                length = max(helper(i-1, j), helper(i, j-1)) # two different routes
                
            memo[(i, j)] = length
            return length
        
        return helper(m-1, n-1)