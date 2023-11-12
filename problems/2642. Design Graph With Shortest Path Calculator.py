# link: https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

from collections import defaultdict
import heapq
class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        self.edges = defaultdict(list)
        for f, t, c in edges:
            self.edges[f].append((t, c))

    def addEdge(self, edge: list[int]) -> None:
        self.edges[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        visited = set()
        print(node1, node2)
        while heap:
            cost, node = heapq.heappop(heap)
            visited.add(node)
            if node == node2:
                return cost
            for next_node, c in self.edges[node]:
                if next_node in visited:
                    continue
                new_cost = cost + c
                heapq.heappush(heap, (new_cost, next_node))

        return -1



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)