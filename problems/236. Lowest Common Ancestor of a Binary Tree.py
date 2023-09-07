# link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Time: O(n) 1 pass, Space: O(log(n))
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        answer = root

        def dfs(node):
            if node is None:
                return (0, None)
            left, l_ans = dfs(node.left)
            if l_ans:
                return (2, l_ans)
            right, r_ans = dfs(node.right)
            if r_ans:
                return (2, r_ans)
            state = left + right + int(node==p or node==q)
            if state == 2:
                print(node.val)
                return (state, node)
            else:
                return (state, None)
        
        return dfs(root)[1]
    
# Hash Map: Time: O(n) 4 passes, Space: O(n)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        answer = root

        def dfs(node):
            if node is None:
                return (0, None)
            left, l_ans = dfs(node.left)
            if l_ans:
                return (2, l_ans)
            right, r_ans = dfs(node.right)
            if r_ans:
                return (2, r_ans)
            state = left + right + int(node==p or node==q)
            if state == 2:
                print(node.val)
                return (state, node)
            else:
                return (state, None)
            
        
        return dfs(root)[1]