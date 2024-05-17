# link: https://leetcode.com/problems/parallel-courses/

from collections import defaultdict
class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        indegree = [0] * (n+1)
        next_courses = defaultdict(list)
        for pre, course in relations:
            indegree[course] += 1
            next_courses[pre].append(course)

        taking = []
        for course in range(1, n+1):
            if indegree[course] == 0:
                taking.append(course)

        semesters = 0
        while taking:
            to_take = []
            for course in taking:
                for next_course in next_courses[course]:
                    indegree[next_course] -= 1
                    if indegree[next_course] == 0:
                        to_take.append(next_course)

            taking = to_take
            semesters += 1

        if any(val > 0 for val in indegree):
            return -1
        else:
            return semesters
