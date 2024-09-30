# link: https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

# HashSet
class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        result = 0
        prefixs = set()
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        for num in arr1:
            while num > 0:
                prefixs.add(num)
                num //= 10

        for num in arr2:
            while num > 0:
                if num in prefixs:
                    result = max(result, len(str(num)))
                    break
                else:
                    num //= 10

        return result

# Trie
class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self, arr:list[int]):
        self.root = TrieNode()
        for num in arr:
            self.insert(str(num))

    def insert(self, s: str):
        cur = self.root
        for c in s:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

    def search_depth(self, s: str) -> int:
        depth = 0
        cur = self.root
        for i, c in enumerate(s):
            if c in cur.children:
                cur = cur.children[c]
            else:
                return i

        return len(s)


class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        trie = Trie(arr1)
        return max(trie.search_depth(str(num)) for num in arr2)
