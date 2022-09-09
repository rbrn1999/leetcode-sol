# link: https://leetcode.com/problems/mirror-reflection/

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        def gcd(x, y):
           while(y):
               x, y = y, x % y
           return x

        def lcm(x, y):
           lcm = (x*y)//gcd(x,y)
           return lcm

        turn = lcm(p, q)
        bottom = (turn // q) % 2
        left = (turn // p) % 2

        while bottom & left == 1:
            turn *= 2
            bottom = (turn // q) % 2
            left = (turn // p) % 2

        return (1 - bottom) +left
