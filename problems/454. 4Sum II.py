# link: https://leetcode.com/problems/4sum-ii/

import itertools
class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        # calculate every pair of num1 + num2, num3 + num4 -> O(n^2)
        # sum1 = all num1 + num2, sum2 = all num3 + num4
        # find sum1 + sum2 == 0 -> O(n^2)

        n = len(nums1)
        sum1 = {}
        result = 0
        for i, j in itertools.product(range(n), range(n)):
            total = nums1[i] + nums2[j]
            if total not in sum1:
                sum1[total] = 0
            sum1[total] += 1

        for k, l in itertools.product(range(n), range(n)):
            total = nums3[k] + nums4[l]
            if -total in sum1:
                result += sum1[-total]
        
        return result

        
            