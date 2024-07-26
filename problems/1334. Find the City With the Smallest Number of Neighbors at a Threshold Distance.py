# link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for u, v, d in edges:
            graph[u].append((v, d))
            graph[v].append((u, d))
        
        reachable_cities = [-1] * n

        for source in range(n):
            heap = [(0, source)]
            visited = set()
            while heap:
                distance, city = heapq.heappop(heap)
                if city in visited:
                    continue
                visited.add(city)
                reachable_cities[source] += 1
                for next_city, d in graph[city]:
                    if next_city in visited:
                        continue
                    
                    new_distance = distance + d
                    if new_distance > distanceThreshold:
                        continue
                    
                    heapq.heappush(heap, (new_distance, next_city))
        
        min_reachable = min(reachable_cities)
        for city in range(n-1, -1, -1):
            if reachable_cities[city] == min_reachable:
                return city
        
        return -1
