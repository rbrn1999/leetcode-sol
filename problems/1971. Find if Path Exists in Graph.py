# link: https://leetcode.com/problems/find-if-path-exists-in-graph/description/
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(node: int) -> bool:
            if node in visited:
                return False
            else:
                visited.add(node)
            if node == destination:
                return True
            for n in graph[node]:
                if dfs(n):
                    return True

            return False

        return dfs(source)
