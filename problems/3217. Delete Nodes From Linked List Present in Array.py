# link: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        dummy_head = ListNode(next=head)
        prev = dummy_head
        cur = dummy_head.next

        while cur is not None:
            if cur.val in nums_set:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        
        return dummy_head.next
