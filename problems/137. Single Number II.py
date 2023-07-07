# link: https://leetcode.com/problems/single-number-ii/

from collections import defaultdict
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] == 3:
                del count[num]
        
        return next(iter(count.keys()))