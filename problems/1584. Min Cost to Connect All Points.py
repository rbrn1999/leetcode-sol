# link: https://leetcode.com/problems/min-cost-to-connect-all-points/

import heapq
# solution reference: https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/843995/
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        distance = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
        heap = []
        # Prim's Algorithm

        for i in range(1, len(points)):
            heap.append((distance(points[0], points[i]), i))

        edgeCount = 0
        cost = 0
        visited = [True] + [False] * (len(points)-1)
        heapq.heapify(heap)
        
        while heap:
            d, end_p = heapq.heappop(heap)
            if not visited[end_p]:
                visited[end_p] = True
                cost += d
                for i in range(1, len(points)):
                    if i != end_p and not visited[i]:
                        heapq.heappush(heap, (distance(points[end_p], points[i]), i))
                edgeCount += 1
            if edgeCount >= len(points):
                break

        return cost

                    
# Failed Approach: Time Limit Exceeded
# class Solution:
#     def minCostConnectPoints(self, points: list[list[int]]) -> int:
#         distance = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])

#         # Prim's Algorithm
        
#         costs = [0] + [float('inf')]*(len(points)-1)  # point costs from [0]->[i]
        
#         pending = [(0, 0)] # (cost, index)
#         visited = set([0])
        
#         while pending:
#             node = heapq.heappop(pending)[1]
#             for dest in range(len(points)):
#                 if node == dest or dest in visited:
#                     continue
                    
#                 costs[dest] = min(costs[dest], distance(points[node], points[dest]))
#                 if dest not in pending:
#                     heapq.heappush(pending, (costs[dest], dest))
                    
#             visited.add(node)
        
#         return sum(costs)



# # solution reference: https://leetcode.com/problems/min-cost-to-connect-all-points/solution/
# class UnionFind:
#     def __init__(self, size):
#         self.group = [i for i in range(size)]
#         self.rank = [0] * size
        
#     def find(self, node: int) -> int:
#         if self.group[node] != node:
#             self.group[node] = self.find(self.group[node])
#         return self.group[node]
    
#     def join(self, node1: int, node2: int) -> bool:
#         group1 = self.find(node1)
#         group2 = self.find(node2)
        
#         if group1 == group2:
#             return False
        
#         if self.rank[group1] > self.rank[group2]:
#             self.group[group2] = group1
#         elif self.rank[group1] < self.rank[group2]:
#             self.group[group1] = group2
#         else:
#             self.group[group1] = group2
#             self.rank[group2] += 1
        
#         return True

# class Solution:
#     def minCostConnectPoints(self, points: list[list[int]]) -> int:
#         def distance(a, b):
#             return abs(a[0] - b[0]) + abs(a[1] - b[1])
#         n=len(points)
#         edges = [] # (weight, node1, node2)
#         for i in range(n):
#             for j in range(i+1, n):
#                 edges.append((distance(points[i], points[j]), i, j))
                
#         edges.sort()
        
#         uf = UnionFind(n)
#         mst_cost = 0
#         edges_used = 0
        
#         for weight, node1, node2 in edges:
#             if uf.join(node1, node2):
#                 mst_cost += weight
#                 edges_used += 1
#                 if edges_used == n-1:
#                     break

#         return mst_cost        