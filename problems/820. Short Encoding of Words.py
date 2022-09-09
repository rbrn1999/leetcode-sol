# link: https://leetcode.com/problems/short-encoding-of-words/

class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:


        words.sort(key=len, reverse=True)
        unique = []
        count = 0

        def isSeen(w):
            for i in range(len(unique)-1, -1, -1):
                if w in unique[i][-len(w):]:
                    return True
            return False

        for word in words:
            if not isSeen(word):
                unique.append(word)
                count += len(word) + 1

        return count
