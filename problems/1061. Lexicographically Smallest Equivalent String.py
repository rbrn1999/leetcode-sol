# link: https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class UnionFind():
    def __init__(self, chars):
        self.parent = {char: char for char in chars}

    def find(self, char: chr) -> chr:
        parent = self.parent[char]
        if parent != char:
            parent = self.find(parent)
            self.parent[char] = parent
        return parent

    def union(self, c1, c2):
        p1, p2 = self.find(c1), self.find(c2)
        if p1 == p2:
            return False
        else:
            if p1 > p2:
                p1, p2 = p2, p1
            self.parent[p2] = p1
            return True

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        unionFind = UnionFind(list(set(s1).union(set(s2)).union(set(baseStr))))
        for i in range(len(s1)):
            unionFind.union(s1[i], s2[i])

        result = []
        for char in baseStr:
            result.append(unionFind.find(char))

        return ''.join(result)

