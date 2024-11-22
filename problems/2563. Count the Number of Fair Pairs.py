# link: https://leetcode.com/problems/count-the-number-of-fair-pairs/

class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        count = 0
        while l < r and nums[l] + nums[r] < lower:
            l += 1

        while l < r and nums[l] + nums[r] > upper:
            r -= 1

        j1 = l + 1
        j2 = r
        while j1 < r and nums[0] + nums[j1] < lower:
            j1 += 1
        while j2 >= j1 and nums[0] + nums[j2] > upper:
            j2 -= 1

        for i in range(l, r):
            j1 = max(i+1, j1)
            while j1-1 > i and nums[i] + nums[j1-1] >= lower:
                j1 -= 1
            while j2-1 > i and nums[i] + nums[j2] > upper:
                j2 -= 1

            if lower <= nums[i] + nums[j1] <= upper and lower <= nums[i] + nums[j2] <= upper:
                count += j2 - j1 + 1

        return count
