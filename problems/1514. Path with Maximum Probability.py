# link: https://leetcode.com/problems/path-with-maximum-probability/

from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
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
