# link: https://leetcode.com/problems/decoded-string-at-index/

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        l = 0
        i = -1
        while l < k:
            i += 1
            if s[i].isdigit():
                l *= int(s[i])
            else:
                l += 1
            
        for j in range(i, -1, -1):
            if s[j].isdigit():
                l //= int(s[j])
                k %= l
            else:
                if k == l or k == 0:
                    return s[j]
                l -= 1
        
        return ""
        