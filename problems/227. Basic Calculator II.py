# link: https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        sign = 1
        lhs = 0
        current_num = 0
        total = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c == ' ':
                while i + 1 < len(s) and s[i+1] == ' ':
                    i += 1
            elif c.isdigit():
                current_num = current_num * 10 + int(c)
            else:
                lhs = sign * current_num
                current_num = 0
                sign = 1
                if c == '-':
                    sign = -1
                if c == '+' or c == '-':
                    total += lhs
                elif c == '*' or c == '/':
                    l = i + 1
                    while s[l] == ' ':
                        l += 1
                    r = l
                    while r < len(s) and s[r].isdigit():
                        r += 1
                    
                    rhs = int(s[l:r])
                    if c == '*':
                        current_num = (lhs * rhs)
                    else:
                        current_num = int(lhs / rhs) # round to zero
                    
                    i = r - 1
            
            i += 1


        total += sign * current_num
        
        return total
            
