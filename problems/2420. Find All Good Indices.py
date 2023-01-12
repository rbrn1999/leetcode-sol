# link: https://leetcode.com/problems/find-all-good-indices/

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        decreaseStreak = [1] * n
        increaseStreak = [1] * n

        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                decreaseStreak[i] = decreaseStreak[i-1] + 1

        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                increaseStreak[i] = increaseStreak[i+1] + 1

        result = []
        for i in range(k, n-k):
            if decreaseStreak[i-1] >= k and increaseStreak[i+1] >= k:
                result.append(i)

        return result

