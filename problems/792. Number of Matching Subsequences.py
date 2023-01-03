# link: https://leetcode.com/problems/number-of-matching-subsequences/

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.head = TrieNode()
    def insert(self, word):
        cur = self.head
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

    def insert_all(self, char, node):
        for child in node.children:
            self.insert_all(char, child)
        if char not in node.children:
            node.children[char] = TrieNode()
            

    def search(self, word) -> bool:
        cur = self.head
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
            
class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        trie = Trie()
        count = 0
        for c in s:
            trie.insert_all(c, trie.head)
        for word in words:
            if trie.search(word):
                count += 1

        return count


s = "abcde"
words = ["a","bb","acd","ace"]

print(Solution().numMatchingSubseq(s, words))