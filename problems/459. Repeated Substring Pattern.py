# link: https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i != 0:
                continue
            flag = True
            for j in range(1, n // i):
                if s[:i] != s[j*i:j*i+i]:
                    flag = False
                    break
            if flag:
                return True
        
        return False

# short solution with Python syntax sugar
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0 and s[:i] * (n // i) == s:
                return True

        return False