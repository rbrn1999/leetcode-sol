# link: https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
n: number of nodes, k: number of linked lists
Time Complexity: O(nlogk)
Space Complexity: O(n)
''' 
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # (value, list index)
        heap = []
        for i in range(len(lists)):
            if lists[i] is not None:
                val = lists[i].val
                heapq.heappush(heap, (val, i))
                lists[i] = lists[i].next
        cur = head = None
        while heap:
            val, i = heapq.heappop(heap)
            node = ListNode(val=val)
            if head is None:
                head = cur = node
            else:
                cur.next, cur = node, node
            if lists[i] is not None:
                val = lists[i].val
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        return head