# link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        opens = 0
        for c in s:
            if c == '(':
                opens += 1
            elif opens > 0:
                opens -= 1
            else:
                count += 1 # insert open parentheses
        
        return count + opens