# link: https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

from collections import defaultdict
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        distance = defaultdict(list)
        def dfs(node: int, d: int = 0, visited: set = set()) -> int:
            if node in visited: # cycle
                return

            distance[node].append(d)

            if edges[node] == -1: # no outgoing edge
                return

            visited.add(node)
            dfs(edges[node], d+1, visited)
            visited.remove(node)

        dfs(node1)
        dfs(node2)
        min_distance = float('inf')
        result_node = -1
        for i in range(n):
            if len(distance[i]) == 2 and max(distance[i]) < min_distance:
                result_node = i
                min_distance = max(distance[i])

        return result_node

