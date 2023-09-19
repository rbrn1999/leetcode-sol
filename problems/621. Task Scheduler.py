# link: https://leetcode.com/problems/task-scheduler/

from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        taskCount = Counter(tasks)
        maxHeap = [-count for count in taskCount.values()] 
        q = deque()
        heapq.heapify(maxHeap)
        t = 0
        while maxHeap or q:
            while q and q[0][1] <= t:
                count, _ = q.popleft()
                heapq.heappush(maxHeap, -count)
            if not maxHeap:
                count, new_t = q.popleft()
                heapq.heappush(maxHeap, -count)
                t = new_t
            count = -1 * heapq.heappop(maxHeap)
            count -= 1
            t += 1
            if count > 0:
                q.append((count, t + n))
        
        return t