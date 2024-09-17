# link: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @staticmethod
    def gcd(a: int, b: int) -> int:
        if a < b:
            a, b = b, a

        while b > 0:
            a, b = a-b, b
            if a < b:
                a, b = b, a

        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next
        while cur:
            val = Solution.gcd(prev.val, cur.val)
            new_node = ListNode(val)
            prev.next = new_node
            new_node.next = cur
            prev = cur
            cur = cur.next

        return head
