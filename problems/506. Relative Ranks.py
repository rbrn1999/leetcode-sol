# link: https://leetcode.com/problems/relative-ranks/

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_score = sorted([(score, i) for i, score in enumerate(score)], reverse=True)
        result = [''] * len(score)

        for j in range(len(score)):
            _, i = sorted_score[j]
            if j > 2:
                result[i] = str(j+1)
            elif j == 0:
                result[i] = "Gold Medal"
            elif j == 1:
                result[i] = "Silver Medal"
            elif j == 2:
                result[i] = "Bronze Medal"

        return result
