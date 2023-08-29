# link: https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: list[int], x: int) -> int:
        if x == 0: 
            return 0
        sl = SortedList(nums[x:])
        min_diff = float('inf')
        for i in range(len(nums)-x):
            j = sl.bisect_left(nums[i])
            diff = float('inf')
            if j < len(sl):
                diff = abs(nums[i]-sl[j])
            if j > 0:
                diff = min(diff, nums[i]-sl[j-1])
            min_diff = min(diff, min_diff)
            sl.remove(nums[i+x])
        
        return min_diff
