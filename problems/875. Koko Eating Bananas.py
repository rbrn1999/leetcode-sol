# link: https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        def isValid(k):
            hour_count = 0
            for i in range(n):
                hour_count += math.ceil(piles[i] / k)
                if hour_count > h:
                    return False

            return True

        high = max(piles)
        low = math.ceil(sum(piles) / h)
        while low < high:
            mid = low + (high - low) // 2
            if isValid(mid):
                high = mid
            else:
                low = mid + 1

        return low

