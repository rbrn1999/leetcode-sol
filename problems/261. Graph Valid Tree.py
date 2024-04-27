# link: https://leetcode.com/problems/graph-valid-tree/

from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        def dfs(node: int, par: int=-1):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == par:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False
            return True

        if not dfs(0):
            return False
        return len(visited) == n
