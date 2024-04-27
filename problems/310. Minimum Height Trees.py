# link: https://leetcode.com/problems/minimum-height-trees/

from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        q = deque()

        for node in range(n):
            if len(graph[node]) <= 1:
                q.append(node)

        result = []

        while q:
            result = list(q)
            for _ in range(len(q)):
                node = q.popleft()
                for neighbor in graph[node]:
                    graph[neighbor].remove(node)
                    if len(graph[neighbor]) == 1:
                        q.append(neighbor)

        return result
