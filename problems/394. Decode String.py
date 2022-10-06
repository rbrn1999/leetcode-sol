# link: https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        stack = [["", 1]]
        for c in s:
            if c == '[':
                stack.append(["", num])
                num = 0
            elif c == ']':
                bufferString, times = stack.pop()
                stack[-1][0] += bufferString * times
            elif c.isdigit():
                num = num * 10 + int(c)
            else:
                stack[-1][0] += c
        return stack[0][0]
