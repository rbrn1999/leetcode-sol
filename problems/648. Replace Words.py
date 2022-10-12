# link: https://leetcode.com/problems/replace-words/

class Node:
    def __init__(self, char):
        self.char = char
        self.isEnd = False
        self.children = {}
class Trie:
    def __init__(self):
        self.root = Node("")

    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                newNode = Node(char)
                node.children[char] = newNode
                node = newNode
        node.isEnd = True

    def search(self, word): # return the shortest matched root or return word
        node = self.root
        for i, char in enumerate(word):
            if char in node.children:
                node = node.children[char]
                if node.isEnd:
                    return word[:i+1]
            else:
                break
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            trie.insert(root)
        return ' '.join(map(trie.search, sentence.split()))
