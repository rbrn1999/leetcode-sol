# link: https://leetcode.com/problems/sum-of-two-integers/
# solution reference: https://youtu.be/gVUrDV4tZfY

class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = a ^ b
        carry = (a & b) << 1

        while carry > 0:
            res, carry = res ^ carry, (carry & res) << 1

        return res

