# link: https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        steps = 0
        n = len(nums)
        zeros = nums.count(0)
        while zeros < n:
            for i in range(n):
                if nums[i] % 2 == 1:
                    if nums[i] == 1:
                        zeros += 1
                    steps += 1
                nums[i] //= 2
            if zeros < n:
                steps += 1 # all elements divide by 2

        return steps

