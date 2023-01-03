# link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints[:k])
        result = total
        for i in range(k):
            total = total - cardPoints[k-1-i] + cardPoints[n-1-i]
            result = max(result, total)
        return result
