# Bottom-Up
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # low and high are 1-indexed
        dp = [1] + [0] * high # dp[i]: combinations of [0~i)
        for i in range(high+1):
            if i + zero <= high:
                dp[i+zero] = (dp[i+zero] + dp[i]) % (10**9 + 7)
            if i + one <= high:
                dp[i+one] = (dp[i+one] + dp[i]) % (10**9 + 7)
                
        # dp offset: +1, low-high offset: +1 -> cancelled out
        return sum(dp[low:]) % (10**9 + 7)
    

# Top-Down
# from functools import cache
# class Solution:
#     def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
#         @cache
#         def dfs(i: int) -> int:
#             if i > high:
#                 return 0
#             count = dfs(i+zero) + dfs(i+one)
#             if i >= low:
#                 count += 1
#             return count % (10**9 + 7)
        
#         return dfs(0)