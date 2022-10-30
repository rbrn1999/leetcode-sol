# link: https://leetcode.com/problems/destroy-sequential-targets/

from collections import defaultdict
class Solution:
    def destroyTargets(self, nums: list[int], space: int) -> int:
        groups = defaultdict(list)
        for num in nums:
            groups[num % space].append(num)
        maxLen = 0
        res = float('inf')
        for group in groups.values():
            length = len(group)
            if length > maxLen:
                maxLen = len(group)
                res = min(group)
            elif length == maxLen and length > 0:
                res = min(res, min(group))
        return res