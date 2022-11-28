# link: https://leetcode.com/problems/find-the-pivot-integer/

class Solution:
    def pivotInteger(self, n: int) -> int:
        left = (1 + n) * n // 2
        right = 0
        for num in range(n, 0, -1):
            right += num
            if left == right:
                return num
            left -= num

        return -1
