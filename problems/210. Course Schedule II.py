from collections import defaultdict

# detect cycle while in process (much better approach)
# reference: https://youtu.be/6kTZYvNNyps

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        edges = defaultdict(list)
        for course, prerequisite in prerequisites:
            edges[course].append(prerequisite)

        order = []
        visited = {} # False: visited, True: in path, not done(processed) yet

        def dfs(course):
            if course in visited: # pass if visited and early return if cycle detected
                return visited[course]
            visited[course] = True

            for edge in edges[course]:
                if dfs(edge):
                    return True # cycle detected

            order.append(course)
            visited[course] = False
            return False

        for course in range(numCourses):
            if dfs(course):
                return []

        return order


# detect cycle afterhand
# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
#         edges = defaultdict(list)
#         for course, prerequisite in prerequisites:
#             edges[course].append(prerequisite)
#         order = []
#         visited = [False] * numCourses

#         def dfs(course):
#             visited[course] = True
#             for edge in edges[course]:
#                 if visited[edge]:
#                     continue
#                 dfs(edge)

#             order.append(course)
#             return True

#         for course in range(numCourses):
#             if visited[course]:
#                 continue
#             dfs(course)

#         # check cycle
#         positions = {course: pos for pos, course in enumerate(order)}
#         for i in range(numCourses):
#             for edge in edges[i]:
#                 if positions[i] < positions[edge]:
#                     return []

#         return order