# link: https://leetcode.com/problems/greatest-common-divisor-traversal/

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.size = [1] * n
        self.count = n

    def find(self, x):
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
        
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            self.par[px] = py
            self.size[py] += self.size[px]
        else:
            self.par[py] = px
            self.size[px] += self.size[py]
        self.count -= 1

class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        uf = UnionFind(len(nums))
        factor_index = {} # f -> index of value with factor f
        for i, n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0: # f is a prime
                    if f in factor_index:
                        uf.union(i, factor_index[f])
                    else:
                        factor_index[f] = i

                    # eliminate factors with f
                    while n % f == 0:
                        n //= f
                f += 1

            if n > 1:
                if n in factor_index:
                    uf.union(i, factor_index[n])
                else:
                    factor_index[n] = i
        
        return uf.count == 1