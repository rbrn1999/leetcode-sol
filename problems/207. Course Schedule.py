from collections import defaultdict
from functools import cache
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        prereq_dict = defaultdict(list)
        for p in prerequisites:
            prereq_dict[p[0]].append(p[1])
       
        path = set()
        visited = set()
        @cache
        def dfs(course):
            path.add(course)
            for p in prereq_dict[course]:
                if p in visited:
                    continue
                if p in path or dfs(p):
                    return True # cycle
            path.remove(course)
            return False

        for i in range(numCourses):
            if dfs(i):
                return False
        return True
