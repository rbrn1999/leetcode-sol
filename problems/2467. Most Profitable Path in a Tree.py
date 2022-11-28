from collections import defaultdict, deque

class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        edgesDict = defaultdict(set)
        for a, b in edges:
            edgesDict[a].add(b)
            edgesDict[b].add(a)
        bobPath = []
        def dfs(root, path=deque()):
            path.appendleft(root)
            if root == bob:
                nonlocal bobPath
                bobPath = path.copy()
            for node in edgesDict[root]:
                edgesDict[node].remove(root)
                dfs(node, path)
            path.popleft()             
        
        dfs(0)
        bob_time = {bobPath[i]: i for i in range(len(bobPath))}
        res = -float('inf')
        def helper(root=0, alice_time=0, income=0):
            if root in bob_time and bob_time[root] == alice_time:
                income += amount[root] // 2
            elif (root in bob_time and bob_time[root] > alice_time) or root not in bob_time:
                income += amount[root]
            
            for child in edgesDict[root]:
                helper(child, alice_time+1, income)
            
            if not edgesDict[root]:
                nonlocal res
                res = max(res, income)
        
        helper()
        return res
