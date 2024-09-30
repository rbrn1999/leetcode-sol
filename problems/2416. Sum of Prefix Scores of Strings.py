# link: https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self, words: list[str]):
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word: str):
        cur = self.root
        for c in word:
            cur.children.setdefault(c, TrieNode())
            cur = cur.children[c]
            cur.count += 1


    def get_score(self, word: str) -> int:
        cur = self.root
        count = 0
        for c in word:
            if c not in cur.children:
                break
            cur = cur.children[c]
            count += cur.count

        return count

class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        prefix_tree = Trie(words)
        return [prefix_tree.get_score(word) for word in words]
