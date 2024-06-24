# link: https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        def isValid(force: int) -> bool:
            prev = position[0]
            balls = m-1
            for p in position[1:]:
                if p - prev >= force:
                    balls -= 1
                    prev = p
                    if balls == 0:
                        return True
            
            return False

        position.sort()
        low = 1
        high = (max(position) - min(position)) // (m-1)

        while low < high:
            mid = (low + high + 1) // 2
            if isValid(mid):
                low = mid
            else:
                high = mid - 1
        
        return low