# link: https://leetcode.com/problems/number-of-atoms/

# Stack
from collections import defaultdict
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]

        i = 0
        while i < len(formula):
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                multiplier = 0
                i += 1
                while i < len(formula) and formula[i].isdigit():
                    multiplier = multiplier * 10 + int(formula[i])
                    i += 1
                multiplier = max(1, multiplier)
                for atom, count in stack.pop().items():
                    stack[-1][atom] += count * multiplier
            else:
                j = i + 1
                while j < len(formula) and formula[j].islower():
                    j += 1

                k = j
                multiplier = 0
                while k < len(formula) and formula[k].isdigit():
                    multiplier = multiplier * 10 + int(formula[k])
                    k += 1
                multiplier = max(1, multiplier)
                stack[-1][formula[i:j]] += multiplier
                i = k

        atom_count = stack.pop()
        result = []

        for atom in sorted(atom_count.keys()):
            result.append(atom)
            if atom_count[atom] > 1:
                result.append(str(atom_count[atom]))

        return ''.join(result)
