# link: https://leetcode.com/problems/remove-nodes-from-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse list
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        head = prev
        # traverse in reversed order, keep track of current max
        # if the current max is larger than the node, remove it
        curMax = 0
        prev = ListNode()
        cur = head
        while cur:
            curMax = max(curMax, cur.val)
            if cur.val < curMax:
                prev.next = cur.next
            else:
                prev = cur

            cur = cur.next

        # reverse the link back to the original order
        cur = head
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
