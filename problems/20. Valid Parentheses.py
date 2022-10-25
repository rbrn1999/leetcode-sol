# link: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        bracketsTable = {'(' : ')', '[' : ']', '{' : '}'}
        for l in s:
            if l in bracketsTable:
                brackets.append(l)
            else:
                if brackets and bracketsTable[brackets.pop()] == l:
                    continue
                else:
                    return False
            
        return True if not brackets else False