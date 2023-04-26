from collections import deque
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        count = 0
        for c in s:
            if c == ')' and count == 0:
                continue
            
            stack.append(c)
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
        
        if count == 0:
            return ''.join(stack)
        
        q = deque()
        while count > 0:
            c = stack.pop()
            if c == '(':
                count -= 1
            else:
                q.appendleft(c)
        
        q.extendleft(stack[::-1])
        return ''.join(q)

# cleaner solution by: asivura

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        answer = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    answer.append('')
                    continue
            answer.append(s[i])
        
        while stack:
            answer[stack.pop()] = ''
        
        return ''.join(answer)
        