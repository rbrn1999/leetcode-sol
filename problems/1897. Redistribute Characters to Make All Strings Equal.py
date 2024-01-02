# link: https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        count = {}
        for word in words:
            for c in word:
                count[c] = count.get(c, 0) + 1
        
        for c in count.values():
            if c % len(words) != 0:
                return False
        
        return True