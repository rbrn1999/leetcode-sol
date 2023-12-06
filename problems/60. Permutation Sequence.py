# link: https://leetcode.com/problems/permutation-sequence/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(num: int) -> int:
            product = 1
            for i in range(1, num+1):
                product *= i
            return product

        nums = list(range(1, n+1))
        ans = []
        k -= 1
        for i in range(n-1, -1, -1):
            f = factorial(i)
            ans.append(str(nums.pop(k // f)))
            k %= f
        
        return ''.join(ans)