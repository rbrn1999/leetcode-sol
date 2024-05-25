# link: https://leetcode.com/problems/word-break-ii/

# Trie, DP
class Node:
    def __init__(self, c: chr, isEnd: bool=False):
        self.c = c
        self.isEnd = isEnd
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node('')
    
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node(c)
            cur = cur.children[c]
        
        cur.isEnd = True
    
    def search(self, c: chr, node: Node) -> Node:
        if c in node.children:
            return node.children[c]
        else:
            return node # not found

from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        words = []
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        @cache
        def dfs(i: int) -> list[bool, list[list[str]]]:
            if i == len(s):
                return [True, [['']]]
            result = []

            node = trie.root
            for r in range(i, len(s)):
                next_node = trie.search(s[r], node)
                if node == next_node:
                    break
                else:
                    node = next_node
                
                if node.isEnd:
                    isValid, words_lists = dfs(r+1)
                    if isValid:
                        for words in words_lists:
                            result.append([s[i:r+1]] + words)
            
            if result:
                return [True, result]
            else:
                return [False, []]
        
        words_lists = dfs(0)[1]
        if not words_lists:
            return []
            
        return [' '.join(words[:-1]) for words in words_lists]


# Backtracking
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
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

