# link: https://leetcode.com/problems/redundant-connection/description/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        neighbors = defaultdict(set)
        for a, b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)

        visited = set()
        path = []
        cycleNodes = set()
        def dfs(node, parent):
            # print(node, path)
            if node in visited: # cycle detected
                # deal with the cycle
                i = path.index(node)
                nonlocal cycleNodes
                cycleNodes = set(path[i:])
                return

            visited.add(node)
            path.append(node)
            for neighbor in list(neighbors[node]):
                if neighbor == parent:
                    continue
                dfs(neighbor, node)
            visited.remove(node)
            path.pop()

        dfs(1, 1)

        for a, b in edges[::-1]:
            if a in cycleNodes and b in cycleNodes:
                return [a, b]
