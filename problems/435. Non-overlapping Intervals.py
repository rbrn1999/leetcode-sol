# link:https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        prevEnd = intervals.pop(0)[1]
        
        count = 0
        for start, end in intervals:
            if start >= prevEnd: # no overlapp
                prevEnd = end 
            else: # remove the one with the larger end point (less chance to overlap)
                prevEnd = min(prevEnd, end)
                count += 1
        
        return count
        