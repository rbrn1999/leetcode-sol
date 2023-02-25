# link: https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        answer = [-1] * len(nums)
        cur = 0
        for i in range(len(nums)):
            cur ^= nums[i]
            answer[~i] = cur ^ (2 ** maximumBit - 1)
        return answer

