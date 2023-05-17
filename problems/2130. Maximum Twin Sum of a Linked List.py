# link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next
        while fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow.next # first node of the second half
        slow.next = None # cut the the list into two halves
        while cur:
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        
        first = head
        second = prev

        maxVal = 0
        while first:
            maxVal = max(maxVal, first.val + second.val)
            first = first.next
            second = second.next
        
        return maxVal
