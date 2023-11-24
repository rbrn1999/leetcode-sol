# link: https://leetcode.com/problems/count-nice-pairs-in-an-array/

from collections import defaultdict
class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        group_sizes = defaultdict(int)
        for num in nums:
            group_sizes[num - int(str(num)[::-1])] += 1
        
        pairs = 0
        for size in group_sizes.values():
            pairs += (size * (size-1) // 2) % (10 ** 9 + 7)
            pairs %= (10 ** 9 + 7)
        
        return pairs