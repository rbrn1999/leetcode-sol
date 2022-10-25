# link: https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n-1)
        result = []
        start = end = 0
        while end < len(s):
            if s[end] == s[start]:
                end += 1
            else:
                result += [str(end-start), s[start]]
                start = end
        result += [str(end-start), s[start]]
        return ''.join(result)
