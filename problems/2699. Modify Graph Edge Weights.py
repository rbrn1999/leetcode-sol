# link: https://leetcode.com/problems/modify-graph-edge-weights

import heapq
class Solution:
    def shorestPath(self, graph: dict, source: int, destination: int) -> int:

        heap = [(0, source)]
        visited = set()

        while heap:
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue

            visited.add(node)
            if node == destination:
                return weight

            for neighbor, w in graph[node]:
                if neighbor in visited:
                    continue
                heapq.heappush(heap, (weight + w, neighbor))

        return int(2e9)

    def modifiedGraphEdges(self, n: int, edges: list[list[int]], source: int, destination: int, target: int) -> list[list[int]]:
        graph = {node: list() for node in range(n)}
        modifiable_edge_indexes = []
        for i, (u, v, w) in enumerate(edges):
            if w == -1:
                modifiable_edge_indexes.append(i)
            else:
                graph[u].append((v, w))
                graph[v].append((u, w))

        curr_distance = self.shorestPath(graph, source, destination)
        if curr_distance < target:
            return []
        matches_target = curr_distance == target

        for i in modifiable_edge_indexes:
            edges[i][2] = int(2e9) if matches_target else 1
            u, v, w = edges[i]
            graph[u].append((v, w))
            graph[v].append((u, w))

            if not matches_target:
                new_distance = self.shorestPath(graph, source, destination)
                if new_distance <= target:
                    matches_target = True
                    edges[i][2] += target - new_distance

        return edges if matches_target else []
