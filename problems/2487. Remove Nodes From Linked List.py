# link: https://leetcode.com/problems/remove-nodes-from-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        max_list = collections.deque()
        cur = head
        while cur:
            max_list.append(cur.val)
            cur = cur.next

        for i in range(len(max_list)-2, -1, -1):
            max_list[i] = max(max_list[i], max_list[i+1])

        cur = head
        prev = None
        while cur:
            if max_list.popleft() > cur.val:
                if cur is head:
                    cur = cur.next
                    head = cur
                else:
                    prev.next = cur.next
                    cur = cur.next
            else:
                prev, cur = cur, cur.next

        return head
