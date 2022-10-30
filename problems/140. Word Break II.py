# link: https://leetcode.com/problems/word-break-ii/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        sentences = []
        def dfs(wordInds=[], i=0):
            if i == n:
                sentences.append(' '.join(wordDict[j] for j in wordInds))
                return
            elif i > n:
                return

            for j, word in enumerate(wordDict):
                if s[i:i+len(word)] == word:

                    dfs(wordInds + [j], i+len(word))

        dfs()
        return sentences

