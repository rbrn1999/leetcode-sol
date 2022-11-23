# link: https://leetcode.com/problems/ugly-number/

# brute force
class Solution:
    def isUgly(self, n: int) -> bool:
        def isPrettyPrime(n):
            if n in [2, 3, 5]:
                return False
            res = n > 1
            for i in range(2, int(sqrt(n))+1):
                if n % i == 0:
                    return False
            return res

        if n <= 0:
            return False

        for i in range(1, int(sqrt(n))+1):
            if n % i == 0 and (isPrettyPrime(i) or isPrettyPrime(n//i)):
                return False

        return True

# optimal
# solution reference: https://leetcode.com/problems/ugly-number/discuss/69305
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        primes = [2, 3, 5]
        for p in primes:
            while n % p == 0:
                n /= p
        return n == 1
