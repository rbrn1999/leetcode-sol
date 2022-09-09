# link: https://leetcode.com/problems/ugly-number-ii/
class Solution:
    # https://leetcode.com/problems/ugly-number-ii/discuss/718879/Python-O(n)-universal-dp-solution-explained
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        k = len(factors)
        nums = [1]
        cur_idx = [0] * k
        for _ in range(n-1):
            candidates = [nums[cur_idx[i]]*factors[i] for i in range(k)]
            num = min(candidates)
            nums.append(num)
            cur_idx = [cur_idx[i] + int(candidates[i] == num) for i in range(k)]
        return nums[-1]

    # First attempt (), too slow
    # from functools import lru_cache
    # from math import sqrt
    # def nthUglyNumber(self, n: int) -> int:
    #     @lru_cache(None)
    #     def isPrime(num):
    #         if num < 2:
    #             return False
    #         for i in range(2, int(sqrt(num))+1):
    #             if num % i == 0:
    #                 return False
    #         return True
    #     def helper(num) -> bool:
    #         for i in range(1, int(sqrt(num))+1):
    #             if num % i == 0:
    #                 if isPrime(i) and i not in {2, 3, 5}:
    #                     return False
    #                 if isPrime(num//i) and num//i not in {2, 3, 5}:
    #                     return False
    #         return True

    #     i = num = 1
    #     l = []
    #     while i <= n:
    #         if helper(num):
    #             if i == n:
    #                 return num
    #             else:
    #                 i += 1
    #         num += 1
    #     return -1
                
print(Solution().nthUglyNumber(400))