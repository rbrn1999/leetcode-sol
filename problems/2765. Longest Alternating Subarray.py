# link: https://leetcode.com/problems/longest-alternating-subarray/

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        answer = -1
        i = 0
        while i < len(nums):
            end = i
            for j in range(i, len(nums)):
                if nums[j] != nums[i] + (j-i) % 2:
                    break
                end = j
            if end > i:
                answer = max(answer, end-i+1)
            i = max(i+1, end)

        return answer
    