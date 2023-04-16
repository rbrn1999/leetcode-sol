# link: https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # head = [1,2,3,4,5], left = 2, right = 4
        # * -> 1 -> (2 -> 3 -> 4) -> 5

        # Use dummy head to rule out edge cases (e.g. "only one node in list", "reverse starts from head")
        dummyHead = ListNode(next=head)
        cur = dummyHead
        prev = None
        for _ in range(left):
            prev = cur
            cur = cur.next

        # start: 1
        # cur: 2
        start = prev # the node to the before "left"

        prev = None
        for _ in range(right - left + 1):
            nextNode = cur.next
            cur.next = prev
            prev, cur = cur, nextNode

        # cur: 5
        # prev (last node to reverse in the original list): 4
        # traverse prev: 4 -> 3 -> 2 -> NULL
        # traverse dummy head: * -> 1(start) -> (2 -> NULL)

        # 2 -> 5
        # 1 -> 4
        start.next.next = cur
        start.next = prev

        # 1 -> 4 -> 3 -> 2 -> 5
        return dummyHead.next

