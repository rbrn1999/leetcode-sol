# link: https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def isValid(target):
            cost = -target
            if (index+1) >= target:
                cost += ((1 + target) * target) // 2 + (index+1) - target
            else:
                cost += ((2 * target - index) * (index+1)) // 2
            if n - 1 - index >= target:
                cost += ((1 + target) * target) // 2 + n - index - target
            else:
                cost += ((2 * target - (n - 1 - index)) * (n-index)) // 2
            return cost <= maxSum
        
        low = maxSum // n
        high = maxSum - n + 1
        while low + 1 < high:
            mid = low + (high - low) // 2
            if isValid(mid):
                low = mid
            else:
                high = mid - 1
        
        return high if isValid(high) else low
    