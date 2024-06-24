# link: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        def canMake(days: int) -> bool:
            consequtive = 0
            bouquets = 0
            for flower in bloomDay:
                if flower <= days:
                    consequtive += 1
                    if consequtive == k:
                        bouquets += 1
                        consequtive = 0
                        if bouquets == m:
                            return True
                else:
                    consequtive = 0
            
            return False


        n = len(bloomDay)
        if k * m > n:
            return -1
        
        low = 0
        high = max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if canMake(mid):
                high = mid
            else:
                low = mid + 1
        
        return low