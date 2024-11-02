# link: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self, paths: list[str]):
        self.root = TrieNode()
        for path in paths:
            self.insert(path)

    def insert(self, path: str):
        node = self.root
        for folder in path.split('/')[1:]:
            if folder not in node.children:
                node.children[folder] = TrieNode()
            node = node.children[folder]

        node.isEnd = True

    def isSubFolder(self, path: str) -> bool:
        node = self.root
        for folder in path.split('/')[1:-1]:
            if folder not in node.children:
                return False
            node = node.children[folder]
            if node.isEnd:
                return True

        return False


class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        trie = Trie(folder)
        return [f for f in folder if not trie.isSubFolder(f)]
