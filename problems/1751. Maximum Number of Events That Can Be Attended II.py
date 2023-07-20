# link: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

import bisect
from functools import cache
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        answer = 0
        @cache
        def dfs(i, k):
            if k == 0 or i == len(events):
                return 0
            j = bisect.bisect_right(events, events[i][1], key=lambda x: x[0])
            return max(events[i][2] + dfs(j, k-1), dfs(i+1, k))

        return dfs(0, k)

