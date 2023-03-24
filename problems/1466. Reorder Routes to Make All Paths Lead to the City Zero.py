# link: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        inverse_graph = defaultdict(set)
        for a, b in connections:
            graph[a].add(b)
            inverse_graph[b].add(a)

        answer = 0
        def dfs(node: int, parent: int = -1):
            nonlocal answer
            for child in graph[node]:
                if child == parent:
                    continue
                answer += 1
                dfs(child, node)
            for child in inverse_graph[node]:
                if child == parent:
                    continue
                dfs(child, node)

        dfs(0)
        return answer

