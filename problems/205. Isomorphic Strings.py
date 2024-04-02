# link: https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        used = set()
        for i in range(len(s)):
            if s[i] in char_map:
                if char_map[s[i]] != t[i]:
                    return False
            elif t[i] in used:
                return False
            else:
                char_map[s[i]] = t[i]
                used.add(t[i])

        return True
