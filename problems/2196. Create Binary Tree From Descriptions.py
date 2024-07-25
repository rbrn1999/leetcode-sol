# link: https://leetcode.com/problems/create-binary-tree-from-descriptions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        node_map = {} # val: node
        parents = set()
        children = set()
        for parent, child, isLeft in descriptions:
            parents.add(parent)
            children.add(child)
            if parent not in node_map:
                node_map[parent] = TreeNode(parent)
            if child not in node_map:
                node_map[child] = TreeNode(child)

            if isLeft == 1:
                node_map[parent].left = node_map[child]
            else:
                node_map[parent].right = node_map[child]

        root_val = next(iter(parents - children))

        return node_map[root_val]
