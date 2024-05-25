# link: https://leetcode.com/problems/different-ways-to-add-parentheses/

import itertools
from operator import add, sub, mul
class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        ops = {'+': add, '-': sub, '*': mul}
        memo = {}
        def dfs(exp: str) -> list[int]:
            if exp in memo:
                return memo[exp]
            if exp.isdigit():
                memo[exp] = [int(exp)]
                return [int(exp)]

            results = []

            for i in range(1, len(exp)):
                if exp[i] not in ops:
                    continue

                op = ops[exp[i]]
                lhs = dfs(exp[:i])
                rhs = dfs(exp[i+1:])
                for l, r in itertools.product(lhs, rhs):
                    results.append(op(l, r))
                
            memo[exp] = results
            return results
        
        return dfs(expression)

                