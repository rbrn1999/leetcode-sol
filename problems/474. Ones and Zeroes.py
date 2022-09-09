# link: https://leetcode.com/problems/ones-and-zeroes/

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = [(s.count('0'), s.count('1')) for s in strs]
        
        @cache
        def dp(zeros, ones, pairCount):
            if zeros < 0 or ones < 0:
                return -float('inf')
            if pairCount == len(strs):
                return 0
            cur_zeros, cur_ones = counts[pairCount]
            return max(dp(zeros-cur_zeros, ones-cur_ones, pairCount+1)+1, dp(zeros, ones, pairCount+1))
        
        return dp(m, n, 0)