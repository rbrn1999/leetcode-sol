# top-bottom, recursion
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
# bottom-up, don't use length_words to get better space complexity and same time complexity(but slower runtime)
from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n
        length_words = defaultdict(set)
        for word in wordDict:
            length_words[len(word)].add(word)
        
        for i in range(n):
            if not dp[i]:
                continue
            for length in length_words:
                subString = s[i:i+length]
                if i+length >= n+1 or dp[i+length]:
                    continue
                for word in length_words[length]:
                    if word == subString:
                        dp[i+length] = True
                        break
        
        return dp[-1]
# bottom-up, optimized space, don't use length_words to get better space complexity and same time complexity(but slower runtime)
from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        m = max(len(word) for word in wordDict)
        n = len(s)
        dp = [True] + [False] * m
        length_words = defaultdict(set)
        for word in wordDict:
            length_words[len(word)].add(word)
        
        for i in range(n):
            if not dp[i%(m+1)]:
                continue
            for length in length_words:
                subString = s[i:i+length]
                if i+length >= n+1 or dp[(i+length)%(m+1)]:
                    continue
                for word in length_words[length]:
                    if word == subString:
                        dp[(i+length)%(m+1)] = True
                        break
            if i < n-1:
                dp[i%(m+1)] = False
            
        return dp[n%(m+1)]