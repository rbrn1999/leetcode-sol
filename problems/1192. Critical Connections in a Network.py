# link: https://leetcode.com/problems/critical-connections-in-a-network/
# solution reference: https://leetcode.com/problems/critical-connections-in-a-network/discuss/410345/Python-(98-Time-100-Memory)-clean-solution-with-explanaions-for-confused-people-like-me

from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        def dfs(rank, curr, prev):
            low[curr], result = rank, []
            for neighbor in edges[curr]:
                if neighbor == prev: continue
                if not low[neighbor]:
                    result += dfs(rank + 1, neighbor, curr)
                low[curr] = min(low[curr], low[neighbor])
                if low[neighbor] > rank:
                    result.append([curr, neighbor])
            return result

        low = [0] * n
        edges = defaultdict(list)
        for u, v in connections:
            edges[u].append(v)
            edges[v].append(u)

        return dfs(1, 0, -1) # -1 is for a dummy prev

    # Tarjan’s Algorithm
    # def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
    #     edges = defaultdict(list)
    #     for node1, node2 in connections:
    #         edges[node1].append(node2)
    #         edges[node2].append(node1)
    #     low = [0]*n
    #     visited = set()
    #     stack = []
    #     groups = []
        
    #     def dfs(id, prev):
    #         nonlocal stack, low, edges
    #         stack.append(id)
    #         visited.add(id)
    #         low[id] = id

    #         for dest in edges[id]:
    #             if dest == prev:
    #                 continue
    #             if dest not in visited:
    #                 dfs(dest, id)
    #             if dest in stack:
    #                 low[id] = min(low[id], low[dest])
    #         if id == low[id]:
    #             group = set()
    #             while stack:
    #                 node = stack.pop()
    #                 low[node] = id
    #                 group.add(node)
    #                 if node == id:
    #                     break
    #             groups.append(group)



    #     for i in range(n):
    #         if i not in visited:
    #             prev = -1
    #             dfs(i, prev)

    #     result = []
    #     for connection in connections:
    #         for group in groups:
    #             if connection[0] in group:
    #                 if connection[1] in group:
    #                     break
    #                 else:
    #                     result.append(connection)

    #     return result
        
    # dfs
    # def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
    #     def isConnected(edges):
    #         edges += [[edge[1], edge[0]] for edge in edges]
    #         visited = set()
    #         stack = [0]
    #         while stack:
    #             cur = stack.pop()
    #             visited.add(cur)
    #             for edge in [edge for edge in edges if edge[0] == cur]:
    #                 if edge[1] not in visited:
    #                     stack.append(edge[1])
    #                 edges.remove(edge)
    #         nonlocal n
    #         return len(visited) == n
        
    #     result = []
    #     for connection in connections:
    #         temp = deepcopy(connections)
    #         temp.remove(connection)
    #         if not isConnected(temp):
    #             result.append(connection)
        
    #     return result