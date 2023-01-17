# link: https://leetcode.com/problems/flip-string-to-monotone-increasing/

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        zeros = [0] * (n+1)
        for i in range(n):
            zeros[i+1] = zeros[i] + int(s[i] == '0')

        result = n
        for i in range(n+1):
            result = min(result, i - zeros[i] + zeros[n] - zeros[i])

        return result

