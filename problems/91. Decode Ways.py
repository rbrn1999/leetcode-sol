# link: https://leetcode.com/problems/decode-ways/



'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def numDecodings(self, s: str) -> int: # need to review how does this avoid invalid cases (return 0)
        if s[0] == '0':
            return 0
        prev = [1, 1]
        for i in range(1, len(s)): 
            cur = prev[1] if s[i] != '0' else 0
            if 10 <= int(s[i-1:i+1]) <= 26:
                cur += prev[0]
            prev = [prev[1], cur]
        
        return prev[1]


'''
Time Complexity: O(n)
Space Complexity: O(n)
'''
# solution reference: https://leetcode.com/problems/decode-ways/discuss/30358/
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         dp = len(s) * [0]
#         dp[0] = 1 if s[0] != '0' else 0
#         for i in range(1, len(s)):
#             if s[i] != '0':
#                 dp[i] += dp[i-1]
#             if 10 <= int(s[i-1:i+1]) <= 26:
#                 if i < 2:
#                     dp[i] += 1
#                 else:
#                     dp[i] += dp[i-2]

#         return dp[-1]

