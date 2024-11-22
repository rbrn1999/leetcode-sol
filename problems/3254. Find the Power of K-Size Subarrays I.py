# link: https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

# 2-pass
class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        result = [-1] * (n - (k-1))
        i = 0
        while i < (n - (k-1)):
            j = i
            # find the consequtive sequence
            while j + 1 < n and nums[j]+1 == nums[j+1]:
                j += 1

            for l in range(i, j-k+2):
                result[l] = nums[l+k-1] # the last element of each subarray

            i = j + 1

        return result

# 1-pass
class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        streak = 0
        result = []
        for i in range(k-1):
            if nums[i-1] + 1 == nums[i]:
                streak += 1
            else:
                streak = 1

        for i in range(k-1, n):
            if nums[i-1] + 1 == nums[i]:
                streak += 1
            else:
                streak = 1

            result.append(nums[i] if streak >= k else -1)

        return result
