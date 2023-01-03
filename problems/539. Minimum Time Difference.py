# link: https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for timePoint in timePoints:
            hour = int(timePoint[:2])
            minute = int(timePoint[-2:])
            minutes.append(hour*60 + minute)
        minutes.sort()
        minDiff = float('inf')
        for i in range(1, len(minutes)):
            minDiff = min(minDiff, minutes[i] - minutes[i-1])

        minDiff = min(minDiff, (60 * 24 + minutes[0] - minutes[-1]))
        return minDiff

