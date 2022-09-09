# link: https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # calculate list length
        lenA = lenB = 0
        cur = headA
        while cur:
            cur = cur.next
            lenA += 1

        cur = headB
        while cur:
            cur = cur.next
            lenB += 1

        # truncate the longer list from the head to make them the same length
        if lenA > lenB:
            for _ in range(lenA - lenB):
                headA = headA.next
        elif lenB > lenA:
            for _ in range(lenB - lenA):
                headB = headB.next

        # compare if the two nodes are the same from head to tail
        while headA or headB:
            if headA is headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
