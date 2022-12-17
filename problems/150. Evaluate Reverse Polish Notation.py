# link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

# 2022/12/17
# shorter solution
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        num_stack = []
        ops = {'+': lambda lhs, rhs: lhs + rhs,
            '-': lambda lhs, rhs: lhs - rhs,
            '*': lambda lhs, rhs: lhs * rhs,
            '/': lambda lhs, rhs: abs(lhs) // abs(rhs) * (-1 if ((lhs < 0) ^ (rhs < 0)) else 1)}

        for token in tokens:
            if len(token) > 1 or token.isdigit():
                num_stack.append(int(token))
            else:
                rhs = num_stack.pop()
                lhs = num_stack.pop()
                num_stack.append(ops[token](lhs, rhs))
        
        return num_stack[0]

# 2022/11/15
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
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
