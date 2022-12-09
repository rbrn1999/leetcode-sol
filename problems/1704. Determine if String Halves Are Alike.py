# link: https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        n = len(s)
        count = 0
        for i in range(n // 2):
            count += int(s[i] in vowels)
        for i in range(n // 2, n):
            count -= int(s[i] in vowels)

        return count == 0

