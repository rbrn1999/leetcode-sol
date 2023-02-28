# link: https://leetcode.com/problems/find-duplicate-subtrees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        height_nodes = defaultdict(set)
        duplicates = {None: "null,"}
        answer = []

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1
            height = max(dfs(node.left), dfs(node.right)) + 1
            height_nodes[height].add(node)
            return height

        maxHeight = dfs(root)

        for height in range(maxHeight+1):
            groups = defaultdict(list)
            for node in height_nodes[height]:
                if (node.left and node.left not in duplicates) or (node.right and node.right not in duplicates):
                    continue
                groups[(node.val, duplicates[node.left], duplicates[node.right])].append(node)

            for group in groups.values():
                if len(group) < 2:
                    continue
                answer.append(group[0])
                duplicates.update({node: f'{node.val}l{duplicates[node.left]}r{duplicates[node.right]}' for node in group})

        return answer
