# link: https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1) #dp[i]: can solve at i, the maximum point from [0, i)
        for i in range(n):
            index = min(n, i+questions[i][1]+1)
            dp[i] = max(dp[i], dp[i-1] if i > 0 else 0)
            dp[index] = max(dp[i] + questions[i][0], dp[index])

        return dp[n]

