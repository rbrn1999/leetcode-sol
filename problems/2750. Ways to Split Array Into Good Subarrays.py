# link: https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        firstOne = -1
        lastOne = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                firstOne = i
                break

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 1:
                lastOne = i
                break

        if firstOne == -1:
            return 0

        zeros = 0
        answer = 1
        for i in range(firstOne+1, lastOne+1):
            if nums[i] == 0:
                zeros += 1
            elif zeros != 0:
                answer = answer * (zeros+1) % (10 ** 9 + 7)
                zeros = 0

        return answer

