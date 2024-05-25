# link: https://leetcode.com/problems/race-car/

# BFS
from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        q = deque()
        visited = set()
        q.append((0, 1)) # (position, speed)

        sequence_length = 0

        while q:
            for _ in range(len(q)):
                pos, speed = q.popleft()
                if pos == target:
                    return sequence_length

                # Accelerate
                new_pos = pos + speed
                new_speed = speed * 2
                # if we are at 2 * target, it's the same as being at pos=0 with a different direction (not sure how to proof this), similar for the negative pos
                if new_pos < 2 * target and new_pos > 0 and (new_pos, new_speed) not in visited:
                    visited.add((new_pos, new_speed))
                    q.append((new_pos, new_speed))
                
                # Reverse
                new_speed = 1 if speed < 0 else -1
                if (pos, new_speed) not in visited:
                    visited.add((pos, new_speed))
                    q.append((pos, new_speed))
            
            sequence_length += 1
        
        return -1