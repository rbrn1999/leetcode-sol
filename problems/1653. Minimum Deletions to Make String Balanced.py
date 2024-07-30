# link: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

# Optimzed DP
class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = [0, 0]
        for c in s:
            next_dp = [0, 0]
            if c == 'a':
                next_dp[0] = dp[0]
                next_dp[1] = min(dp) + 1
            else:
                next_dp[0] = dp[0] + 1
                next_dp[1] = min(dp)
            dp = next_dp
        
        return min(dp)

# Counting
class Solution:
    def minimumDeletions(self, s: str) -> int:
        minCount = float('inf')
        n = len(s)
        aCount = []
        cur_count = 0
        for char in s:
            if char == 'a':
                cur_count += 1
            aCount.append(cur_count)

        result = n
        # edge case: whole string is b portion
        result = min(result, aCount[n-1])
        for i in range(n): # i: 0~i: a portion (inclusive)
            cur_delete_count = (i + 1 - aCount[i]) + (aCount[n-1] - aCount[i])
            result = min(result, cur_delete_count)

        return result

