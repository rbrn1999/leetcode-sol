# link: https://leetcode.com/problems/maximum-total-importance-of-roads/

class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        indegree = [0] * n
        for u, v in roads:
            indegree[u] += 1
            indegree[v] += 1
        
        indegree.sort()
        
        return sum(indegree[i] * (i + 1) for i in range(n))