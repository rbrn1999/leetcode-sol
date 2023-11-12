# link: https://leetcode.com/problems/find-the-winner-of-an-array-game/

from collections import deque
class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        
        q = deque(arr[1:])
        cur = arr[0]

        wins = 0
        while wins < k:
            num = q.popleft()
            if num > cur:
                q.append(cur)
                cur = num
                wins = 0
            else:
                q.append(num)
            wins += 1
        
        return cur