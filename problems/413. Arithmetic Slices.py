# link: https://leetcode.com/problems/arithmetic-slices/

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        answer = 0
        subCount = 0 # count of arithmetic subarrays that ended at the current index
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                subCount += 1
            else:
                subCount = 0
            answer += subCount

        return answer

