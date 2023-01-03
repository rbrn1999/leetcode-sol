# link: https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = {}
        for i in range(len(manager)):
            if i == headID:
                continue
            graph.setdefault(manager[i], list())
            graph[manager[i]].append(i)

        def dfs(node):
            if node not in graph:
                return 0
            time = informTime[node]
            time += max(dfs(child) for child in graph[node])
            return time

        return dfs(headID)

