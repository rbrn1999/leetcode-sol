# link: https://leetcode.com/problems/cheapest-flights-within-k-stops/

from collections import deque, defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
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

