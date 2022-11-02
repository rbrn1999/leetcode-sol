# link: https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = [intervals.pop(0)]
        for start, end in intervals:
            if start == res[-1][0]:
                continue
            elif start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        
        return res