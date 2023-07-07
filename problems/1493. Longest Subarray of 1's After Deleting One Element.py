# link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev = 0
        cur = 0
        result = 0
        flag = False

        for num in nums:
            if num == 1:
                cur += 1
            else:
                flag = True
                prev = cur
                cur = 0

            result = max(result, cur+prev)

        return result if flag else len(nums)-1

# sliding window
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0 # [start, end]
        zeroInd = -1
        result = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                if zeroInd == -1:
                    zeroInd = i
                else:
                    result = max(result, i-start-1)
                    start = zeroInd+1
                    zeroInd = i

        if nums[-1] == 1:
            result = max(result, len(nums)-start-1)

        return result
