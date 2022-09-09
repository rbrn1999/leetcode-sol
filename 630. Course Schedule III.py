# link: https://leetcode.com/problems/course-schedule-iii/

import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        pq = [] # max heap
        start = 0

        for dur, end in courses:
            start += dur
            heapq.heappush(pq, -dur) # '-', for max heap
            while start > end:
                start += heapq.heappop(pq) # + instead of - for max heap

        return len(pq)
