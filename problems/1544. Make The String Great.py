# link: https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and c.lower() == stack[-1].lower() and (c.islower() ^ stack[-1].islower()):
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)

