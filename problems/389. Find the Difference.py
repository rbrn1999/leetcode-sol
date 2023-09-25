# link: https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(ord(c) for c in t) - sum(ord(c) for c in s))


from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        for c in t:
            if count_s[c] == 0:
                return c
            else:
                count_s[c] -= 1
        
        return '_'