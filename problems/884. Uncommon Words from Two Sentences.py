# link: https://leetcode.com/problems/uncommon-words-from-two-sentences/

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = {}
        for w in s1.split():
            words[w] = words.get(w, 0) + 1
        for w in s2.split():
            words[w] = words.get(w, 0) + 1
        
        return [w for w in words if words[w] == 1]
        