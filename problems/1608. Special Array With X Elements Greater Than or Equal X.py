# link: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def specialArray(self, nums: list[int]) -> int:
        n = len(nums)
        freq = [0] * (n+1)
        # freq[x]: count of numbers which is = than x,
        # (exception: freq[n]: count of numbers >= n)

        for num in nums:
            freq[min(num, n)] += 1

        larger_or_greater = 0
        for x in range(n, -1, -1):
            larger_or_greater += freq[x]
            if x == larger_or_greater:
                return x

        return -1
