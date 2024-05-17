# link: https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

# 2 Directions

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        opening = 0
        wild = 0
        for i in range(len(s)):
            if locked[i] == '0':
                wild += 1
            elif s[i] == '(':
                opening += 1
            elif opening > 0:
                opening -= 1
            elif wild > 0:
                wild -= 1
            else:
                return False

        closing = 0
        wild = 0
        closing = 0
        wild = 0
        for i in range(len(s)-1, -1, -1):
            if locked[i] == '0':
                wild += 1
            elif s[i] == ')':
                closing += 1
            elif closing > 0:
                closing -= 1
            elif wild > 0:
                wild -= 1
            else:
                return False

        return True

# Stack
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        unlocked_idx = []
        opening_idx = []
        for i in range(len(s)):
            if locked[i] == '0':
                unlocked_idx.append(i)
            elif s[i] == ')':
                if opening_idx:
                    opening_idx.pop()
                elif unlocked_idx:
                    unlocked_idx.pop()
                else:
                    return False
            else:
                opening_idx.append(i)

        while opening_idx:
            if not unlocked_idx or unlocked_idx.pop() < opening_idx.pop():
                return False

        return len(unlocked_idx) % 2 == 0
