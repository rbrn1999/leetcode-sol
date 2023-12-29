# link: https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        right = s[1:].count('1')
        left = int(s[0] == '0')
        score = left + right

        for c in s[1:-1]:
            if c == '0':
                left += 1
            else:
                right -= 1
            score = max(score, left + right)
        
        return score