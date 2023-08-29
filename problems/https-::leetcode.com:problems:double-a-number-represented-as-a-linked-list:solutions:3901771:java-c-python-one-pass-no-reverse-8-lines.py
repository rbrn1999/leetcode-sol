# link: https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/solutions/3901771/java-c-python-one-pass-no-reverse-8-lines/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse list
        cur = head
        prev = None
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev, cur = cur, nextNode
        head = prev
        double_head = None
        carry = 0
        cur = head
        while cur or carry > 0:
            val = (cur.val * 2 + carry) % 10 if cur else carry % 10
            carry = (cur.val * 2 + carry) // 10 if cur else carry // 10
            if cur:
                cur = cur.next
            node = ListNode(val)
            node.next, double_head = double_head, node

        return double_head