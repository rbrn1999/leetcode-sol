#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
# link: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

# @lc code=start
class Solution:
     def maxLength(self, arr: list[str]) -> int:
        max_len = 0
        def dfs(i, charSet):
            if len(set(arr[i])) < len(arr[i]):
                return
            if any(c in charSet for c in arr[i]):
                return
            charSet.update([c for c in arr[i]])
            nonlocal max_len
            max_len = max(max_len, len(charSet))
            for j in range(i+1, len(arr)):
                dfs(j, charSet.copy())
                
        for i in range(len(arr)):
            dfs(i, set())
        return max_len
# @lc code=end

