# link: https://leetcode.com/problems/minimum-interval-to-include-each-query/
import heapq
class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        answer = [-1] * len(queries)
        minHeap = [] # (length, right)
        intervals.sort()
        queries_index = sorted((q, i) for i, q in enumerate(queries))

        i = 0

        for q, j in queries_index:
            while i < len(intervals) and q >= intervals[i][0]:
                if q <= intervals[i][1]:
                    heapq.heappush(minHeap, (intervals[i][1]-intervals[i][0]+1, intervals[i][1]))
                i += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            if minHeap:
                answer[j] = minHeap[0][0]

        return answer
