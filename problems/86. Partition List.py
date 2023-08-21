# link: https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first = ListNode() # < x
        second = ListNode() # nodes with value >= x
        firstTail = first
        secondTail = second
        node = head
        while node:
            nxt = node.next
            node.next = None
            if node.val < x:
                firstTail.next = node
                firstTail = node
            else:
                secondTail.next = node
                secondTail = node
            node = nxt
        
        firstTail.next = second.next
        return first.next