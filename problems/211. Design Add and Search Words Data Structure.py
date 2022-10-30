# link: https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self, isEnd=False):
        self.isEnd = isEnd
        self.children = {} # val: node
class WordDictionary:
    def __init__(self):
        self.root = TrieNode('')
        
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True
    def search(self, word: str) -> bool:
        def helper(word, node):
            if word == "":
                if node.isEnd:
                    return True
            elif word[0] == '.':
                for child in node.children.values():
                    if helper(word[1:], child):
                        return True
                return False
            elif word[0] in node.children:
                return helper(word[1:], node.children[word[0]])
            return False
            
        return helper(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)