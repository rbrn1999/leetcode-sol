# link: https://leetcode.com/problems/merge-in-between-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        a_node = None
        b_node = None
        dummy = ListNode(next=list1)

        a_node = dummy
        for _ in range(a):
            a_node = a_node.next

        b_node = a_node
        for _ in range(b-a+2):
            b_node = b_node.next
        
        c_node = list2
        while c_node.next:
            c_node = c_node.next
        
        a_node.next = list2
        c_node.next = b_node

        return dummy.next