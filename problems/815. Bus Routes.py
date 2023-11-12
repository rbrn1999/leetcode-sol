# link: https://leetcode.com/problems/bus-routes/
from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if target == source:
            return 0

        q = deque()
        visited = set()
        target_buses = set()

        bus_graph = defaultdict(set)
        for bus_a in range(len(routes)):
            s = set(routes[bus_a])
            # add the starting points to the queue
            if source in s:
                q.append(bus_a)
                visited.add(bus_a)
            if target in s:
                target_buses.add(bus_a)

            # build the n*n adjacent bus graph
            for bus_b in range(bus_a+1, len(routes)):
                if any((route in s) for route in routes[bus_b]):
                    bus_graph[bus_a].add(bus_b)
                    bus_graph[bus_b].add(bus_a)

        steps = 1

        while q:
            for _ in range(len(q)):
                bus = q.popleft()
                if bus in target_buses:
                    return steps
                for next_bus in bus_graph[bus]:
                    if next_bus not in visited:
                        visited.add(next_bus)
                        q.append(next_bus)
            steps += 1
        
        return -1