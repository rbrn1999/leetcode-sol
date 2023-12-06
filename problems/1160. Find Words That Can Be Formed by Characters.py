# link: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

from collections import Counter
class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        chars_count = Counter(chars)
        ans = 0
        for word in words:
            word_count = Counter(word)
            valid = True
            for c in word_count:
                if word_count[c] > chars_count.get(c, 0):
                    valid = False
                    break
            if valid:
                ans += len(word)
        
        return ans