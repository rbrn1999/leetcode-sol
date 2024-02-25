# link: https://leetcode.com/problems/find-all-people-with-secret

from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        know_secret = set([0, firstPerson])
        time_meetings = {} # {time: {src: [neighbor]}}
        for src, dst, t in meetings:
            if t not in time_meetings:
                time_meetings[t] = defaultdict(list)
            time_meetings[t][src].append(dst)
            time_meetings[t][dst].append(src)
        
        def dfs(src: int, graph: list[list[int]]):
            if src in visited:
                return
            visited.add(src)
            know_secret.add(src)
            for nei in graph[src]:
                dfs(nei, graph)
        
        for t in sorted(time_meetings.keys()):
            visited = set()
            for src in time_meetings[t]:
                if src not in know_secret:
                    continue
                dfs(src, time_meetings[t])
        
        return list(know_secret)
