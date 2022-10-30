class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_dict = {} # count: [word]
        for word in wordDict:
            word_dict.setdefault(len(word), [])
            word_dict[len(word)].append(word)
        memo = {} # index: valid
        n = len(s)
        def isValid(i):
            if i == n:
                return True
            if i > n:
                return False
            if i in memo:
                return memo[i]
            for j, words in word_dict.items():
                for word in words:
                    if s[i:i+j] == word and isValid(i+j):
                        memo[i] = True
                        return True
            
            memo[i] = False
            return False

        return isValid(0)

print(Solution().wordBreak("applepenapple", ["apple","pen"]))