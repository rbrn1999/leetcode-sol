# link: https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

import sys

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = [sys.maxsize, -1]
        prevDistance = sys.maxsize
        totalDistance = -1
        prevVal = head.val
        cur = head.next

        while cur.next:
            prevDistance += 1
            if (prevVal > cur.val and cur.next.val > cur.val) or (prevVal < cur.val and cur.next.val < cur.val):
                result[0] = min(result[0], prevDistance)
                prevDistance = 0
                if totalDistance == -1:
                    totalDistance = 0
                else:
                    result[1] = totalDistance
            
            if totalDistance != -1:
                totalDistance += 1
            
            prevVal = cur.val
            cur = cur.next
        
        return [result[0] if result[0] < sys.maxsize else -1, result[1]]