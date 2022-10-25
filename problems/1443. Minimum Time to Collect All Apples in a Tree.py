# link: https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        nodeEdges = defaultdict(list)
        for a, b in edges:
            nodeEdges[a].append(b)
            nodeEdges[b].append(a)
        usedEdges = set()
        def dfs(node, path):
            path.append(node)
            if hasApple[node]:
                nonlocal usedEdges
                for i in range(1, len(path)):
                    usedEdges.add((path[i-1], path[i]))
            for dest in nodeEdges[node]:
                if dest not in path:
                    dfs(dest, path.copy())

        dfs(0, [])
        return 2 * len(usedEdges)
