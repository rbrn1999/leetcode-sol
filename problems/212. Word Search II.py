# link: https://leetcode.com/problems/word-search-ii/

class TrieNode:
    def __init__(self, isEnd=False, wordInd=-1):
        self.isEnd = isEnd
        self.wordInd = wordInd
        self.children = {}

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        
        m, n = len(board), len(board[0])

        root = TrieNode()
        for i, word in enumerate(words):
            node = root
            for c in word:
                node = node.children.setdefault(c, TrieNode())
            node.isEnd = True
            node.wordInd = i
            
        res = []
        visited = set()
        def dfs(i, j, node):
            if i<0 or j<0 or i>=m or j>=n or (i, j) in visited or board[i][j] not in node.children:
                return
            visited.add((i, j))
            prev, node = node, node.children[board[i][j]]
            if node.isEnd:
                nonlocal res
                res.append(words[node.wordInd])
                node.isEnd = False
                if len(node.children) == 0:
                    del prev.children[board[i][j]]
                
            dfs(i-1, j, node)
            dfs(i+1, j, node)
            dfs(i, j-1, node)
            dfs(i, j+1, node)
            visited.remove((i, j))
            
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res