# link: https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        perm = []
        low = 0
        high = len(s)
        for c in s:
            if c == 'I':
                perm.append(low)
                low += 1
            else:
                perm.append(high)
                high -= 1
        
        perm.append(low)
        return perm
        