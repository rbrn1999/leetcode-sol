# link: https://leetcode.com/problems/most-profit-assigning-work/

# Sort, Greedy
class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        worker.sort()
        jobs = sorted(zip(difficulty, profit), reverse=True)
        maxProfit = 0
        totalProfit = 0

        for w in worker:
            while jobs and jobs[-1][0] <= w:
                maxProfit = max(maxProfit, jobs.pop()[1])

            totalProfit += maxProfit

        return totalProfit

# Memoization
class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        max_ability = max(worker)
        jobs = [0] * (max_ability + 1)

        for i in range(len(profit)):
            if difficulty[i] > max_ability:
                continue
            jobs[difficulty[i]] = max(jobs[difficulty[i]], profit[i])

        for i in range(1, max_ability + 1):
            jobs[i] = max(jobs[i], jobs[i-1])

        total_profit = 0
        for ability in worker:
            total_profit += jobs[ability]

        return total_profit
