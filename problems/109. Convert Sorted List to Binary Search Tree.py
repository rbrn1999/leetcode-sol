# link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        prev = None
        mid = head
        fast = head
        while fast and fast.next:
            prev = mid
            mid = mid.next
            fast = fast.next.next
        if prev:
            prev.next = None
        return TreeNode(mid.val, self.sortedListToBST(head), self.sortedListToBST(mid.next))

