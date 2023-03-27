# link: https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = set()
        longest_cycle = -1
        def dfs(node, depth, depth_map):
            if node not in visited:
                visited.add(node)
                depth_map[node] = depth
                if edges[node] != -1:
                    dfs(edges[node], depth+1, depth_map)
            else:
                if node not in depth_map:
                    return
                nonlocal longest_cycle
                longest_cycle = max(longest_cycle, depth - depth_map[node])

        for node in range(len(edges)):
            dfs(node, 0, dict())

        return longest_cycle

