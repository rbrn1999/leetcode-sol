# link: https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n += 1
        
        l = n // k
        r = n % k

        answer = [head]
        cur = head
        for _ in range(k-1):
            for _ in range(l + int(r>0)-1):
                cur = cur.next
                if cur is None:
                    break
            if cur:
                prev, cur = cur, cur.next
                prev.next = None
            answer.append(cur)
            r -= 1


        return answer
