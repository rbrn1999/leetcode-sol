# link: https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tokenWord = {}
        usedWords = set()
        words = s.split()
        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in tokenWord:
                if words[i] in usedWords:
                    return False
                else:
                    usedWords.add(words[i])
                tokenWord[pattern[i]] = words[i]
            elif tokenWord[pattern[i]] != words[i]:
                return False
            else:
                pass

        return True

