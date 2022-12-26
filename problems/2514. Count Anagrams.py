# link: https://leetcode.com/problems/count-anagrams/description/

from collections import Counter
from math import factorial
import operator

class Solution:
    def countAnagrams(self, s: str) -> int:
        words = s.split()
        n = len(words)

        result = 1
        for word in words:
            counts = Counter(word).values()
            num = factorial(len(word))
            num //= reduce(operator.mul, (factorial(v) for v in counts))
            result *= num
            result = result % int(1E9 + 7)

        return result

