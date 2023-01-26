# link: https://leetcode.com/problems/cheapest-flights-within-k-stops/

from collections import deque, defaultdict

# 2023/01/26: more optimal
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        minPrice = {src: 0}
        destinationPrice = defaultdict(list)
        for start, end, price in flights:
            if start != dst:
                destinationPrice[start].append([end, price])
        
        queue = deque([(src, 0)])
        steps = 0
        while queue and steps <= k:
            for _ in range(len(queue)):
                node, price = queue.popleft()
                neighborNodes = set()
                for neighbor, pathPrice in destinationPrice[node]:
                    newPrice = price + pathPrice
                    if newPrice < minPrice.get(neighbor, float('inf')):
                        minPrice[neighbor] = newPrice
                        neighborNodes.add(neighbor)
                queue.extend([(node, minPrice[node]) for node in neighborNodes])
            steps += 1
            
        return minPrice.get(dst, -1)

# 2022/12/31
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        edges = defaultdict(list)
        for start, end, price in flights:
            if start != dst:
                edges[start].append((end, price))

        minPrice = {src: 0, dst: float('inf')}
        steps = 0
        queue = deque()

        queue.extend(edges[src])

        while queue and steps <= k:
            for _ in range(len(queue)):
                node, price = queue.popleft()
                if minPrice.get(node, float('inf')) > price:
                    minPrice[node] = price
                    queue.extend([(n_node, price + n_price) for (n_node, n_price) in edges[node]])
            steps += 1

        return minPrice[dst] if minPrice[dst] < float('inf') else -1

