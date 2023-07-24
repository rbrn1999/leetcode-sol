# link: https://leetcode.com/problems/powx-n/

# Recursive
# Approach 1
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        temp = self.myPow(x, abs(int(n/2)))
        product = temp * temp
        if n % 2 == 1:
            product *= x
        return product if n > 0 else 1 / product
# Approach 2
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n *= -1
        if n == 0:
            return 1
        
        if n % 2:
            return x * self.myPow(x**2, (n-1)//2)
        else:
            return self.myPow(x**2, n//2)
    
# Iterative
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n *= -1
        if n == 0:
            return 1
        
        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
                n -= 1
            x = x ** 2
            n = n // 2
        
        return result