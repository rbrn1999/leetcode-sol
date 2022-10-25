# link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i, j = 0, 0
        char_1, char_2 = 0, 0
        while i<len(word1) and j<len(word2):
            if word1[i][char_1] != word2[j][char_2]:
                return False
            else:
                char_1 += 1
                char_2 += 1
            if char_1 >= len(word1[i]):
                i += 1
                char_1 = 0
            if char_2 >= len(word2[j]):
                j += 1
                char_2 = 0
        if i < len(word1) or j < len(word2):
            return False
        else:
            return True
