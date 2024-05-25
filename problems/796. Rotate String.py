# link: https://leetcode.com/problems/rotate-string/

# Brute Force
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
            
        for i in range(len(s)):
            valid = True
            for j in range(len(s)):
                if s[(i+j) % len(s)] != goal[j]:
                    valid = False
                    break

            if valid:
                return True
        
        return False