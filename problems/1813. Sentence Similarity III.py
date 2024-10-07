# link: https://leetcode.com/problems/sentence-similarity-iii/

# Brute Force
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words_1 = sentence1.split()
        words_2 = sentence2.split()

        if len(words_1) > len(words_2):
            words_1, words_2 = words_2, words_1


        offset = len(words_2) - len(words_1)
        for i in range(len(words_1)+1):
            if words_1 == words_2[:i] + words_2[i+offset:]:
                return True

        return False

# Deque
from collections import deque
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words_1 = deque(sentence1.split())
        words_2 = deque(sentence2.split())

        if len(words_1) > len(words_2):
            words_1, words_2 = words_2, words_1


        while words_1 and words_2 and words_1[0] == words_2[0]:
            words_1.popleft()
            words_2.popleft()

        while words_1 and words_2 and words_1[-1] == words_2[-1]:
            words_1.pop()
            words_2.pop()

        return len(words_1) == 0
