#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
# link: https://leetcode.com/problems/merge-two-sorted-lists/description/

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = None
        while list1 and list2:
            if list1.val < list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next
            if head is None:
                head = cur = ListNode(val=val)
            else:
                cur.next = ListNode(val=val)
                cur = cur.next
        if list1:
            if head is None:
                head = list1
            else:
                cur.next = list1
        elif list2:
            if head is None:
                head = list2
            else: 
                cur.next = list2
        return head
# @lc code=end

