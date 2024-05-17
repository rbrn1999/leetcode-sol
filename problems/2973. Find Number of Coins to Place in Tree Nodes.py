# link: https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

import heapq
from collections import defaultdict
from functools import reduce
from operator import mul
class Solution:
    def placedCoins(self, edges: list[list[int]], cost: list[int]) -> list[int]:
        coin = [0] * (len(edges) + 1)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node: int, par: int) -> list[list[int]]: # [[max positives], [min negatives]]
            positives = [] # positive values, minHeap
            negatives = [] # abs of negative values, minHeap
            if cost[node] > 0:
                positives.append(cost[node])
            else:
                negatives.append(-cost[node])
            
            for child in adj[node]:
                if child == par:
                    continue
                pos, neg = dfs(child, node)
  
                for val in pos:
                    heapq.heappush(positives, val)
                    while len(positives) > 3:
                        heapq.heappop(positives)
                for val in neg:
                    heapq.heappush(negatives, val)
                    while len(negatives) > 3:
                        heapq.heappop(negatives)
            
            if len(positives) + len(negatives) < 3:
                coin[node] = 1
            elif (len(positives) == 0) or (len(positives) == 2 and len(negatives) == 1):
                coin[node] = 0
            else:
                coin_count = 0
                positives.sort()
                negatives.sort()
                if len(positives) == 3:
                    coin_count = reduce(mul, positives, 1)
                if len(negatives) >= 2:
                    coin_count = max(coin_count, negatives[-1] * negatives[-2] * positives[-1])
                
                coin[node] = coin_count

            return [positives, negatives]
            
            
        dfs(0, -1)
        return coin

