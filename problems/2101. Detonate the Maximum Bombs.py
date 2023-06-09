# link: https://leetcode.com/problems/detonate-the-maximum-bombs/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = {}
        n = len(bombs)
        for i in range(n):
            graph[i] = []
            x1, y1, r = bombs[i]
            for j in range(n):
                x2, y2, _ = bombs[j]
                if i != j and (x2-x1) ** 2 + (y2-y1) ** 2 <= r ** 2:
                    graph[i].append(j)
               
        def dfs(bomb: int, visited: set) -> int:
            if bomb in visited:
                return 0
            visited.add(bomb)
            count = 1
            for neighbor in graph[bomb]:
                count += dfs(neighbor, visited)
            return count
        
        return max(dfs(bomb, set()) for bomb in graph)
    