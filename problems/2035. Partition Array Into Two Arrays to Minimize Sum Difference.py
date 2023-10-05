# link: https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

import bisect
class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n = len(nums) // 2
        total = sum(nums)
        target = total / 2

        dp1 = [set() for _ in range(n + 1)]
        dp2 = [set() for _ in range(n + 1)]

        stack = []
        def dfs(i: int, end: int, dp: list[list[int]], cur: int = 0):
            dp[len(stack)].add(cur)
            if i > end:
                return
            for i in range(i, end+1):
                stack.append(nums[i])
                cur += nums[i]
                dfs(i+1, end, dp, cur)
                cur -= nums[i]
                stack.pop()
        
        dfs(0, n-1, dp1)
        dfs(n, 2*n-1, dp2)
        dp2 = [sorted(s) for s in dp2]

        answer = float('inf')
        for k in range(n+1):
            for first in dp1[k]:
                i = bisect.bisect_left(dp2[n-k], target - first)
                if i < len(dp2[n-k]):
                    second = dp2[n-k][i]
                    part_1 = first + second
                    part_2 = total - part_1
                    answer = min(answer, abs(part_1 - part_2))
                if i + 1 < len(dp2[n-k]):
                    second = dp2[n-k][i+1]
                    part_1 = first + second
                    part_2 = total - part_1
                    answer = min(answer, abs(part_1 - part_2))
                
        return answer