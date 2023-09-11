# link: https://leetcode.com/problems/number-of-provinces/
# explaination: https://leetcode.com/explore/featured/card/graph/618/disjoint-set/3846/

# Union Find
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        parents = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        # find root with path compression
        def find(node):
            if node == parents[node]:
                return node
            parents[node] = find(parents[node])
            return parents[node]
        # iterative
        # def find(node):
        #     parent = node
        #     while parent != parents[parent]:
        #         parents[parent] = parents[parents[parent]]
        #         parent = parents[parent]
        #     return parent

        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                return False
            if rank[parent1] > rank[parent2]:
                parents[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parents[parent1] = parent2
                rank[parent2] += rank[parent1]
            return True

        result = n
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    result -= 1 if union(i, j) else 0

        return result

# DFS
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = set()

        def dfs(i):
            if i in visited:
                return 0
            else:
                visited.add(i)
            for j in range(n):
                if i != j and isConnected[i][j] == 1 and j not in visited:
                    dfs(j)
            
            return 1
        
        count = 0
        for i in range(n):
            count += dfs(i)
        
        return count