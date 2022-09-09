# link: https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n>0:
            weight += 1
            # remove the lease significant 1 e.g. 1100 & (1100-1) = 1100 & 1011 = 1000
            n &= n-1
        return weight