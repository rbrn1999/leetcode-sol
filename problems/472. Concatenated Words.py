# link: https://leetcode.com/problems/concatenated-words/

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words + [""])
        memo = {}
        def dfs(word):
            if word in memo:
                return memo[word]
            memo[word] = False
            for i in range(1, len(word)):
                if (word[:i] in wordSet or dfs(word[:i])) and (word[i:] in wordSet or dfs(word[i:])):
                    memo[word] = True
                    break
            return memo[word]

        result = []
        for word in sorted(words):
            if dfs(word):
                result.append(word)

        return result
