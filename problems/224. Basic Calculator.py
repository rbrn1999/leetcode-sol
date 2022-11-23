# link: https://leetcode.com/problems/basic-calculator/

class Solution:
    def calculate(self, s: str) -> int:
        def getNumEnd(i):
            end = i
            while end < len(s) and s[end].isdigit():
                end += 1
            return end
        
        n = len(s)
        stack = []
        sign = 1
        i = 0
        op = 1
        res = 0
        while i < n:
            if s[i] == '(':
                stack.append(op)
                sign *= op
                op = 1
            elif s[i] == ')':
                sign *= stack.pop()
            elif s[i] == '+':
                op = 1
            elif s[i] == '-':
                op = -1
            elif s[i].isdigit():
                end = getNumEnd(i)
                num = int(s[i:end])
                res += sign * op * num
                i = end - 1
            else:
                pass
            i += 1
            
        return res