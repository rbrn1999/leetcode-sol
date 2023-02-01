# link: https://leetcode.com/problems/best-team-with-no-conflicts/

from functools import cache
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        scores = [score for _, score in sorted(zip(ages, scores))]
        dp = scores.copy()

        for cur in range(n):
            for prev in range(cur):
                if scores[cur] >= scores[prev]:
                    dp[cur] = max(dp[cur], dp[prev] + scores[cur])

        return max(dp)
