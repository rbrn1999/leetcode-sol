# link: https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def isValid(value):
            count = 1
            prev = price[0]

            for i in range(1, n):
                if price[i] - prev >= value:
                    count += 1
                    prev = price[i]

            return count >= k

        n = len(price)
        price.sort()
        result = 0
        low = 0
        high = price[-1] - price[0]

        while low <= high:
            mid = low + (high - low) // 2

            if isValid(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result
