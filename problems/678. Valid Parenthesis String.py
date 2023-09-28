# link: https://leetcode.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, s: str) -> bool:
        # range of opening parenthesis we have: [open_min, open_max]
        open_min = 0
        open_max = 0

        for c in s:
            match c:
                case '(':
                    open_min += 1
                    open_max += 1
                case ')':
                    open_min = max(open_min-1, 0)
                    open_max -= 1
                case '*':
                    open_min = max(open_min-1, 0)
                    open_max += 1
            if open_max < 0:
                return False
        
        return open_min == 0