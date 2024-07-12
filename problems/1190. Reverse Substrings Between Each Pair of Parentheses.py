# link: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

# Brute Force
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        for c in s:
            if c == '(':
                stack.append([])
            elif c == ')':
                partition = stack.pop()
                stack[-1].extend(partition[::-1])
            else:
                stack[-1].append(c)

        return ''.join(stack[0])

#  Wormhole Teleportation technique
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_parentheses_indices = []
        pairs = [0] * n

        for i, c in enumerate(s):
            if c == '(':
                open_parentheses_indices.append(i)
            elif c == ')':
                j = open_parentheses_indices.pop()
                pairs[i], pairs[j] = j, i

        result = []
        curr_index = 0
        direction = 1

        while curr_index < n:
            if s[curr_index] == '(' or s[curr_index] == ')':
                curr_index = pairs[curr_index]
                direction *= -1
            else:
                result.append(s[curr_index])

            curr_index += direction

        return ''.join(result)
