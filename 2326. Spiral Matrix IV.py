# link: https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> list[list[int]]:
        matrix = [[-1] * n for _ in range(m)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c = 0, -1
        d = 0
        cur = head
        while cur:
            nr, nc = r+dirs[d][0], c+dirs[d][1]
            if nr >= m or nr < 0 or nc >= n or nc < 0 or matrix[nr][nc] != -1:
                d = (d + 1) % 4
            
            r, c = r+dirs[d][0], c+dirs[d][1]
            matrix[r][c] = cur.val
            cur = cur.next
        
        return matrix
