# link: https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        prev_node = dummy_head
        flag = True
        while prev_node.next and flag:
            cur = prev_node.next
            for _ in range(k):
                if not cur:
                    flag = False
                    break
                cur = cur.next
            
            if not flag:
                break

            # reverse
            prev = cur # node next to the reverse portion
            cur = prev_node.next
            last_in_reversed = cur

            for _ in range(k):
                n = cur.next
                cur.next = prev
                prev, cur = cur, n
            prev_node.next = prev # prev: last node in pre-reversed list
            prev_node = last_in_reversed

        return dummy_head.next