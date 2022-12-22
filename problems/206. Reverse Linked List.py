# link: https://leetcode.com/problems/reverse-linked-list/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            cur.next, cur, prev = prev, cur.next, cur

        return prev

# recursive
# solution: https://leetcode.com/problems/reverse-linked-list/solutions/58127/python-iterative-and-recursive-solution/comments/291532

 def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node
