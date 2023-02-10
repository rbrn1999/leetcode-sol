# link: https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)

        def helper(node: Optional[TreeNode], isRoot: bool=True) -> List[TreeNode]:
            if node is None:
                return []

            # remove link to node to delete
            left, right = node.left, node.right
            if left and left.val in to_delete:
                node.left = None
            if right and right.val in to_delete:
                node.right = None

            # recursion
            if node.val in to_delete:
                return helper(left) + helper(right)
            else:
                return ([node] if isRoot else []) + helper(left, False) + helper(right, False)


        return helper(root)


