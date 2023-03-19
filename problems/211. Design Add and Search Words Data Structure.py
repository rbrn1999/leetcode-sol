# link: https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            node.children.setdefault(c, TrieNode())
            node = node.children[c]
        node.isEnd = True

    def __search(self, word, node) -> bool:
        for i in range(len(word)):
            if word[i] == '.':
                return any(self.__search(word[i+1:], child) for child in node.children.values())
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
        return node.isEnd

    def search(self, word: str) -> bool:
        return self.__search(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)