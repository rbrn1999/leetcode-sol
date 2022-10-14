# link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = slow = fast = head
        
        while fast and fast.next:
            prev, slow = slow, slow.next
            fast = fast.next.next
            
        prev.next = slow.next
        if fast == head:
            return None
        return head