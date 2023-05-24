# link: https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

# In-Degree Count
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return set(range(n))-set(dest for _, dest in edges)

# DFS
from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for start, dest in edges:
            graph[start].add(dest)
        
        vertices = set()
        visited = set()
        def dfs(node):
            if node in vertices:
                vertices.remove(node)
                return
            if node in visited:
                return
            
            visited.add(node)
            for dest in graph[node]:
                dfs(dest)

        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            vertices.add(i)
        
        return list(vertices)