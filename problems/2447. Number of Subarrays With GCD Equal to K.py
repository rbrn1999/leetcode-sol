import math

class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:
        res = 0
        for l in range(len(nums)):
            gcd = nums[l]
            for r in range(l, len(nums)):
                gcd = math.gcd(gcd, nums[r])
                if gcd < k:
                    break
                if gcd == k:
                    res += 1
        return res             