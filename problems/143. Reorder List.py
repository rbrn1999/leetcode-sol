#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next # second: head of second half
        prev = slow.next = None

        # reverse second half
        while second:
            second.next, prev, second = prev, second, second.next

            # be careful of the multiple assignment order on mutable objects
            # the two lines under are incorrect
            # second, second.next, prev = second.next, prev, second
            # prev, second, second.next = second, second.next, prev
        
        # merge first half and reversed second half
        first, second = head, prev
        while second:
            nextFirst, nextSec = first.next, second.next
            first.next, second.next = second, first.next
            first, second = nextFirst, nextSec        
        
# @lc code=end

