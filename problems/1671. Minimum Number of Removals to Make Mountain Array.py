# link: https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

import bisect
class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        def minRemoves(pivot: int) -> int:
            dp = []
            for i in range(pivot):
                j = bisect.bisect_left(dp, nums[i])
                if j < len(dp):
                    dp[j] = nums[i]
                else:
                    dp.append(nums[i])
            i = bisect.bisect_left(dp, nums[pivot])
            if i == 0:
                return len(nums)
            removes = pivot - i

            dp = []
            for i in range(len(nums)-1, pivot, -1):
                j = bisect.bisect_left(dp, nums[i])
                if j < len(dp):
                    dp[j] = nums[i]
                else:
                    dp.append(nums[i])
            i = bisect.bisect_left(dp, nums[pivot])
            if i == 0:
                return len(nums)
            removes += len(nums) - 1 - pivot - i
            return removes

        result = len(nums)-3
        for pivot in range(1, len(nums)-1):
            result = min(minRemoves(pivot), result)

        return result
