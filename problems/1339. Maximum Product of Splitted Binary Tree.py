# link: https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def findTotal(node):
            if node is None:
                return 0
            return node.val + findTotal(node.left) + findTotal(node.right)


        def findMid(node, target, finalVal = [0]):
            if node is None:
                return 0
            left = findMid(node.left, target, finalVal)
            right = findMid(node.right, target, finalVal)
            if finalVal[0] > 0: # early return if mid is already found
                return finalVal[0]
            total = node.val + left + right
            prev = max(left, right)
            print(left, right, total)
            if total > target:
                if total - target < target - prev:
                    finalVal[0] = total
                else:
                    finalVal[0] = prev
                return finalVal[0]
            else:
                return total


        total = findTotal(root)
        mid = findMid(root, total / 2)
        return ((mid) * (total - mid)) % int(1E9 + 7)

