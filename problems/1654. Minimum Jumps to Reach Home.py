# link: https://leetcode.com/problems/minimum-jumps-to-reach-home/

from collections import deque
class Solution:
    def minimumJumps(self, forbidden: list[int], a: int, b: int, x: int) -> int:
        if x == 0:
            return 0
        forbidden = set(forbidden)
        upper_bound = max(x, max(forbidden)) + a + b
        q = deque()
        q.append((0, True)) # pos, isAbleToJumpBack
        visited = set()
        visited.add((0, True))
        steps = 0
        while q:
            for _ in range(len(q)):
                i, canJumpBack = q.popleft()
                if i + a == x or (canJumpBack and i - b == x):
                    return steps + 1
                if i + a not in forbidden and (i+a, True) not in visited \
                    and i <= upper_bound:
                    q.append((i+a, True))
                    visited.add((i+a, True))
                    visited.add((i+a, False))
                if canJumpBack and i - b > 0 and i - b not in forbidden and (i-b, False) not in visited:
                    q.append((i-b, False))
                    visited.add((i-b, False))
            steps += 1
        
        return -1


