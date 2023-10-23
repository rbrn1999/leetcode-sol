# link: https://leetcode.com/problems/parallel-courses-iii/

from functools import cache
from collections import defaultdict
class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        requirements = defaultdict(set)
        for pre, course in relations:
            requirements[course-1].add(pre-1)

        @cache        
        def dfs(course: int) -> int:
            t = time[course]
            if requirements[course]:
                t += max(dfs(pre) for pre in requirements[course])
            print(course, t)
            return t
        
        return max(dfs(course) for course in range(n))