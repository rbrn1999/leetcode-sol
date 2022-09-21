# link: https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast:
            if fast.next is None:
                return slow
            elif fast.next.next is None:
                return slow.next
            else:
                slow = slow.next
                fast = fast.next.next
        return slow