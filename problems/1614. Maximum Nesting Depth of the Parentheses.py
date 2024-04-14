# link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        result = 0
        for c in s:
            if c == '(':
                depth += 1
                result = max(result, depth)
            elif c == ')':
                depth -= 1
        
        return result
