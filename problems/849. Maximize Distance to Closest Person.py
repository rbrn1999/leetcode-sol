# link: https://leetcode.com/problems/maximize-distance-to-closest-person/

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        distance = 1
        prev = -1
        for i in range(n):
            if seats[i] == 0:
                continue
            distance = max(distance, (i-prev) // 2) if prev >= 0 else i
            prev = i

        return max(distance, n-prev-1)

