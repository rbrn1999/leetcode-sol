# link: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def findTarget(root):
            nonlocal target, count, flag
            if root is None or flag:
                return
            count += 1
            if root == target:
                flag = True
                return
            findTarget(root.left)
            findTarget(root.right)
        def findCopy(root):
            nonlocal count, order, flag, node
            if root is None or flag:
                return
            count += 1
            if count == order:
                flag = True
                node = root
                return
            findCopy(root.left)
            findCopy(root.right)
            
        
        count = 0
        flag = False
        node = None
        findTarget(original)
        order, count = count, 0
        flag = False
        findCopy(cloned)
        return node
        
        