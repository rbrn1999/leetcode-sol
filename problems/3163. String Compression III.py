# link: https://leetcode.com/problems/string-compression-iii/

class Solution:
    def compressedString(self, word: str) -> str:
        streak = 1
        result = []
        for i in range(1, len(word)):
            if word[i] == word[i-1] and streak < 9:
                streak += 1
            else:
                result.append(str(streak))
                result.append(word[i-1])
                streak = 1

        result.append(str(streak))
        result.append(word[-1])

        return ''.join(result)
