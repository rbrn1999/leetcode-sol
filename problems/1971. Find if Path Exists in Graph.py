# link: https://leetcode.com/problems/find-if-path-exists-in-graph/description/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = defaultdict(set)
        visited = set()

        for a, b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)

        def dfs(node):
            if node == destination:
                return True
            for neighbor in neighbors[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                neighbors[neighbor].remove(node)
                if dfs(neighbor):
                    return True
            return False

        visited.add(source)
        return dfs(source)

