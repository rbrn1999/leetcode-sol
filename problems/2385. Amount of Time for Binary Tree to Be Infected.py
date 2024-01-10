# link: https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

from collections import defaultdict, deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        edges = defaultdict(list)
        def dfs(root):
            if root is None:
                return
            if root.left:
                edges[root.val].append(root.left.val)
                edges[root.left.val].append(root.val)
                dfs(root.left)
            if root.right:
                edges[root.val].append(root.right.val)
                edges[root.right.val].append(root.val)
                dfs(root.right)
        
        dfs(root)
        q = deque()
        q.append(start)
        visited = set()
        t = -1

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                visited.add(node)
                for neighbor in edges[node]:
                    if neighbor not in visited:
                        q.append(neighbor)
            
            t += 1
        
        return t