# link: https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2022/12/06
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        evenHead = head.next
        evenTail = head.next
        oddTail = head
        cur = head.next.next
        oddTail.next = evenTail.next = None
        isOdd = True
        while cur:
            if isOdd:
                oddTail.next = cur
                oddTail = cur
                cur = cur.next
                oddTail.next = None
            else:
                evenTail.next = cur
                evenTail = cur
                cur = cur.next
                evenTail.next = None

            isOdd = not isOdd

        oddTail.next = evenHead
        return head

# 2021/11/25
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cur = head
        evenHead = head.next
        evenTail = None

        while cur.next:
            if evenTail is None:
                evenTail = cur.next
            else:
                evenTail.next = cur.next
                evenTail = cur.next
            cur.next = cur.next.next
            if cur.next:
                cur = cur.next

        cur.next = evenHead
        evenTail.next = None
        return head
