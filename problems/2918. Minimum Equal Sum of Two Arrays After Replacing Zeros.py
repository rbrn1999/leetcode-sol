# link: https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        flag1 = False
        flag2 = False
        sum1 = sum2 = 0
        for i in range(len(nums1)):
            if nums1[i] == 0:
                flag1 = True
                nums1[i] = 1
            sum1 += nums1[i]
        for i in range(len(nums2)):
            if nums2[i] == 0:
                flag2 = True
                nums2[i] = 1
            sum2 += nums2[i]
        
        if not flag1 and not flag2 and sum1 != sum2:
            return -1
        if not flag1 and sum2 > sum1:
            return -1
        if not flag2 and sum1 > sum2:
            return -1
        
        return max(sum1, sum2)