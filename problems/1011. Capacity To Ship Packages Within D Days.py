# link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValid(maxWeight: int) -> bool:
            day = 1
            weightSum = 0
            for weight in weights:
                if weightSum + weight <= maxWeight:
                    weightSum += weight
                elif weight <= maxWeight and day < days:
                    day += 1
                    weightSum = weight
                else:
                    return False

            return True

        low, high = max(weights), sum(weights)

        while low < high:
            mid = low + (high - low) // 2
            if isValid(mid):
                high = mid
            else:
                low = mid + 1

        return low

