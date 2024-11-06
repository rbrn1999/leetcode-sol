# link: https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        for i in range(0, len(s), 2):
            changes += int(s[i] != s[i+1])
        
        return changes