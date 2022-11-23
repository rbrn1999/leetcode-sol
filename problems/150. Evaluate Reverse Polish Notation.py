# link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = []
        for token in tokens:
            if token in ops:
                rhs = stack.pop()
                lhs = stack.pop()
                if token == '+':
                    stack.append(lhs + rhs)
                elif token == '-':
                    stack.append(lhs - rhs)
                elif token == '*':
                    stack.append(lhs * rhs)
                elif token == '/':
                    sign = -1 if (lhs < 0) ^ (rhs < 0) else 1
                    stack.append(abs(lhs) // abs(rhs) * sign)
                else:
                    print('something is wrong')
            else:
                stack.append(int(token))

        return stack[-1]
