# link: https://leetcode.com/problems/number-of-good-pairs/
from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = Counter(nums)
        answer = 0
        for c in count.values():
            if c < 2:
                continue
            answer += c * (c-1) // 2
        
        return answer