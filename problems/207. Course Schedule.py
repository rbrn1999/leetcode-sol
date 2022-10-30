from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        prereq_dict = defaultdict(list)
        for p in prerequisites:
            prereq_dict[p[0]].append(p[1])
        finished = [False] * numCourses
        def canFinish(course, seen):
            if finished[course]:
                return True
            if course in seen:
                return False
            if course not in prereq_dict:
                finished[course] = True
                return True
            seen.add(course)
            for p in prereq_dict[course]:
                if canFinish(p, seen):
                    finished[p] = True
                else:
                    return False
            seen.remove(course)
            return True
        
        for i in range(numCourses):
            if not canFinish(i, set()):
                return False
        return True
