# link: https://leetcode.com/problems/count-vowels-permutation/

from functools import cache
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        @cache
        def helper(i: int, prev: chr) -> int:
            if i == n:
                return 1
            count = 0
            if prev == 'a':
                return helper(i+1, 'e')
            if prev == 'e':
                return (helper(i+1, 'a') + helper(i+1, 'i')) % (10 ** 9 + 7)
            if prev == 'i':
                return (helper(i+1, 'a') + helper(i+1, 'e') + helper(i+1, 'o') + helper(i+1, 'u')) % (10 ** 9 + 7)
            if prev == 'o':
                return (helper(i+1, 'i') + helper(i+1, 'u')) % (10 ** 9 + 7)
            if prev == 'u':
                return helper(i+1, 'a')
        
        count = 0
        for vowel in ('a', 'e', 'i', 'o', 'u'):
            count = (count + helper(1, vowel)) % (10 ** 9 + 7)
        
        return count