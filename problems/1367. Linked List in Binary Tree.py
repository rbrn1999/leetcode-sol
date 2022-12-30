# link: https://leetcode.com/problems/linked-list-in-binary-tree/
# solution reference: https://leetcode.com/problems/linked-list-in-binary-tree/solutions/524881/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    # contains a subPath somewhere -> True
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if head is None:
            return True
        if root is None:
            return False
        
        return self.isPath(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    # dfs, root has the same path as head -> True
    def isPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if head is None:
            return True
        if root is None:
            return False

        return head.val == root.val and (self.isPath(head.next, root.left) or self.isPath(head.next, root.right))
        