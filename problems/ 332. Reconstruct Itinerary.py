# link: https://leetcode.com/problems/reconstruct-itinerary/

# DFS
from collections import defaultdict, Counter
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)
        
        for start in graph:
            graph[start].sort()
        
        itinerary = ["JFK"]
        src = "JFK"
        ticketCount = Counter(tuple(ticket) for ticket in tickets)
        def dfs(src) -> bool:
            if len(itinerary) == len(tickets) + 1:
                return True

            for dest in graph[src]:
                if ticketCount[(src, dest)] == 0:
                    continue
                itinerary.append(dest)
                ticketCount[(src, dest)] -= 1
                if dfs(dest):
                    return True
                itinerary.pop()
                ticketCount[(src, dest)] += 1
            
            return False

        dfs(src)
        return itinerary