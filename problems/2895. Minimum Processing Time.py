# link: https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: list[int], tasks: list[int]) -> int:
        timeSpent = 0
        processorTime.sort(reverse=True)
        tasks.sort()
        while processorTime:
            pTime = processorTime.pop()
            tTime = -float('inf')
            for _ in range(4):
                tTime = max(tTime, tasks.pop())
            totalTime = pTime + tTime
            timeSpent = max(timeSpent, totalTime)
        
        return timeSpent
            