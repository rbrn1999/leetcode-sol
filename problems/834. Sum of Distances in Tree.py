# link: https://leetcode.com/problems/sum-of-distances-in-tree

# solution: https://leetcode.com/problems/sum-of-distances-in-tree/solutions/130611/sum-of-distances-in-tree/
# better explaination: https://leetcode.com/problems/sum-of-distances-in-tree/solutions/1308366/
from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        answer = [0] * n
        count = [1] * n

        '''
        set node 0 as the root node
        get answer for root node and node count for each node
        ans[node] won't account the parent side for now,
        so only the root node gets the correct sum of distance
        '''
        def dfs(node: int=0, par: int=-1):
            for child in adj[node]:
                if child == par:
                    continue
                dfs(child, node)
                count[node] += count[child]
                answer[node] += answer[child] + count[child]

        '''
        comparing to the parent(current) node:
        the distance to the parent nodes will increase by 1 -> 1 * (n - count[child])
        the distance to the child nodes will decrease by 1  -> 1 * count[child]
        '''
        def dfs2(node: int=0, par: int=-1):
            for child in adj[node]:
                if child == par:
                    continue
                answer[child] = answer[node] - count[child] + (n - count[child])
                dfs2(child, node)

        dfs() # get the answer for node 0
        dfs2() # get the answer for the rest of the nodes

        return answer
