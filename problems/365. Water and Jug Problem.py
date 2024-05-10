# link: https://leetcode.com/problems/water-and-jug-problem/

from collections import deque
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False

        q = deque([(0, 0)])
        visited = set([(0, 0)])

        while q:
            amount_x, amount_y = q.popleft()

            if amount_x + amount_y == target:
                return True
            
            # (fill x), (fill y), (empty x), (empty y), (pour x to y), (pour y to x)
            next_states = [(x, amount_y), (amount_x, y), (0, amount_y), (amount_x, 0),
                (min(amount_x + amount_y, x), (0 if amount_x + amount_y <= x else amount_y - (x - amount_x))),
                (min(amount_x + amount_y, y), (0 if amount_x + amount_y <= y else amount_x - (y - amount_y))),
            ]

            for state in next_states:
                if state in visited:
                    continue
                else:
                    visited.add(state)
                    q.append(state)
            
        return False