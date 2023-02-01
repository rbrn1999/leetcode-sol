# link: https://leetcode.com/problems/greatest-common-divisor-of-strings/

from collections import deque
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def isDivisor(s: str, d: str):
            if len(s) % len(d) != 0:
                return False
            length = len(d)
            for i in range(len(s)//length):
                if s[i*length:(i+1)*length] != d:
                    return False
            return True
        if len(str1) > len(str2):
            str1, str2 = str2, str1

        splits = deque()
        len_str1 = len(str1)
        for i in range(int(math.sqrt(len_str1)), 0, -1):
            if len_str1 % i == 0:
                splits.append(i)
                splits.appendleft(len_str1 // i)

        for i in splits:
            if isDivisor(str1, str1[:i]) and isDivisor(str2, str1[:i]):
                return str1[:i]

        return ""
