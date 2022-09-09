# link: https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}

        for c in s:
            if c not in d:
                d[c] = 1
            elif d[c] == 1:
                d[c] += 1
            else:
                pass

        for i in range(len(s)):
            if d[s[i]] == 1:
                return i

        return -1
