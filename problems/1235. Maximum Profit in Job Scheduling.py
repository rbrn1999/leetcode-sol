# link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/

# Top-Down DP
from functools import cache
import bisect
class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))

        @cache
        def helper(i: int) -> int:
            if i == len(jobs):
                return 0

            # skip this job
            p = helper(i+1)

            # take this job
            j = bisect.bisect(jobs, (jobs[i][1], -1, -1))
            p = max(p, jobs[i][2] + helper(j))

            return p
        
        return helper(0)

# solution reference: https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/409009/
class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        memo = [[0, 0]]
        for start, end, profit in jobs:
            ind = bisect.bisect(memo, [start + 1, 0]) - 1
            if memo[ind][1] + profit > memo[-1][1]:
                memo.append([end, memo[ind][1] + profit])

        return memo[-1][1]
