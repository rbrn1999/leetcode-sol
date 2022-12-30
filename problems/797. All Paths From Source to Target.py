# link: https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        path = []
        def dfs(node):
            if node == n-1:
                paths.append(path + [n-1])
                return
            path.append(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            path.pop()

        dfs(0)
        return paths
