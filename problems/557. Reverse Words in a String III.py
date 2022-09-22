# link: https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        for word in s.split():
            result.append(word[::-1])
        return ' '.join(result)
