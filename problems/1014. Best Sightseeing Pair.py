# link: https://leetcode.com/problems/best-sightseeing-pair/description/?envType=study-plan&id=dynamic-programming-i

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        best_i = 0
        maxScore = 1
        for i in range(n-1):
            j = i+1
            if values[i]+i > values[best_i] + best_i:
                best_i = i
            maxScore = max(maxScore, values[best_i]+values[j]+best_i-j)

        return maxScore

