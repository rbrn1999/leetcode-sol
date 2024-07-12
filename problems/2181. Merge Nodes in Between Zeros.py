# link: https://leetcode.com/problems/merge-nodes-in-between-zeros/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sumVal = 0
        prev = head
        cur = head.next
        while cur:
            if cur.val == 0:
                prev.val = sumVal
                prev.next = cur if cur.next else None
                prev = cur
                sumVal = 0
            else:
                sumVal += cur.val

            cur = cur.next

        return head