# link: https://leetcode.com/problems/minimum-time-to-complete-trips/

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def canComplete(targetTime):
            total = 0
            for t in time:
                total += targetTime // t
                if total >= totalTrips:
                    return True
            return False

        low = 1
        high = totalTrips  * min(time)

        while low < high:
            mid = low + (high - low) // 2
            if canComplete(mid):
                high = mid
            else:
                low = mid + 1

        return low

