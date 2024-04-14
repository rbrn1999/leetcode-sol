# link: https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and int(stack[-1]) > int(digit):
                k -= 1
                stack.pop()
            stack.append(digit)
        
        stack = stack[:len(stack) - k]
        
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
        
        stack = stack[i:]
        if not stack:
            return '0'
        else:
            return ''.join(stack)
