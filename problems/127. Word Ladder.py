# link: https://leetcode.com/problems/word-ladder/

from collections import deque
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        steps = 1
        words = set(wordList)
        visited = set()
        q = deque()
        q.append(beginWord)
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return steps
                visited.add(word)
                for i in range(len(word)):
                    for letter in string.ascii_lowercase:
                        n_word = word[:i] + letter + word[i+1:]
                        if n_word in words and n_word not in visited:
                            q.append(n_word)

            steps += 1

        return 0

