# link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# solution reference: https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/409009/
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        memo = [[0, 0]]
        for start, end, profit in jobs:
            ind = bisect.bisect(memo, [start + 1, 0]) - 1
            if memo[ind][1] + profit > memo[-1][1]:
                memo.append([end, memo[ind][1] + profit])

        return memo[-1][1]
