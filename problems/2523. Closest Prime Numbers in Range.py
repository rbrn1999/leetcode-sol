# link: https://leetcode.com/problems/closest-prime-numbers-in-range/

from functools import cache
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        @cache
        def isPrime(num):
            if num < 2:
                return False
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    return False
            return True

        answer = [-1, -1]
        maxDiff = float('inf')

        num1 = left
        while num1 < right and maxDiff > 2:
            if not isPrime(num1):
                num1 += 1
                continue
            found = False
            for num2 in range(num1+1, min(num1+maxDiff, right+1)):
                if isPrime(num2):
                    maxDiff = num2 - num1
                    answer = [num1, num2]
                    num1 = num2
                    found = True
                    break
            if not found:
                num1 += maxDiff

        return answer

