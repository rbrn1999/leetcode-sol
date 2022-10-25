# link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# solution reference: https://youtu.be/XVuQxVej6y8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = head
        
        for _ in range(n): # set offset
            right = right.next
            
        prev = None
        while right:
            prev, left = left, left.next
            right = right.next
 
        if left is head:
            return left.next
        else:
            prev.next = left.next
        
        return head