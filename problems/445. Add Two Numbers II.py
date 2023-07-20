# link: https://leetcode.com/problems/add-two-numbers-ii/submissions/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# reverse linked-list
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while l1:
            temp = l1.next
            l1.next = prev
            prev = l1
            l1 = temp
        l1 = prev

        prev = None
        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp
        l2 = prev

        cur = None
        carry = 0
        while l1 or l2 or carry > 0:
            if l1 and l2:
                val = l1.val+l2.val+carry
            elif l1:
                val = l1.val+carry
            elif l2:
                val = l2.val+carry
            else:
                val = carry
            carry = val // 10
            val %= 10
            cur = ListNode(val, cur)
        
        return cur
            
# stack
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        cur = None
        carry = 0
        while s1 or s2 or carry > 0:
            val = (s1.pop() if s1 else 0) + (s2.pop() if s2 else 0) + carry
            carry = val // 10
            val %= 10
            cur = ListNode(val, cur)
        
        return cur