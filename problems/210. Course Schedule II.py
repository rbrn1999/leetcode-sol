from collections import deque, defaultdict
from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        for course, prerequisite in prerequisites:
            edges[course].append(prerequisite)
        order = [-1] * numCourses
        visited = [False] * numCourses

        orderIndex = 0
        def dfs(course):
            visited[course] = True
            for edge in edges[course]:
                if visited[edge]:
                    continue
                dfs(edge)

            nonlocal orderIndex
            order[orderIndex] = course
            orderIndex += 1
            return True

        for course in range(numCourses):
            if visited[course]:
                continue
            dfs(course)

        # check cycle
        positions = {course: pos for pos, course in enumerate(order)}
        for i in range(numCourses):
            for edge in edges[i]:
                if positions[i] < positions[edge]:
                    return []

        return order
