# link: https://leetcode.com/problems/average-waiting-time/

class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        totalTime = 0
        currentTime = 0
        for arrive, timeCost in customers:
            totalTime += max(currentTime-arrive, 0) + timeCost
            currentTime = max(currentTime, arrive) + timeCost

        return totalTime / len(customers)
