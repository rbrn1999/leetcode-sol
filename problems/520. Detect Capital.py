# link: https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if n <= 1:
            return True

        if word[0].islower():
            for i in range(1, n):
                if word[i].isupper():
                    return False
            return True

        if word[1].islower():
            for i in range(2, n):
                if word[i].isupper():
                    return False
            return True
        else:
            for i in range(2, n):
                if word[i].islower():
                    return False
            return True

