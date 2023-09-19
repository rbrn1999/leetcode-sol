# link: https://leetcode.com/problems/shortest-path-visiting-all-nodes/

from collections import deque
class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
            
        q = deque()
        visited = set() # (bit_mask_of_visited, last_node)
        for node in range(n):
            q.append([node, 2 ** node])
            visited.add((node, 2 ** node))
        steps = 0
        while q:
            for _ in range(len(q)):
                node, visited_mask = q.popleft()
                for neighbor in graph[node]:
                    new_visited_mask = visited_mask | (2 ** node)
                    if (neighbor, new_visited_mask) in visited:
                        continue
                    else:
                        visited.add((neighbor, new_visited_mask))
                    if new_visited_mask == 2 ** n - 1:
                        return steps
                    else:
                        q.append([neighbor, new_visited_mask])
            steps += 1
        
        return steps
    