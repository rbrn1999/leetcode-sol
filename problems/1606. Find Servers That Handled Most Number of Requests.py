# link: https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

from sortedcontainers import SortedList
import heapq
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        handled_requests = [0] * k
        available_servers = SortedList(range(k))
        processing_heap = [] # (finishing time, index of the server)
        n = len(arrival)

        for i in range(n):
            while processing_heap and processing_heap[0][0] <= arrival[i]:
                _, index = heapq.heappop(processing_heap)
                available_servers.add(index)

            if not available_servers:
                continue

            j = available_servers.bisect_left(i%k)
            index = available_servers[j] if j < len(available_servers) else available_servers[0]
            handled_requests[index] += 1
            end_time = arrival[i] + load[i]
            available_servers.remove(index)
            heapq.heappush(processing_heap, (end_time, index))


        max_requests = max(handled_requests)
        result = []
        for i in range(k):
            if handled_requests[i] == max_requests:
                result.append(i)

        return result
