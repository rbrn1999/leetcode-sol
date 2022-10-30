# link: https://leetcode.com/problems/implement-trie-prefix-tree/

class Node:
    def __init__(self, val, isEnd = False):
        self.val = val
        self.children = []
        self.isEnd = isEnd

class Trie:

    def __init__(self):
        self.head = Node('')

    def insert(self, word: str) -> None:
        cur = self.head
        for c in word:
            exist = False
            childInd = -1
            for i, node in enumerate(cur.children):
                if node.val == c:
                    exist = True
                    childInd = i
                    break
            if exist:
                cur = cur.children[childInd]
            else:
                node = Node(c)
                cur.children.append(node)
                cur = node
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.head
        for c in word:
            exist = False
            childInd = -1
            for i, node in enumerate(cur.children):
                if node.val == c:
                    exist = True
                    childInd = i
                    break
            if not exist:
                return False
            cur = cur.children[childInd]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for c in prefix:
            exist = False
            childInd = -1
            for i, node in enumerate(cur.children):
                if node.val == c:
                    exist = True
                    childInd = i
                    break
            if not exist:
                return False
            cur = cur.children[childInd]
        return True      


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)