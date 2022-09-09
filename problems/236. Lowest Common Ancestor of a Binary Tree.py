# link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, path, target):
            if root is None:
                return None
            if root is target:
                return path+[root]
            
            if root.left:
                path_candidate = dfs(root.left, path+[root], target)
                if path_candidate:
                    return path_candidate
            if root.right:
                return dfs(root.right, path+[root], target)
            
            return None
        
        
        pa = dfs(root, [], p)
        qa = dfs(root, [], q)
        
        # print([node.val for node in pa])
        # print([node.val for node in qa])
                
        for i in pa[::-1]:
            for j in qa[::-1]:
                if i == j:
                    return i
        
        return None

root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

print(Solution().lowestCommonAncestor(root, root.left, root.right).val)