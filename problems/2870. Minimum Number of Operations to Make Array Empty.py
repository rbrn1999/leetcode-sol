# link: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

from collections import Counter
import math
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        num_count = Counter(nums)
        answer = 0
        for count in num_count.values():
            if count == 1:
                return -1
            answer += math.ceil(count / 3) # remain = 2: use a 2, remain = 1: remove one 3 and add two 2s.
        
        return answer