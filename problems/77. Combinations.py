# link: https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        comb = []
        def helper(i, n=n, k=k):
            if k == 0:
                result.append(comb.copy())

            for num in range(i, n+1):
                comb.append(num)
                helper(num+1, n, k-1)
                comb.pop()
        
        helper(1)
        return result
        
    def combine(self, n: int, k: int) -> list[list[int]]:
        def helper(i, n=n, k=k):
            if k == 0:
                return [[]]
            result = []
            for num in range(i, n+1):
                for comb in helper(num+1, n, k-1):
                    result.append([num] + comb)

            return result

        return helper(1)

