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

# Binary Search
class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            leftSum = (1 + mid) * mid // 2
            rightSum = (mid + n) * (n - mid + 1) // 2
            if leftSum < rightSum:
                left = mid + 1
            elif leftSum > rightSum:
                right = mid - 1
            else:
                return mid
        
        return -1