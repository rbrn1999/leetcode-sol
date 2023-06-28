# link: https://leetcode.com/problems/path-with-maximum-probability/

from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
        graph = defaultdict(list)

        for i in range(len(edges)):
            a, b = edges[i]
            graph[a].append((succProb[i], b))
            graph[b].append((succProb[i], a))

        maxHeap =[(-1, start)]
        visited = set()

        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            prob *= -1
            visited.add(node)
            if node == end:
                return prob
            for n_prob, neighbor in graph[node]:
                if neighbor in visited:
                    continue
                heapq.heappush(maxHeap, (-prob*n_prob, neighbor))

        return 0

# Use sum of log instead of multiplying
# from collections import defaultdict
# import heapq
# import math
# class Solution:
#     def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
#         graph = defaultdict(list)
#         for i in range(len(edges)):
#             a, b = edges[i]
#             prob = succProb[i]
#             graph[a].append((b, prob))
#             graph[b].append((a, prob))
            
#         maxHeap = [(0, start)]
#         visited = set([start])

#         while maxHeap:
#             prob, node = heapq.heappop(maxHeap)
#             prob *= -1
#             if node == end:
#                 return 2 ** prob
#             visited.add(node)
#             for neighbor, nextProb in graph[node]:
#                 if neighbor not in visited:
#                     heapq.heappush(maxHeap, (-prob - math.log(nextProb, 2), neighbor))

#         return 0