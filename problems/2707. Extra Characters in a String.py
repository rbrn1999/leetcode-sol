# link: https://leetcode.com/problems/extra-characters-in-a-string/

# DP
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = list(range(len(s)+1)) # dp[i]: the min cost of  building s[0~i] (inclusive)

        for i in range(len(s)+1):
            dp[i] = min(dp[i], dp[i-1] + 1)
            for word in dictionary:
                if s[i:i+len(word)] == word:
                    dp[i+len(word)] = min(dp[i], dp[i+len(word)])

        return dp[-1]

# DP, HashSet
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = list(range(n+1))
        words = set(dictionary)
        k = max(len(word) for word in dictionary)

        for i in range(n+1):
            dp[i] = min(dp[i], dp[i-1] + 1)
            for j in range(i+1, min(n, i+k) + 1):
                if s[i:j] in words:
                    dp[j] = min(dp[i], dp[j])

        return dp[n]


# DP, Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self, dictionary: list[str]):
        self.root = TrieNode()
        for word in dictionary:
            self.insert(word)

    def insert(self, word: str):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = list(range(n+1)) # dp[i]: the min cost of  building s[0~i] (inclusive)
        trie = Trie(dictionary)

        k = max(len(word) for word in dictionary)

        for i in range(n+1):
            dp[i] = min(dp[i], dp[i-1] + 1)
            node = trie.root
            for j in range(i, min(n, i+k)):
                if s[j] in node.children:
                    node = node.children[s[j]]
                    if node.is_word:
                        dp[j+1] = min(dp[j+1], dp[i])
                else:
                    break

        return dp[n]
