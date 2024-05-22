# link: https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)

        prevArriveTime = 0
        fleets = 0

        for p, s in pairs:
            time = (target - p) / s
            if time > prevArriveTime: # does arrive at the same time or early than the previous fleet
                # form a new fleet
                fleets += 1
                prevArriveTime = time
        
        return fleets