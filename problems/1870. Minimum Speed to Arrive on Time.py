# link: https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def inTime(speed: int) -> bool:
            t = 0
            for i in range(len(dist)-1):
                t += math.ceil(dist[i] / speed)
                if t >= hour:
                    return False
            return t + dist[-1] / speed <= hour

        n = len(dist)
        if n-1 >= hour:
            return -1
        
        low = 1
        high = max(dist[:-1]) if len(dist) > 1 else 0
        high = max(high, math.ceil(dist[-1] / (hour-(n-1))))

        while low < high:
            mid = low + (high - low) // 2
            if inTime(mid):
                high = mid
            else:
                low = mid + 1
        
        return low