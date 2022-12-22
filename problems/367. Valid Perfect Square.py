#link: https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num
        while low <= high:
            mid = low + (high - low) // 2
            square = mid * mid
            if square < num:
                low = mid + 1
            elif square > num:
                high = mid - 1
            else:
                return True
        return False

