# link: https://leetcode.com/problems/make-array-strictly-increasing/

from functools import cache
import bisect
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        @cache
        def helper(i, prev=-1):
            if i == len(arr1):
                return 0
            ops = float('inf')
            if arr1[i] > prev:
                ops = helper(i+1, arr1[i])
            j = bisect.bisect_right(arr2, prev)
            if j < len(arr2):
                ops = min(ops, 1 + helper(i+1, arr2[j]))

            return ops

        res = helper(0)
        return res if res < float('inf') else -1

