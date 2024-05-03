# link: https://leetcode.com/problems/sentence-screen-fitting/

# Approach 1

from functools import cache
class Solution:
    def wordsTyping(self, sentence: list[str], rows: int, cols: int) -> int:
        maxLen = max(len(word) for word in sentence)
        if maxLen > cols:
            return 0

        @cache
        def helper(col: int) -> tuple[int, int]: # return new end position (dr, c)
            r, c = 0, col-1
            i = 0
            while i < len(sentence):
                if c + len(sentence[i]) + int(c != -1) >= cols:
                    r += 1
                    c = -1
                else:
                    c += len(sentence[i]) + int(c != -1)
                    i += 1
            return (r + c//cols, c%cols)

        n = len(sentence)
        count = 0
        r, c = 0, -1
        while r < rows:
            dr, c = helper(c+1)
            count += 1
            r += dr
            if 1 + len(sentence[0]) + c >= cols: # start at start of the line again
                return count * rows // (r+1)

        return count - 1

# Approach 2

from functools import cache
class Solution:
    def wordsTyping(self, sentence: list[str], rows: int, cols: int) -> int:
        n = len(sentence)

        @cache
        def fillRow(i: int) -> tuple[int, int]: # the line starts with the i-th word, return the new index and complete counts
            c, completes = 0, 0
            while c + len(sentence[i]) <= cols:
                c += len(sentence[i]) + 1
                i += 1
                if i == n:
                    completes += 1
                    i = 0

            return i, completes

        answer = 0
        i = 0
        for _ in range(rows):
            i, completes = fillRow(i)
            answer += completes

        return answer
