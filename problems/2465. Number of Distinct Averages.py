# link: https://leetcode.com/problems/number-of-distinct-averages/

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        s = set()
        l = 0
        r = len(nums) - 1
        nums.sort()
        while l <= r:
            s.add((nums[l] + nums[r]) / 2)
            l += 1
            r -= 1
        return len(s)
