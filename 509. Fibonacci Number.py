# link: https://leetcode.com/problems/fibonacci-number/

class Solution:
    memory = {0:0, 1:1}
    def fib(self, n: int) -> int:
        if n in self.memory:
            return self.memory[n]
        else:
            self.memory[n] =  self.fib(n-1) + self.fib(n-2)
            return self.memory[n]
