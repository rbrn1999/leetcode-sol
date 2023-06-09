# link: https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = [None] * (len(word1) + len(word2))
        n = min(len(word1), len(word2))
        for i in range(n):
            answer[2*i] = word1[i]
            answer[2*i+1] = word2[i]

        if len(word1) > n:
            answer[2*n:] = [c for c in word1[n:]]
        elif len(word2) > n:
            answer[2*n:] = [c for c in word2[n:]]

        return ''.join(answer)


# shorter more pythonic version
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        n = min(len(word1), len(word2))
        for i in range(n):
            answer.append(word1[i])
            answer.append(word2[i])

        return ''.join(answer) + word1[n:] + word2[n:]

