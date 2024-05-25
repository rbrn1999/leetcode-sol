# link: https://leetcode.com/problems/employee-free-time/

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        result = []
        heap = [] # (start, end, employee_index, interval_index)
        n = len(schedule)
        for i in range(n):
            interval = schedule[i][0]
            heapq.heappush(heap, (interval.start, interval.end, i, 1))

        prev = -1
        while heap:
            start, end, employee, index = heapq.heappop(heap)
            if index < len(schedule[employee]):
                interval = schedule[employee][index]
                heapq.heappush(heap, (interval.start, interval.end, employee, index+1))

            if prev != -1 and start > prev:
                free_interval = Interval(prev, start)
                result.append(free_interval)
            
            prev = max(prev, end)
        
        return result
        