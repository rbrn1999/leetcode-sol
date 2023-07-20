# link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        edges = defaultdict(list)
        node_map = {}
        def dfs(node):
            if not node:
                return
            node_map[node.val] = node
            if node.left:
                edges[node].append(node.left)
                edges[node.left].append(node)
                dfs(node.left)
            if node.right:
                edges[node].append(node.right)
                edges[node.right].append(node)
                dfs(node.right)

        dfs(root)
        distance = 0
        q = deque()
        visited = set()
        q.append(target.val)
        visited.add(target.val)

        for _ in range(k):
            for _ in range(len(q)):
                node = node_map[q.popleft()]
                for neighbor in edges[node]:
                    if neighbor.val not in visited:
                        visited.add(neighbor.val)
                        q.append(neighbor.val)

        return list(q)

