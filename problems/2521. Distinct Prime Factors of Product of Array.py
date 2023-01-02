# link: https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

import math
from functools import cache
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes = set()
        @cache
        def isPrime(num):
            if num < 2:
                return False
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    return False
            return True

        def findPrimes(num):
            for i in range(1, int(math.sqrt(num))+1):
                if num % i != 0:
                    continue
                if isPrime(i):
                    primes.add(i)
                if isPrime(num // i):
                    primes.add(num // i)

        for num in nums:
            findPrimes(num)
        return len(primes)

