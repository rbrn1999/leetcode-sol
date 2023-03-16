# link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# in-place solution
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        inorder_index = {inorder[i]:i for i in range(len(inorder))}

        def helper(i_start, i_end, p_start, p_end): # [start, end)
            if i_start == i_end:
                return None
            root_ind = inorder_index[postorder[p_end-1]]
            if root_ind < i_start or root_ind >= i_end:
                return None
            root = TreeNode(postorder[p_end-1])
            root.left = helper(i_start, root_ind, p_start, p_start + (root_ind-i_start))
            root.right = helper(root_ind+1, i_end, p_start + (root_ind-i_start), p_end - 1)
            return root

        return helper(0, len(inorder), 0, len(postorder))


# copy array solution (slower)
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        in_index = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:in_index], postorder[:in_index])
        root.right = self.buildTree(inorder[in_index+1:], postorder[in_index:-1])
        return root